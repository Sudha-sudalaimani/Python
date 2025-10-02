#Classes and object
class goa:
    name=""
    drink=""
    def party(self):
        print("Lets party")
    def beach(self):
        print("Enjoying the beach")
ramesh=goa()
suresh=goa()
ramesh.name="Ramesh"
suresh.name="Suresh"
ramesh.drink="Yes"
suresh.drink="No"
ramesh.party()
suresh.beach()
print(ramesh.name)
print(ramesh.drink)
print(suresh.name)
print(suresh.drink)
