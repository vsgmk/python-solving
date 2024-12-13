class Fathername():
    def __init__(self,father):
        pass
    def fathername(self, father):
        print(father)

class Mothername(Fathername):
    def __init__(self):
        pass
    def mothername(self, mother, father):
        print(mother)
        self.fathername(father)

class Child1(Mothername,Fathername):
    def __init__(self,mother,father,name):
        self.name=name
        self.mother=mother
        self.father=father

    def completename1(self):
        print(self.name)
        self.mothername(self.mother, self.father)
        
class Child2(Mothername,Fathername):
    def __init__(self,mother,father,name):
        self.name=name
        self.mother=mother
        self.father=father

    def completename2(self):
        print(self.name)
        self.mothername(self.mother, self.father)

obj1=Child1("Sangita","Dipak","Vaibhav")
obj2=Child2("Sangita","Dipak","Gaurav")
obj1.completename1()
obj2.completename2()