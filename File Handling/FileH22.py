# Read the contents of two text files and create a third file containing the contents of both files.

f1 = open("FileH1.py", "r")
data1 = f1.read()
f1.close()

f2 = open("FileH2.py", "r")
data2 = f2.read()
f2.close()

f3 = open("Filemerge.py", "w")
f3.write(data1 + "\n" + data2)
f3.close()

print("Files merged successfully")
