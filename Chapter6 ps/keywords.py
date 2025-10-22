#detects scam comments
word1 = "Make a lot of money"
word2 = "buy now"
word3 = "subscribe this"
word4 = "click this"

comment = input("Enter your comment: ")

if ((word1 in comment) or (word2 in comment) or (word3 in comment) or (word4 in comment)):
    print("This is a scam comment")

else:
    print("This comment is not a scam")