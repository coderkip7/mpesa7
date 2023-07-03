#name,gender,age
class People:
    def __init__(self,name,gender,age):
        self.myname=name
        self.mygender=gender
        self.myage=age
    def show(self):
        print(self.myname,self.mygender,self.myage)
myobj=People("Dennis","Male",22)
myobj2=People("Tasha","Female",25)
myobj3=People("Mount","Male",24)
myobj.show()
myobj2.show()
myobj3.show()

