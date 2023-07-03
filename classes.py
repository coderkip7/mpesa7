class magari:
    def __init__(self,modelname,color,year,price,brand):
        self.model=modelname
        self.mycolor=color
        self.myyear=year
        self.myprice=price
        self.mybrand=brand
    def onyesha(self):
        print(self.model,self.mycolor,self.myyear,self.myprice,self.mybrand)
    #create an object
myobj=magari("Rolls-Royce","Gold",2020,"2.5 MILLION USD","cullinan")
myobj.onyesha()