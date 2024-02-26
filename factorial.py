'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def factorial(a):
    if(a<=1):
        return 1
    else:
        return a*factorial(a-1)
a=int(input("Positive num: "))
print("fac of %d is %d"%(a,factorial(a)))