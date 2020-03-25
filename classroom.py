class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def getFirstname(self):
        return self.firstname
    def getLastname(self):
        return self.lastname
    def __str__(self):
        return "%s %s" %(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, firstname, lastname, subjectArea):
        Person.__init__(self, firstname, lastname)
        self.subjectArea = subjectArea
    def printNameSubject(self):
        return "%s %s, %s" %(self.firstname, self.lastname, self.subjectArea)

class Teacher(Person):
    def __init__(self, firstname, lastname, courseName):
        Person.__init__(self, firstname, lastname)
        self.courseName = courseName
    def printNameCourse(self):
        return "%s %s, %s" %(self.firstname, self.lastname, self.courseName)
