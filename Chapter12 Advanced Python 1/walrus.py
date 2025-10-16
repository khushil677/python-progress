#Using basic Python
n = [1, 2, 3, 4, 5]

if (len(n) > 3):
     print(f"List is too long ({len(n)} elements expected <= 3)") #Output: List is too long (5 elements, expected <= 3)


#Using Walrus Operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements expected <= 3)") #Output: List is too long (5 elements, expected <= 3)