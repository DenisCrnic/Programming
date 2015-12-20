class Family:

    def __init__(self, family_name, list_of_members):
        self.family_name = family_name
        self.list_of_members = list_of_members


    def addFamilyMember(self, other):
        self.list_of_members.update({other.name : other})


    def removeFamilyMember(self, name):
        del self.list_of_members[name]


    def __str__(self):
        temp = ''
        for i in self.list_of_members:
            temp += str(self.list_of_members[i]) + '\n'
        return temp
