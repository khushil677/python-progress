# Changing self to something else to check what happens

from random import randint

class Train:

    def __init__(khushil, trainNo):
        khushil.trainNo = trainNo

    def book(khushil, fro, to):
        print(f"Ticket is booked in train no: {khushil.trainNo} from {fro} to {to}")

    def getStatus(khushil, trainNo, fro, to):
        print(f"Train {khushil.trainNo} from {fro} to {to} is running succesfully!")

    def getFare(khushil, trainNo, fro, to):
        print(f"Ticket is booked in train no: {khushil.trainNo} from {fro} to {to} is {randint(250, 4000)}") 

    
t = Train(2332)
t.book("Eldoret", "Nairobi")
t.getStatus(2322, "Eldoret", "Nairobi")
t.getFare(2322, "Eldoret", "Nairobi")


# It works the same way, but it is not a good practice, why would i keep my name or some other random word instead of self