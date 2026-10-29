#Read a Python source file and create another file after removing single-line comments.

f = open("FileH1.py", "r")
lines = f.readlines()
f.close()

f = open("output.py", "w")

for line in lines:
    if not line.lstrip().startswith("#"):
        f.write(line)

f.close()
print("Comments removed")
