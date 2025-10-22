a = (1, 45, 45, 67, 89, False, "Rohan", "Achyutam")
print(a)

no = a.count(45) #BECAUSE tuples are immutable, count method will tell us how many times 45 appears in the tuple
print(no)

ind = a.index(67) #tells us the index of the number
print(ind)