import csv


def add_new_employee(employee_id, first_name, last_name, title, salary):
    with open('sample_hrm.csv', 'a') as fp:
        writer = csv.writer(fp, delimiter=',')
        writer.writerow([employee_id, first_name, last_name, title, salary])

def write_data(database):
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
