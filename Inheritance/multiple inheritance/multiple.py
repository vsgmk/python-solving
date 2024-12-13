# # multiple inheritance

# class Register():
#     def __init__(self,username,userid):
#         self.username=username
#         self.userid=userid
#     def Register():
#         if(username!=userid):
#             print("username could not exist register first")
# class Login():
#     def __init__(self,username,password):
#         self.username=username
#         self.password=password
#     def Login():
#         if(user_password==password and userid==username):
#             print("welcome in website")
#         elif(username== userid and user_password!=password):
#             print("wrong password! try again.")

# class user(Login,Register):
#     def __init__(self,username,password):
#         self.username=username
#         self.password=password
#     def Isuser():
#         userid=input("enter the username")
#         user_password=input("Enter the password : ")

# username="vaibhav"
# password="abcd"
# obj=user(username,password)
# obj.Isuser()
# obj.Login(username,password)
# obj.Register(username)

class Mother():
    def Mothername(self):
        print("Mother name is Sangita")

class Father():
    def Fathername(self):
        print("Father name is Dipak")

class son(Mother,Father):
    def name(self):
        print("my name is Vaibhav")

obj=son()
obj.name()
obj.Fathername()
obj.Mothername()