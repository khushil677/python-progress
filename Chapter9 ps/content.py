f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("Twinkle present in content")
else: 
    print("Twinkle not present in content")

f.close()