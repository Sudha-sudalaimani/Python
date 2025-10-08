class movie():
    def __init__(self,m,r):
        self.moviename=m
        self.rating=r
    def isHit(self):
        print("Movie Name:",self.moviename)
        if(self.rating>7):
            print("Movie is hit")
        else:
            print("Movie is flop")
m1=movie("Kandukonden Kandukonden",10)
m1.isHit()
