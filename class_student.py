class student:
    def __init__(self):
        name=""
        regno=0
    def display(self):
        print("Name:",self.name)
        print("Regno:",self.regno)
obj=student()
obj.name="Sam"
obj.regno=101
obj.display()
