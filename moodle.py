from pprint import pprint
import json
from Admin import New_Admin

from Student import New_Student

from Teacher import New_Teacher

def authorization(login, password, role):
    isAdmin = False
    isStudent = False
    isTeacher = False

    pas = int(123456)

    if role == 'admin':
        print("For be new admin enter the password")
        isNew = int(input())
        if pas == isNew:
            isAdmin = True
        else:
            return 0
    elif role == 'student':
        isStudent = True
    elif role == 'teacher':
        isTeacher = True

    if isAdmin:
        admin = json.load(open('access.json'))

        admin = dict(admin)

        login_list = []
        login_list.append(login)

        password_list = []
        password_list.append(password)

        admin["admin"] = {"login": login_list, "password": password_list}

        #def __init__(self, name, surname, age, isMale, login, password):
        main_admin = New_Admin(input("Name: "), input("Surname: "), input("Age: "), input("Are you Male, True or False?: "), admin["admin"]["login"], admin["admin"]["password"])

        information = json.load(open("information.json"))

        information = dict(information)

        information["admin"] = {"fullName": main_admin.getFullName(), "age": main_admin.getAge(), "isMale": main_admin.getGender(),"login":main_admin.getLogin(), "password":main_admin.getPassword()}

        with open('information.json', 'w') as informationWF:
            json.dump(information, informationWF, indent=2)

        with open('access.json', 'w') as adminWF:
            json.dump(admin, adminWF, indent=2)
        return 1

    if isStudent:
        course = dict(json.load(open("course.json")))
        student = dict(json.load(open('access.json')))

        student = dict(student)
        if "student" in student.keys():

            accesss = True
            information = dict(json.load(open("information.json")))

            if login[:6] in information.keys():
                accesss = False


            if accesss:
                login_list = student['student']['login']

                login_list = list(login_list)

                login_list.append(login)

                password_list = student['student']['password']

                password_list = list(password_list)

                password_list.append(password)

                student['student'] = {"login": login_list,"password":password_list}


                new_student = New_Student(input("Name: "), input("Surname: "), input("Age: "),
                                          input("Are you Male, True or False?: "), login,
                                          password, input("Group: "),
                                          login[:6])

                information[new_student.getBarcode()] = {"fullName": new_student.getFullName(), "age": new_student.getAge(),
                                                         "isMale": new_student.getGender(), "login": new_student.getLogin(),
                                                         "password": new_student.getPassword(), "group": new_student.group,
                                                         "barcode": new_student.getBarcode()}
                groupping(new_student)
                # def __init__(self, name, surname, age, isMale, login, password, group, barcode):

                courses = []

                for i in course.keys():
                    courses.append(str(i))


                for i in courses:
                    if new_student.group in course[i]["groups"].keys():
                        course[i]['groups'][new_student.group][str(new_student.getBarcode())] = {
                            "fullName": new_student.getFullName(), "login": new_student.getLogin()}


                with open('course.json','w') as courseWF:
                    json.dump(course, courseWF, indent=2)

                with open('information.json', 'w') as informationWF:
                    json.dump(information, informationWF, indent=2)

                with open('access.json', 'w') as studentWF:
                    json.dump(student, studentWF, indent=2)

                return 1
            else:
                print("This student is already studying there")
                return 0


        else:
            login_list = []
            login_list.append(login)

            password_list = []
            password_list.append(password)

            student["student"] = {"login": login_list, "password":password_list}

            new_student = New_Student(input("Name: "), input("Surname: "), input("Age: "),
                                      input("Are you Male, True or False?: "), login,
                                      password, input("Group: "),
                                      login[:6])
            information = json.load(open("information.json"))

            information = dict(information)

            information[new_student.getBarcode()] = {"fullName": new_student.getFullName(), "age": new_student.getAge(),
                                                     "isMale": new_student.getGender(), "login": new_student.getLogin(),
                                                     "password": new_student.getPassword(), "group": new_student.group,
                                                     "barcode": new_student.getBarcode()}
            groupping(new_student)
            # def __init__(self, name, surname, age, isMale, login, password, group, barcode):

            with open('information.json', 'w') as informationWF:
                json.dump(information, informationWF, indent=2)

            with open('access.json', 'w') as studentWF:
                json.dump(student, studentWF, indent=2)

            return 1



    if isTeacher:

        accesss = True

        information = dict(json.load(open("information.json")))

        teacher = json.load(open('access.json'))

        teacher = dict(teacher)

        if login[:-16] in information.keys():
            accesss = False
        if "teacher" in teacher.keys():

            if accesss:

                login_list = teacher['teacher']['login']

                login_list = list(login_list)

                login_list.append(login)

                password_list = teacher['teacher']['password']

                password_list = list(password_list)

                password_list.append(password)

                teacher['teacher'] = {"login": login_list, "password": password_list}

                #def __init__(self, name, surname, age, isMale, login, password):
                new_teacher = New_Teacher(input("Name: "), input("Surname: "), input("Age: "),
                                          input("Are you Male, True or False?: "), login,
                                          password, input("Subject: "))

                information[new_teacher.getBarcode()] = {"fullName": new_teacher.getFullName(), "age": new_teacher.getAge(),
                                                         "isMale": new_teacher.getGender(), "login": new_teacher.getLogin(),
                                                         "password": new_teacher.getPassword(), "barcode": new_teacher.getBarcode(),"subject":new_teacher.subject}
                with open('information.json', 'w') as informationWF:
                    json.dump(information, informationWF, indent=2)

                with open('access.json', 'w') as teacherWF:
                    json.dump(teacher, teacherWF, indent=2)

                return 1

            else:
                print("This teacher is already exist")
                return 0
        else:
            login_list = []
            login_list.append(login)

            password_list = []
            password_list.append(password)

            teacher["teacher"] = {"login": login_list, "password": password_list}

            new_teacher = New_Teacher(input("Name: "), input("Surname: "), input("Age: "),
                                      input("Are you Male, True or False?: "), login,
                                      password,input("Subject: "))

            information[new_teacher.getBarcode()] = {"fullName": new_teacher.getFullName(), "age": new_teacher.getAge(),
                                                     "isMale": new_teacher.getGender(), "login": new_teacher.getLogin(),
                                                     "password": new_teacher.getPassword(),
                                                     "barcode": new_teacher.getBarcode(),"subject":new_teacher.subject}
            with open('information.json', 'w') as informationWF:
                json.dump(information, informationWF, indent=2)

            with open('access.json', 'w') as teacherWF:
                json.dump(teacher, teacherWF, indent=2)

            return 1

    if isTeacher == False and isAdmin == False and isStudent == False:
        return 0



def access(login, password, role):
    isHaveAccess = False

    accesss = json.load(open('access.json'))

    accesss = dict(accesss)

    checker = int(0)
    index_login = int(-1)
    list_login = accesss[role]['login']
    list_login = list(list_login)
    for i in list_login:
        if login in i:
            checker = 1
            index_login = list_login.index(i)
            if password == accesss[role]['password'][index_login] and checker==1:
                isHaveAccess = True
                return isHaveAccess
    return isHaveAccess

def courseCreation():
    information = dict(json.load(open("information.json")))

    list_course = []
    seperator = ", "
    for i in information.keys():
        if len(i) > 6:
            list_course.append(information[i]["subject"])

    pprint("This is our courses that have a teacher: %s"%seperator.join(list_course))

    courseName = str(input("Name of the course: "))

    accesss = True

    group = dict(json.load(open("groups.json")))

    course = dict(json.load(open('course.json')))

    if accesss:
        list1 = list(group.keys())

        information = dict(json.load(open("information.json")))

        teachers = []

        seperator = ", "
        for i in information.keys():
            if len(i) > 6:
                if courseName == information[i]["subject"]:
                    teachers.append(information[i]['barcode'])

        print("Teachers with barcode: %s" % seperator.join(teachers))

        barcode_teacher = str(input("Which will be a course teacher Please input a barcode: "))

        if barcode_teacher in information.keys():
            teacher = {"fullName": information[barcode_teacher]["fullName"],
                                    "login": information[barcode_teacher]["login"],
                                    "barcode": information[barcode_teacher]["barcode"]}
            group_quantity = int(input("Please input quantity of group: "))

            list2 = []
            if group_quantity>len(list1):
                return "Not correct input"
            else:
                i = 0
                seperator = ", "
                while i<group_quantity:
                    print(seperator.join(group.keys()))
                    group_name = str(input("Group name: "))
                    if group_name in group.keys():
                         list2.append(group_name)
                         i+=1
                    else:
                        print("Not correct input")

            for i in list1:
                if i in list2:
                    continue
                else:
                    del group[i]

            course[courseName] =  {"groups":group,"teacher":teacher}

            with open("course.json", 'w') as courseWF:
                json.dump(course, courseWF, indent=2)
            return "Done"
        else:
            return "Not correct input"
    else:
        return "This course already exist"

def delete(role):

    if role == 'student':
        information = dict(json.load(open("information.json")))

        access = dict(json.load(open("access.json")))

        logins = list(access['student']['login'])

        course = dict(json.load(open('course.json')))

        groups = dict(json.load(open('groups.json')))


        for i in range(len(logins)):
            a = logins[i]
            logins[i] = a[:6]
        students = dict()
        for i in information.keys():
            if len(i) == 6:
                students[i] = information[i]

        pprint(students)

        barcode = str(input("Which student you want to delete from University:(barcode) "))

        if barcode in information.keys():
            courses = []
            for i in course.keys():
                courses.append(str(i))

            for i in courses:
                if information[barcode]["group"] in course[i]["groups"].keys():
                    del course[i]['groups'][information[barcode]["group"]][information[barcode]["barcode"]]

            del groups[information[barcode]['group']][barcode]
            del information[barcode]
            save_index = logins.index(barcode)


            del access['student']['login'][save_index]
            del access['student']['password'][save_index]

            with open('course.json','w') as courseWF:
                json.dump(course, courseWF,indent=2)
            with open("information.json",'w') as informationWF:
                json.dump(information, informationWF, indent=2)
            with open("access.json",'w') as accessWF:
                json.dump(access, accessWF, indent=2)
            with open("groups.json",'w') as groupsWF:
                json.dump(groups, groupsWF, indent=2)
            return "Done"
        else:
            return "Not correct input"
    elif role == 'teacher':
        information = dict(json.load(open("information.json")))

        access = dict(json.load(open("access.json")))

        logins = list(access['teacher']['login'])

        course = dict(json.load(open('course.json')))

        for i in range(len(logins)):
            a = logins[i]
            logins[i] = a[:-16]

        teachers = dict()

        for i in information.keys():
            if len(i) > 6:
                teachers[i] = information[i]

        pprint(teachers)

        barcode = str(input("Which teacher you want to delete from University:(barcode) "))
        if barcode in information.keys():

            if barcode in course[information[barcode]['subject']]['teacher']['barcode']:
                del course[information[barcode]['subject']]['teacher']
            del information[barcode]
            save_index = logins.index(barcode)

            del access['teacher']['login'][save_index]
            del access['teacher']['password'][save_index]

            with open('course.json', 'w') as courseWF:
                json.dump(course, courseWF, indent=2)
            with open("information.json", 'w') as informationWF:
                json.dump(information, informationWF, indent=2)
            with open("access.json", 'w') as accessWF:
                json.dump(access, accessWF, indent=2)
            return "Done"
        else:
            return "Not correct input"
    elif role == 'course':
        course = dict(json.load(open("course.json")))
        courses = []
        seperator = ', '
        for i in course.keys():
            courses.append(i)
        pprint(seperator.join(courses))
        course_name = str(input("Which course you want to delete: "))

        if course_name in course.keys():
            del course[course_name]

            with open('course.json', 'w') as courseWF:
                json.dump(course, courseWF, indent=2)
            return "Done"
        else:
            return "Not correct input"

def adminTools():

    done = False

    while done==False:
        print("1. Create")
        print("2. Update")
        print("3. Delete")
        print("4. Show")
        print("0. Exit")
        print("\n\n------------------------------------------------------------------------------------\n\n")
        option = int(input("Choose option: "))
        if option == 1:
            print("1. Create new Student")
            print("2. Create new Teacher")
            print("3. Change admin to new")
            print("4. Create new course")
            print("0. Back")
            option = int(input("Choose option: "))
            if option == 1:
                login = input(
                    "Login: (the first 6 variable must be barcode of student and end must be @astanait.edu.kz)   ")
                password = input("Password: ")
                role = "student"
                authorization(login, password, role)
            elif option == 2:
                login = input(
                    "Login: (start must be name and surname of teacher and end must be @astanait.edu.kz)   ")
                password = input("Password: ")
                role = "teacher"
                authorization(login, password, role)
            elif option == 3:
                login = input("Login: ")
                password = input("Password: ")
                role = "admin"
                authorization(login,password,role)
            elif option == 4:
                print(courseCreation())
        elif option == 2:
            print("1. Update student")
            print("2. Update teacher")
            print("3. Update course")
            print("0. Back")
            option = int(input("Choose the option: "))
            if option == 1:
                role = "student"
                update(role)
            elif option == 2:
                role = "teacher"
                update(role)
            elif option == 3:
                role = "course"
                update(role)
        elif option == 3:
            print("1. Delete student")
            print("2. Delete teacher")
            print("3. Delete course")
            print("0. Back")
            option = int(input("Choose the option: "))
            if option==1:
                role = "student"
                delete(role)
            elif option==2:
                role = "teacher"
                delete(role)
            elif option==3:
                role = "course"
                delete(role)

        elif option == 4:
            print("1. Show all students")
            print("2. Show all teachers")
            print("3. Show all courses")
            print("0. Back")

            option = int(input("Choose the option: "))
            if option==1:
                role = "student"
                pprint(show(role))
            elif option == 2:
                role = "teacher"
                pprint(show(role))
            elif option == 3:
                role = "course"
                pprint(show(role))
        elif option == 0:
            done = True



def update(role):
    information = dict(json.load(open("information.json")))
    if role == 'student':
        students = dict()
        for i in information.keys():
            if len(i) == 6:
                students[i] = information[i]

        pprint(students)
        done = False
        barcode = str(input("Barcode of the student: "))
        while done == False:
            print("What you want update: ")
            print("1. Age")
            print("2. Gender")
            print("0. Back")
            option = int(input("Choose the option: "))
            if option==1:
                print("Current age: %s"%information[barcode]["age"])
                forWhat = str(input("For what: "))
                information[barcode]['age'] = forWhat
                with open("information.json", 'w') as informationWF:
                    json.dump(information,informationWF, indent=2)
                print("Done")
                done = True

            elif option==2:
                if information[barcode]["isMale"] == 'True':
                    print("Current gender: male")
                else:
                    print("Current gender: female")
                forWhat = str(input("For what:(Male or Female) "))
                if forWhat.lower()=="male":
                    forWhat=True
                else:
                    forWhat=False
                information[barcode]['isMale'] = forWhat
                with open("information.json", 'w') as informationWF:
                    json.dump(information, informationWF, indent=2)
                print("Done")
                done = True
            else:
                return 0
    elif role == 'teacher':
        teachers = dict()
        for i in information.keys():
            if len(i) > 6:
                teachers[i] = information[i]

        pprint(teachers)
        done = False
        barcode = str(input("Barcode of the teacher: "))
        while done == False:
            print("What you want update: ")
            print("1. Age")
            print("2. Gender")
            print("0. Back")
            option = int(input("Choose the option: "))
            if option == 1:
                print("Current age: %s" % information[barcode]["age"])
                forWhat = str(input("For what: "))
                information[barcode]['age'] = forWhat
                with open("information.json", 'w') as informationWF:
                    json.dump(information, informationWF, indent=2)
                print("Done")
                done = True
            elif option == 2:
                if information[barcode]["isMale"] == 'True':
                    print("Current gender: male")
                else:
                    print("Current gender: female")
                forWhat = str(input("For what:(Male or Female) "))
                if forWhat.lower() == "male":
                    forWhat = True
                else:
                    forWhat = False
                information[barcode]['isMale'] = forWhat
                with open("information.json", 'w') as informationWF:
                    json.dump(information, informationWF, indent=2)
                    print("Done")
                done = True
            else:
                done = True
    elif role == 'course':
        seperator = ", "
        course = dict(json.load(open("course.json")))
        pprint(seperator.join(course.keys()))

        course_name = str(input("name of course: "))

        information = dict(json.load(open("information.json")))

        done = False

        while done==False:
            print("What you want update")
            print("1. Teacher of the course")
            print("2. Group of course")
            print("0. back")
            option = int(input("Choose the option: "))
            if option == 1:
                if 'teacher' not in course[course_name].keys():
                    print("There free space: (need a teacher) ")
                    list_course = []
                    isExist = False
                    seperator = ", "
                    for i in information.keys():
                        if len(i) > 6:
                            if information[i]['subject'] == course_name:
                                list_course.append(information[i]['barcode'])
                    if len(list_course) == 0:
                        isExist = False
                        done = True
                    else:
                        isExist = True
                    if isExist:
                        print("Our free teachers: %s" % seperator.join(list_course))
                        barcode = str(input("Input the barcode of new Teacher: "))

                        course[course_name]['teacher'] = {
                            "fullName": information[barcode]["fullName"],
                                    "login": information[barcode]["login"],
                                    "barcode": information[barcode]["barcode"]
                        }
                        with open("course.json", 'w') as courseWF:
                            json.dump(course, courseWF, indent=2)
                        print("Done")
                        done = True
                else:
                    pprint(course[course_name])
                    barcode = str(input("Input the barcode of Teacher: "))
                    list_course = []
                    isExist = False

                    for i in information.keys():
                        if len(i) > 6:
                            if information[i]['subject'] == information[barcode]['subject']:
                                if information[i] != information[barcode]:
                                    list_course.append(information[i]["barcode"])
                    if len(list_course) == 0:
                        isExist = False
                        done = True
                    else:
                        isExist = True
                    if isExist:
                        pprint("This is our " +course_name+" teachers : %s" % seperator.join(list_course))
                        forWhat = str(input("barcode of new Teacher: "))
                        course[course_name]['teacher'] = {
                                    "fullName": information[forWhat]["fullName"],
                                    "login": information[forWhat]["login"],
                                    "barcode": information[forWhat]["barcode"]
                                    }
                        with open("course.json", 'w') as courseWF:
                            json.dump(course, courseWF, indent=2)
                        print("Done")
                        done = True
            elif option == 2:
                groups = dict(json.load(open("groups.json")))

                group_names = list(groups.keys())

                currect_groups_of_course = []

                for i in course[course_name]["groups"].keys():
                   currect_groups_of_course.append(i)
                print(seperator.join(currect_groups_of_course))
                current = str(input("Please input the name of group that you want change: "))
                group_names.remove(current)
                print("Exist groups: %s"%seperator.join(group_names))

                forWhat = str(input("For what you want change: "))
                del course[course_name]["groups"][current]
                course[course_name]["groups"][forWhat] = groups[forWhat]
                with open('course.json', 'w') as courseWF:
                    json.dump(course, courseWF, indent=2)
                print("Done")
                done = True
            else:
                done = True



def show(role):
    if role == 'student':
        information = dict(json.load(open("information.json")))

        students = dict()

        for i in information.keys():
            if len(i)==6:
                students[i] = information[i]

        return students
    elif role == 'teacher':
        information = dict(json.load(open("information.json")))

        teachers = dict()

        for i in information.keys():
            if len(i) > 6:
                teachers[i] = information[i]
        return teachers
    elif role == 'course':
        course = dict(json.load(open("course.json")))

        return course

def groupping(new_student):

    groups = dict(json.load(open("groups.json")))

    isExist = False

    if new_student.group in groups.keys():
        isExist = True

    if isExist:
        groups[new_student.group][f"{new_student.getBarcode()}"] = {"fullName": new_student.getFullName(), "login": new_student.getLogin()}
        with open("groups.json", 'w') as groupsWF:
            json.dump(groups, groupsWF, indent=2)
    else:
        groups[new_student.group] = {
            f"{new_student.getBarcode()}": {"fullName": new_student.getFullName(), "login": new_student.getLogin()}}

        with open("groups.json", 'w') as groupsWF:
            json.dump(groups, groupsWF, indent=2)

def teacherTool(login):
    done = False

    course = dict(json.load(open("course.json")))

    information = dict(json.load(open("information.json")))
    isLead = False
    while done==False:
        print("1. See subject that you lead")
        print("2. Start a lesson")
        print("0. Exit")
        option = int(input("Choose the option: "))

        if option == 1:
            if information[login[:-16]]['barcode'] == course[information[login[:-16]]['subject']]["teacher"]['barcode']:
                isLead = True
            print(information[login[:-16]]['subject'])
            continue

        if option == 2:
            if information[login[:-16]]['barcode'] == course[information[login[:-16]]['subject']]["teacher"]['barcode']:
                isLead = True
            if isLead:
                print("Which group will have a lesson today?")
                seperator = ", "
                print(seperator.join(course[information[login[:-16]]['subject']]['groups'].keys()))
                group_name = str(input("Group name: "))
                current_lesson = dict(json.load(open("current_lesson.json")))
                grades_file = dict(json.load(open("grades.json")))

                grades_file[information[login[:-16]]['subject']] = course[information[login[:-16]]['subject']]["groups"][group_name]

                current_lesson = course[information[login[:-16]]['subject']]["groups"][group_name]
                students = list(course[information[login[:-16]]['subject']]["groups"][group_name])
                with open("current_lesson.json", 'w') as current_lessonWF:
                    json.dump(current_lesson, current_lessonWF, indent=2)

                if group_name in course[information[login[:-16]]['subject']]['groups'].keys():
                    work_end = False
                    while work_end== False:
                        if bool(current_lesson) == True:
                            print("1. Mark Student")
                            print("2. Rate student")
                            print("0. Finish the lesson")
                            option = int(input("Choose the option: "))

                            if option==1:
                                print(seperator.join(current_lesson.keys()))
                                isExist = str()

                                for i in students:
                                    if "attendance" not in grades_file[information[login[:-16]]['subject']][i].keys():
                                        print("Present? %s"%i)
                                        isExist = input("yes or no: ")
                                        if isExist.lower() == "no":
                                            attendance = list()
                                            attendance.append("absent")
                                            grades_file[information[login[:-16]]['subject']][i]["attendance"] = attendance
                                            del current_lesson[i]
                                        else:
                                            attendance = list()
                                            attendance.append("present")
                                            grades_file[information[login[:-16]]['subject']][i]["attendance"] = attendance
                                            continue
                                    else:
                                        print("Present? %s" % i)
                                        isExist = input("yes or no: ")
                                        if isExist.lower() == "no":
                                            attendance = grades_file[information[login[:-16]]['subject']][i]["attendance"]
                                            attendance.append("absent")
                                            [information[login[:-16]]['subject']][i]["attendance"] = attendance
                                            del current_lesson[i]
                                        else:
                                            attendance = grades_file[information[login[:-16]]['subject']][i]["attendance"]
                                            attendance.append("present")
                                            grades_file[information[login[:-16]]['subject']][i][
                                                "attendance"] = attendance
                                            continue

                                with open("grades.json", 'w') as gradesWF:
                                    json.dump(grades_file, gradesWF, indent=2)
                                with open("current_lesson.json", 'w') as current_lessonWF:
                                    json.dump(current_lesson, current_lessonWF, indent=2)
                                continue
                            if option == 2:

                                print(seperator.join(current_lesson.keys()))

                                for i in current_lesson.keys():
                                    if "grades" not in grades_file[information[login[:-16]]['subject']][i].keys():
                                        print("Rate the student from 0 to 10 %s" % i)
                                        grade = input("Grade: ")
                                        if "grades" not in course[information[login[:-16]]['subject']]["groups"][group_name][i].keys():
                                            grades = list()
                                            grades.append(grade)
                                            course[information[login[:-16]]['subject']]["groups"][group_name][i]["grades"] = grades

                                            grades_file[information[login[:-16]]['subject']][i]["grades"] = grades

                                        else:
                                            grades = list(course[information[login[:-16]]['subject']]["groups"][group_name][i]["grades"])
                                            grades.append(grade)
                                            course[information[login[:-16]]['subject']]["groups"][group_name][i]["grades"] = grades

                                            grades_file[information[login[:-16]]['subject']][i]["grades"] = grades
                                    else:
                                        print("Rate the student from 0 to 10 %s" % i)
                                        grade = input("Grade: ")
                                        if "grades" not in course[information[login[:-16]]['subject']]["groups"][group_name][i].keys():
                                            grades = list()
                                            grades.append(grade)
                                            course[information[login[:-16]]['subject']]["groups"][group_name][i]["grades"] = grades
                                            grades = list(grades_file[information[login[:-16]]['subject']][i]["grades"])
                                            grades.append(grade)
                                            grades_file[information[login[:-16]]['subject']][i]["grades"] = grades

                                        else:
                                            grades = list(course[information[login[:-16]]['subject']]["groups"][group_name][i]["grades"])
                                            grades.append(grade)
                                            course[information[login[:-16]]['subject']]["groups"][group_name][i]["grades"] = grades

                                            grades = list(grades_file[information[login[:-16]]['subject']][i]["grades"])
                                            grades.append(grade)
                                            grades_file[information[login[:-16]]['subject']][i]["grades"] = grades


                                with open("grades.json", 'w') as gradesWF:
                                    json.dump(grades_file, gradesWF, indent=2)
                                with open("current_lesson.json", 'w') as current_lessonWF:
                                    json.dump(current_lesson, current_lessonWF, indent=2)

                            else:
                                current_lesson = {}
                                with open("current_lesson.json", 'w') as current_lessonWF:
                                    json.dump(current_lesson, current_lessonWF, indent=2)
                                work_end = True
                        else:
                            print("Today all the students absent in class")
                            print("\n")

                            work_end = True
                else:
                    print("Not correct input")

            else:
                print("I'm sorry, but you're not teaching in the course yet")
        else:
            done = True

def studentTool(login):
    done = False

    course = dict(json.load(open("course.json")))

    information = dict(json.load(open("information.json")))

    grades = dict(json.load(open("grades.json")))

    seperator = ", "

    while done == False:
        print("1. See course")
        print("2. Rate the teacher")
        print("0. Exit")
        option = int(input("Choose option: "))
        if option==1:
            print(seperator.join(course.keys()))
            course_name = str(input("Course name: "))
            if course_name in grades.keys():
                if login[:6] in grades[course_name].keys():
                    end = False
                    while end == False:
                        print("1. See grades: ")
                        print("2. See groupmates: ")
                        print("3. See attendance")
                        print("0. back")
                        option = int(input("Choose option: "))
                        if option == 1:
                            if "grades" in grades[course_name][login[:6]].keys():
                                print(seperator.join(grades[course_name][login[:6]]['grades']))
                            else:
                                print("sorry you have not graded yet")
                        elif option == 2:
                            pprint(grades[course_name])
                        elif option == 3:
                            print(seperator.join(grades[course_name][login[:6]]['attendance']))
                        else:
                            end = True
                else:
                    print("123213That course not beggin or just your group not enrolled to course")
            else:
                print("That course not beggin or just your group not enrolled to course")
        elif option == 2:
            teachers = []

            for i in information.keys():
                if len(i)>6:
                    teachers.append(i)

            print(seperator.join(teachers))
            barcode = str(input("Barcode of teacher: "))
            rate = dict(json.load(open("rateTeacher.json")))
            if barcode in information.keys():
                rate[barcode] = dict(information[barcode])
                some_word = str(input("Please write a few words about the teacher how she/he conducted the lesson? "))
                rate[barcode]["rate"] = some_word
                with open("rateTeacher.json", 'w') as rateTeacherWF:
                    json.dump(rate, rateTeacherWF, indent=2)
            else:
                print("Not correct input")
        else:
            done=True