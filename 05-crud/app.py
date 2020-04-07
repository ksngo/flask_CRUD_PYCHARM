from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/')
def display_employees():
    # 'R' => READ
    employees = read_data()
    return render_template('list_employees.template.html', employees=employees)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)