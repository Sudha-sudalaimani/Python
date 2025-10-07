class Book():
    def __init__(self,t,a,p):
        self.title=t
        self.author=a
        self.price=p
    def displaydetails(self):
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"Price:{self.price}")
Book1=Book("Atomic Habits","Unknown",200.0)
Book1.displaydetails()
