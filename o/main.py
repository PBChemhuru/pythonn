f = open("nice.text2", "a")
f.write("booom shakkalaka")
f.close()
f= open("nice.text2", "w")
f.write("are you really")
f = open("nice.text2", "r")
print(f.read())

