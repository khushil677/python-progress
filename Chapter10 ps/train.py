from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self, trainNo, fro, to):
        print(f"Train {self.trainNo} from {fro} to {to} is running succesfully!")

    def getFare(self, trainNo, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to} is {randint(250, 4000)}") 

    
t = Train(2332)
t.book("Eldoret", "Nairobi")
t.getStatus(2322, "Eldoret", "Nairobi")
t.getFare(2322, "Eldoret", "Nairobi")


