class student:
    def info(self):
        rollno = int(input("Enter your rollno ==> "))
        name = input("Enter your name ==> ")

class exam(student):
    def examinfo(self):
        print("Selection your Semester Exam ...")

class CIA1(exam):
    def cia1(self):
        Python = int(input("Enter your Python marks ==> "))
        Java = int(input("Enter your Java marks ==> "))     
        cia1 = Python + Java

class CIA2(exam):
    def cia2(self):
        Python = int(input("Enter your Python marks ==> "))
        Java = int(input("Enter your Java marks ==> "))   
        cia2 = Python + Java

class SEE(exam):
    def see(self):
        Python = int(input("Enter your Python marks ==> "))
        Java = int(input("Enter your Java marks ==> "))   
        see = Python + Java

class result(student):
    def Result(self):
        print("rollno = ",rollno)
        print("name = ",name)
        

r1 = result()
r1.Result()


        
