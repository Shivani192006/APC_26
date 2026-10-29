#Write a program to compare two text files and display whether their contents are 
#identical. If different, identify the first line where they differ.

f1 = open("FileH1.py", "r")
lines1 = f1.readlines()
f1.close()

f2 = open("FileH2.py", "r")
lines2 = f2.readlines()
f2.close()

if lines1 == lines2:
    print("Files are identical")
else:
    print("Files are different")

    for i in range(max(len(lines1), len(lines2))):
        line1 = lines1[i] if i < len(lines1) else "No line"
        line2 = lines2[i] if i < len(lines2) else "No line"

        if line1 != line2:
            print("First difference at line", i + 1)
            print("File 1:", line1.strip())
            print("File 2:", line2.strip())
            break
