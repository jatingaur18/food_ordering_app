from csv import writer
from csv import reader
class admin:
    def __init__(self):
        self.__name="name"
        self.__username="un"
        self.__password="pass"
    
    def setter(self,n,un,p):
        self.__name=n
        self.__usename=un
        self.__password=p 
        
    def addstaff(self,n,un,pas):
        b=False
        st=[n,un,pas]
        with open('dataset\staff1.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(st)
            f_object.close()
            b=True
        return b
        
    def adddish(self,d,p):
        b=False
        nd=[d,p]
        with open('dataset\dish1.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(nd)
            f_object.close()
            b=True
        return b
    
    def adminlogin(self,un,pas):
        b=False
        with open('dataset\staff1.csv', mode ='r')as file:
            csvFile = reader(file)
            for lines in csvFile:
                if(lines[1]==un and lines[2]==pas):
                    self.setter(self,lines[0],lines[1],lines[2])
                    b=True
                    break
        return b
# commits

class user:
    def init__(self):
        self.name="name"
        self.password="pass"
        self.username="un"
        self.email="email"
    
    def setter(self,n,p,un,e):
        self.name=n
        self.password=p
        self.username=un
        self.email=e
        
    def signup(self,n,e,un,p):
        b=False
        self.setter(self,n,p,un,e)
        nu=[self.name,self.password,self.username,self.email]
        with open('dataset\\user1.csv', 'a', newline='') as u_object:
            writer_object = writer(u_object)
            writer_object.writerow(nu)
            u_object.close()
            b=True
        return b
    def login(self,un,pas):
        a=False
        with open('dataset\\user1.csv', mode ='r')as file:
            csvFile = reader(file)
            for lines in csvFile:
                if(lines[2]==un and lines[1]==pas):
                    self.setter(self,lines[0],lines[1],lines[2],lines[3])
                    a=True
                    break
        return a
    
    def order(self,arr,price):
        arr.append(self.name)
        with open('dataset\\order.csv', 'a', newline='') as u_object:
            writer_object = writer(u_object)
            writer_object.writerow(arr)
            u_object.close()
            b=True
        return b

                
class payment:
    pass

class cash(payment):
    def makepay():
       pass

class card(payment):
    def makepay():
        pass

class creditcard(card):
    def makepay():
        pass

class debitcard(card):
    def makepay():
        pass

u=user
a=admin

def useersignup(n,e,un,p):
    return u.signup(u,n,e,un,p)

def loginuser(us,pas):
    return u.login(u,us,pas)

def adminuser(us,pas):
    return a.adminlogin(a,us,pas)

def adminadding(n,un,pas):
    return a.addstaff(a,n,un,pas)

def addingdish(d,p):
    return a.adddish(a,d,p)

def addorder(arr,price):
    return u.order(u,arr,price)