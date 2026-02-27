import json

data= {
    "name": "Vishal Rawat",
    "age": 23,
    "skills": [".netCore","Angular"]
}

with open("file.txt", "w") as file:
    json.dump(data, file, indent=4)

with open("file.txt", "r") as file:
    content = json.load(file)

print(content)
print("dfdfd")