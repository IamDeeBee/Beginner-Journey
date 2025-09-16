'''
Challenge 1 : Build A Calculator

Deadline: 2 days from today

It must run  only in the main function.

1.) Take 2 inputs
2.) It will output the sum
3.) It will output the difference 
4.) It will output the product
5.) It will output the square 
'''
import math

def main():
   x = int(input("Enter first number :"))
   y = int(input("Enter second number:"))

   print("\n") 
   '''
   print("First number is ", x)
   print("Second number is ", y,"\n")
   '''
   print("The sum is ", x+y)
   print("The difference is ", x-y)
   print("The product is ", x*y)
   print("The square of x is ", x*x)
   print("The square of y is ", y*y)
'''
This is called a main guard
It is a best practice while coding in Python
Reasons:
1.)Removes surprises : code doesn’t auto-run when the file is imported elsewhere.
2.)Keeps Code reusable → the same file can act as a library (functions you import) and a program (things you run).
3.)Testing friendly → tools like pytest can import your file without triggering the whole program.
4.)Scales well → once projects get bigger than one file, you need this guard.
'''
if __name__ == "__main__":
   main()

