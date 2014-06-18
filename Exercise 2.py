class Employee(object):
     #init constructor below
    def __init__(self, name, age, title, salary):
        self.name = name
        self.age = age
        self.job = Job(title, salary)

    def talk(self):
        print "My name is %s. I am %s years old. I am a %s. I earn $%s per year!" % (self.name, self.age, self.job.title,
                                                                             self.job.salary)


class Job():
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary
morgan_williams = Employee('Morgan Williams', '24', 'Software Developer', '1000000')
morgan_williams.talk()

# i have a name = Morgan Williams'
# i have an age = 24
# i have a job title = Software Developer
