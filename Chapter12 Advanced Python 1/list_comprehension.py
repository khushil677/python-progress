myList = [1, 2, 3, 4, 5, 6]


# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

# The above code can be written in few lines by list comprehension

squaredList = [i*i for i in myList]

print(squaredList)

# Output: [1, 4, 9, 16, 25, 36]