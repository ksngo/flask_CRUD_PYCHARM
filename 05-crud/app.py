from flask import Flask, render_template, request, redirect, url_for
import os
import data
import random

app = Flask(__name__)

@app.route('/')
def display_employees():
    # 'R' => READ
    employees = data.read_data()
    return render_template('list_employees.template.html', employees=employees)

@app.route('/add_employee')
def add_employee():
    return render_template('add_employee.template.html')


@app.route('/edit_employee/<id>')
def edit_employee(id):
    employee = data.find_employee_by_id(id)
    return render_template('edit_employee.template.html', employee=employee)


@app.route('/edit_employee/<id>', methods=['POST'])
def process_edit_employee(id):
    
    #1 - read in the database
    database = data.read_data()

    #2 - update the entry in the database
    employee_to_update = data.find_employee_by_id(id)
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
    data.write_data(database)
    return redirect(url_for('display_employees'))


@app.route('/add_employee', methods=['POST'])
def process_add_employee():

    employee_id = random.randint(5,9999) #we generate a random number to be the id
    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    title = request.form.get('title')
    salary = request.form.get('salary')
    data.add_new_employee(employee_id, first_name, last_name, title, salary)
    return redirect(url_for('display_employees'))

@app.route('/confirm_delete_employee/<id>')
def confirm_delete(id):

    #1 find the index of the employee that we want to delete
    employee_to_delete = data.find_employee_by_id(id)

    return render_template('confirm_delete.template.html', employee=employee_to_delete)


@app.route('/delete_employee/<id>', methods=['POST'])
def delete_employee(id):

    #0 load in the database
    database = data.read_data()

    #1 find the index of the employee that we want to delete
    employee_to_delete = data.find_employee_by_id(id)

    #2 remove that index from the database list
    for index,e in enumerate(database):
        if e['id'] == employee_to_delete['id']:
            # update the entry in the databse
            database[index] = employee_to_delete
            break # break out of the loop because each id is unique

    del database[index]

    #3 write the whole database back to the file
    data.write_data(database)

    return redirect(url_for('display_employees'))

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='localhost',
            port=8080,
            debug=True)