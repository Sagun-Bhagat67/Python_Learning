'''
Write a Class ‘Train’ which has methods to book a ticket, get status (running or not) 
and get fare information of train running under Indian Railways. 
'''
import random
class Train:
    
    def __init__(self,trainNo):
        self.trainNo =trainNo
        
    def book(self, fro, to):
        print(f"Your ticket for train No: {self.trainNo} from {fro} to {to} is Booked..")

    
    def getFare(self,fro,to):
        print(f"Your ticket Fare for train No: {self.trainNo} from {fro} to {to} is Rs.{random.randint(1,10000)}/-")
    
    def getStatus(self):
        print(f"Your ticket for train No: {self.trainNo} from is running Successfully..")
        
t = Train(6969)

t.book("KTM",'Dehli')
t.getStatus()
t.getFare('KTM','Dehli')