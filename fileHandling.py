with open("file.txt","w") as file:
    file.write("Hello vishal\n")
    file.write("How are you? Are you learnig fileHandiling\n")

with open("file.txt", "r") as file:
    content = file.read()
    print(content)

with open("file.txt", "a") as file:
    file.write("And where are you from vishal rawat")

with open("file.txt", "r") as file:
    content = file.read()
    print(content)

with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())