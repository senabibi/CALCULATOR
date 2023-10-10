
from art import logo
#Calculator
#ADD 
def add(num1,num2):
    return num1+num2
#SUBSTRACT
def substact(num1,num2):
    return num1-num2
#MULTIPLY
def multiply(num1,num2):
    return num1*num2
#DIVIDE
def divide(num1,num2):
    return num1/num2
#Dictionary
operations={
    "+":add,
    "-":substact,
    "*":multiply,
    "/":divide,
} 
is_ok=True
while is_ok:
    print(logo) 
    num1=float(input("What is the first number?"))
    num2=float(input("What is the secons number?"))
    for symbol in operations:
        print(symbol)
    chosen_operation=input("Pick an operation from the line above:")
    calculation_function=operations[chosen_operation]
    answer=calculation_function(num1,num2)
    print(f"The {num1} {chosen_operation} {num2}= {answer}")
    ll_continue=input("Will you wanna continue?('y' for yes and 'n' for no)")
    if ll_continue=="n":
        is_ok=False

