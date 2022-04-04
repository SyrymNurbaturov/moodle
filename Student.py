class New_Student:
    __fullName = str()
    __age = int()
    __gender = bool()
    grades = []
    __login = str()
    __password = str()
    group = str()
    __barcode = int()

    def __init__(self, name, surname, age, isMale, login, password, group, barcode):
        self.__fullName = name + " " + surname
        self.__age = age
        self.__gender = isMale
        self.__login = login
        self.__password = password
        self.group = group
        self.__barcode = barcode

    def getBarcode(self):
        return self.__barcode

    def getLogin(self):
        return self.__login

    def getPassword(self):
        return self.__password

    def getFullName(self):
        return self.__fullName

    def setFullName(self, name, surname):
        self.__fullName = name + " " + surname

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def getGender(self):
        return self.__gender

    def setGender(self, gender):
        self.__gender = gender

    def getGrades(self):
        return self.grades

    def setGrades(self, index, forWhat):
        self.grades[index] = forWhat

    def toString(self):
        return "\t"+"Name: " + self.__fullName +'\n'+ "\t"+"Age: " + self.__age +"\n"+"\t"+"Gender: "+ self.__gender+ "\n" +"\t" "Grades: " + self.grades

