#Write a short PYTHON program to check weather the 
#square root of number is prime or  not.

import math

n = int(input("Enter a number: "))

root = int(math.sqrt(n))

if root * root == n:
    if root < 2:
        print("Square root is not prime")
    else:
        prime = True
        for i in range(2, int(math.sqrt(root)) + 1):
            if root % i == 0:
                prime = False
                break

        if prime:
            print("Square root is prime")
        else:
            print("Square root is not prime")
else:
    print("The number is not a perfect square")
