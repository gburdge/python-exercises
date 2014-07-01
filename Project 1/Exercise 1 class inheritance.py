class Person(object):   # base class
    """
    Base class for all other persons
    """
    def __init__(self, name, age, school):
        self.name=name
        self.age=age
        self.school=school

class Student(Person):
    def talk(self):
        print "My name is %s. I am %s years old. I am studying at %s School." % (self.name, self.age, self.school)

class Teacher(Person):
    def talk(self):
        print "My name is %s. I am %s years old. I am teaching at %s School." % (self.name, self.age, self.school)

peter = Student("Peter", "9", "ABC Primary")
peter.talk()
john = Teacher("John", "23", "ABC Primary")
john.talk()

# i have a name - description
# i have an age
# i have a school
#
# i am a student - differences
# i am a teacher



