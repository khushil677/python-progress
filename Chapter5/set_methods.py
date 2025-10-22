s = {1, 5, 32, 54, 5 ,5 ,5}
s.add(540)
print(s) #{32, 1, 5, 54, 540}

s.remove(5) #removes 5 from the set
s.clear() #empties the set
s.len() #returns the length of the set


s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 5, 7, 10}

print(s1.union(s2)) #prints the values, but without repeating a certain value
print(s1.intersection(s2)) #prints none repeated values only