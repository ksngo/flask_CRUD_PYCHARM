from flask import Flask, render_template, request, redirect, url_for
import random
import csv
import os

app = Flask(__name__)

def read_data():
    fp = open('sample_hrm.csv','r')
    reader = csv.reader(fp, delimiter=',')
    next(reader) #skip the first line
    
    database=[]
    for line in reader:
        employee = {
            "id":int(line[0]),
            "first_name":line[1],
            "last_name":line[2],
            "title":line[3],
            "salary":float(line[4])
        }
        database.append(employee)

    fp.close()
    return database

def find_employee_by_id(wanted_id):
    database = read_data()
    print(type(wanted_id))
    # linear search algo
    for each_employee in database:
        if each_employee['id'] == int(wanted_id):
            print("found")
            return each_employee

@app.route('/')
def display_employees():
    # 'R' => READ
    employees = read_data()
    return render_template('list_employees.template.html', employees=employees)

@app.route('/add_employee')
def add_employee():
    return render_template('add_employee.template.html')


@app.route('/edit_employee/<id>')
def edit_employee(id):
    employee = find_employee_by_id(id)
    return render_template('edit_employee.template.html', employee=employee)

@app.route('/add_employee', methods=['POST'])
def process_add_employee():
    with open('sample_hrm.csv', 'a') as fp:
        employee_id = random.randint(5,9999)
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        title = request.form.get('title')
        salary = request.form.get('salary')
        writer = csv.writer(fp, delimiter=',')
        writer.writerow([employee_id, first_name, last_name, title, salary])
    return redirect(url_for('display_employees'))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)