class student :
  def __init__(self,age,marks) :
    self.age=age
    self.marks=marks

  def validate(self) :
    if self.age<=20 :
      print("Your age is not valid to apply for this university.")
      return
    while True :
      if(self.marks<0 or self.marks>100) : 
        self.marks=int(input("Sorry ..! Enter valid marks : "))
      else : 
        break


  def print_message(self):
    if self.age>20 and self.marks>=65 :
      print("this student is eligible for admission in this university .")
    else : print("your details don't meat threshold required for admission in this university.")


age=int(input("Enter the age : "))
marks=int(input("Enter the marks : "))
stu = student(age,marks)
stu.validate()
stu.print_message()
print("************************************************")
print("************************************************")
age=int(input("Enter the age : "))
marks=int(input("Enter the marks : "))
stu = student(age,marks)
stu.validate()
stu.print_message()
print("************************************************")
print("************************************************")
age=int(input("Enter the age : "))
marks=int(input("Enter the marks : "))
stu = student(age,marks)
stu.validate()
stu.print_message()
