#Create a Student class with rollNo, name, and marks. Write a method to display student details.
class Student():
    def __init__(self,r,n,m):
        self.rollno=r
        self.name=n
        self.marks=m
    def display(self):
        print(f"Roll.No: {self.rollno}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
s1=Student(101,"Sam",585)
s1.display()
