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

    # linear search algo
    for each_employee in database:
        if each_employee['id'] == int(wanted_id):
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


@app.route('/edit_employee/<id>', methods=['POST'])
def process_edit_employee(id):
    
    #1 - read in the database
    database = read_data()

    #2 - update the entry in the database
    employee_to_update = find_employee_by_id(id)
    employee_to_update['first_name'] = request.form.get('firstname')
    employee_to_update['last_name'] = request.form.get('lastname')
    employee_to_update['salary'] = request.form.get('salary')
    employee_to_update['title'] = request.form.get('title')
 
    #find the index to replace
    for index,e in enumerate(database):
        if e['id'] == employee_to_update['id']:
            # update the entry in the databse
            database[index] = employee_to_update
            break # break out of the loop because each id is unique

    #3 - overwrite the file with our current version of database
    with open('sample_hrm.csv', 'w') as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(['id','first_name','last_name','title','salary'])
        for eachEntry in database:
            employee_id = eachEntry['id']
            first_name = eachEntry['first_name']
            last_name = eachEntry['last_name']
            title = eachEntry['title']
            salary =eachEntry['salary']
            writer.writerow([employee_id, first_name, last_name, title, salary])
    return redirect(url_for('display_employees'))


@app.route('/add_employee', methods=['POST'])
def process_add_employee():
    with open('sample_hrm.csv', 'a') as fp:
        employee_id = random.randint(5,9999) #we generate a random number to be the id
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