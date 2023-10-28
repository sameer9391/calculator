print("                           SIMPLE CALCULATOR                                   ")
print("                                      +.Addition\n")
print("                                      -.Substraction\n")
print("                                      *.Multiplication\n")
print("                                      /.Divison\n ")
print("                                      %.Modulus")
n1=int(input("Enter First Number\n"))
n2=int(input("Enter Second Number\n"))
s=input("Enter your Operation Choice you want\n")
if s=='+':
    print(n1+n2)
elif s=='-':
    print(n1-n2)
elif s=='*':
    print(n1*n2)
elif s=='/':
    print(n1/n2)
elif s=='%':
    print(n1%n2)
else:
    print("Invalid operator is given")

