#!cd/usr/bin/python
#version3
#Program::Python as a calculator using Functions
#Author::Sweeti Chauhan

def add(a,b):
	print('{} + {}= ' .format(a, b))
	print(a+b)

def sub(a,b):
	print('{} - {}= ' .format(a, b))
	print(a-b)

def mul(a,b):
	print('{} * {}= ' .format(a, b))
	print(a*b)

def div(a,b):
	print('{} / {}= ' .format(a, b))
	print(a/b)

def calculate():
	ch = input ('''
Please select an operator::
+ for Addition
- for Subtraction
* for Multiply
\ for Division
''')
	a = int(input("Enter a number::"))
	b = int(input("enter another number::"))
	if (ch == '+'):
		add(a,b)
	elif (ch == '-'):
		sub(a,b)
	elif (ch == '*'):
		mul(a,b)
	elif (ch == '/'):
		div(a,b)
	else:
		print("Invalid choice. Please enter valid choice")
	again()


def again():
	ag = input('''
Do you want to calculate again:::
Type Y for yes N for no
''') 
	#Accept y or Y and  n or N as input using .upper()
	if(ag.upper() == 'Y'):
		calculate()
	elif(ag.upper() == 'N'):
		print("See you later")
	else:
		again()


def welcome():
	print("Welcome to Calculator")
#call calculate function outside the def
welcome()
calculate()

