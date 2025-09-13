'''
Challenge 1 : Build A Calculator

Deadline: 2 days from today

It must run  only in the main function.

1.) Take 2 inputs
2.) It will output the sum
3.) It will output the difference 
4.) It will output the product
5.) It will output the difference 
6.) It will output the square 
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

main()

