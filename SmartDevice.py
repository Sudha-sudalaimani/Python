class SmartDevice:
    def __init__(self,b,m,bl):
        self.brand=b
        self.model=m
        self.batteryLevel=bl
    def useapp(self,app_name):
       if self.batteryLevel<=10:
           print(f"Battery Drain Please Put Charge ! : {self.batteryLevel}")
       else:
            self.batteryLevel-=5
            print(f"User using {app_name}")
            print(f"Battery Level: {self.batteryLevel}")
    def charge(self):
        self.batteryLevel=100
        print(f"{self.batteryLevel} : Battery Full !")

s1=SmartDevice("Realme","12x",7)
s1.useapp("Whatsapp")


    
