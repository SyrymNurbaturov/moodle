import json

import moodle

# Login admin
# Password admin
# There only one admin IF you wanna change admin the password is 123456

information = json.load(open("information.json"))

while True:
    print("\t\t\t\tWELCOME TO MOODLE OF ASTANA IT UNIVERSITY\t\t\t\t")
    print("\n")
    print("1. Log on")
    print("0. Exit")
    print("\n\n------------------------------------------------------------------------------------\n\n")
    option = int(input("Choose the option: "))
    if option == 1:
        print("Are you:")
        print("1. admin")
        print("2. student")
        print("3. teacher")
        print("0. Exit")
        print("\n\n------------------------------------------------------------------------------------\n\n")
        option = int(input("Choose the role: "))
        if option == 1:
            login = str(input("Login: "))
            password = str(input("Password: "))
            role = "admin"
            if moodle.access(login, password, role) == True:
                print("Welcome %s" % information[role.lower()]["fullName"])
                moodle.adminTools()
            else:
                break
        elif option == 2:
            login = str(input("Login: "))
            password = str(input("Password: "))
            role = "student"
            if moodle.access(login, password, role) == True:
                print("Welcome %s" % information[login[:6]]["fullName"])
                moodle.studentTool(login)
            else:
                break
        elif option == 3:
            login = str(input("Login: "))
            password = str(input("Password: "))
            role = "teacher"
            if moodle.access(login, password, role) == True:
                print("Welcome %s" % information[login[:-16]]["fullName"])
                moodle.teacherTool(login)
            else:
                break

        else:
            break
    else:
        break