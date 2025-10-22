marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))


#total percentage
total_marks = (marks1 + marks2 + marks3) / 3

if (total_marks >= 40):
    print("Pass: ", total_marks)

else: 
    print("fail: ", total_marks)

