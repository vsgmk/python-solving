class Parent():
    def __init__(self):
        pass
    def Parent_name(self, parent):
        print("parent name is",parent)

class stud1(Parent):
    def __init__(self,name,parent):
        self.name=name
        self.parent=parent
    def stud1name(self):
        print("name is :",self.name)
        self.Parent_name(self.parent)

class stud2(Parent):
    def __init__(self,name,parent):
        self.name=name
        self.parent=parent
    def stud2name(self):
        print("name is :",self.name)
        self.Parent_name(self.parent)

obj1=stud1("vaibhav","dipak")
obj2=stud2("ranjit","netaji")
obj1.stud1name()
obj2.stud2name()