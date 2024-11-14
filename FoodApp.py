from Models.User import User

class LoginSystem:
    
    def Login(self):
        pass

    def Register(self):
        
        Name = input("Name : ")
        MobileNo. = int(input("Mobile No : "))
        MailId = input("Email Id : ")
        Password  = input("Password : ")

    
    def GuestLogin(self):
        pass

    def ValidateOption(self,option):

        if option == 1:
            self.Login()
        elif option == 2:
            self.Register()
        elif option == 3:
            self.GuestLogin()
        elif option == 4:
            self.Exit()
        else:
            print("Invalid Choice...")






class FoodApp:

    LoginOptions = {1:"Login",2:"Register",3:"Guest",4:"Exit"}

    @staticmethod
    def Init():
        print("Welcome to the Online Food Ordering")

        loginsystem = LoginSystem()

        for option in FoodApp.LoginOptions:
            print(f"{option}.{FoodApp.LoginOptions[option]}", end = " ")
        
        print() 

        choice = int(input("Please Enter your choice: "))
        loginsystem.ValidateOption(choice)
        