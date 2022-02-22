#program to change the global variable inside a function
a=10 #global varibale

def inside_func():
    global a
    a=20 + 10  #changing the global varibale inside a function
    print("the variable inside a function is:",a)

inside_func()

print("The global variable is:",a)