marks = {
    "Harry" : 100, 
    "Shubham" : 56,
    "Rohan" : 23
}

print(marks.items()) #prints out the main items in tuples form
print(marks.keys()) #prints the keys, such as harry, rohan
print(marks.values()) #prints out the values, such as 100

marks.update({"Harry" : 99, "Renuka" : 100}) #Updated the marks and also adds if not already in there
print(marks.get("Harry"))
