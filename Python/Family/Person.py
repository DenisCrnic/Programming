class Person:

    def __init__(self, name, age, height, gender):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender


    def __str__(self):
        temp = 'Name: ' + self.name + '\nAge: ' + str(self.age)\
                + '\nHeight: ' + str(self.height) + '\nGender: '\
                + self.gender + '\n'
        return temp
