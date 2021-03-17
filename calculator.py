from tkinter import *
import parser
import math
import re

root = Tk()
root.title('Calculator')
 
#get the user input and place it in the textfield
i = 0
i = 0
def get_variables(num):
    entire_string = display.get()
    if entire_string == 'Error':
        clear_all()
    global i
    display.insert(i,num)
    i+=1
 
def calculate():
    global i
    entire_string = display.get()
    entire_string = clean_factorials(entire_string)
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        if type(result) == float:  # if result has a decimal which is 0, this removes the decimal
            if result.is_integer():
                result = int(result)
        length_result = len(str(result))
        clear_all()
        display.insert(0,result)
        i = length_result
    except Exception:
        clear_all()
        display.insert(0,"Error")
        i = 0

# method to replace the number followed by ! by the factorial on the number
# method replaces the new number in the original string and returns the updated string
def clean_factorials(s):
    factorial_find = re.finditer(r"[.]?\d+[!]",s)
    for i in factorial_find:
        value = i[0]
        new_value = value[:-1]
        if new_value.isdigit():
            new_value = str(math.factorial(int(new_value)))
            s = s.replace(value,new_value)

    return s
 
def get_operation(operator):
    entire_string = display.get()
    if entire_string == 'Error':
        clear_all()
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length
 
def clear_all():
    global i
    display.delete(0,END)
    i = 0
 
def undo():
    global i
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
        i = len(entire_string) - 1
    else:
        clear_all()
        display.insert(0,"Error")
        i = 0

 
#adding the input field
display = Entry(root, bg = 'medium sea green', bd = 10, font=("Arial", 18, "bold"))
display.grid(row=1,columnspan=6,sticky=(N,S,E,W))
 
#adding buttons to the calculator
 
Button(root,text="1", font=("Arial", 14, "bold"), bg = 'sea green', command = lambda :get_variables(1)).grid(row=2,column=0,sticky=(N,S,E,W))
Button(root,text="2", font=("Arial", 14, "bold"), bg = 'sea green',command = lambda :get_variables(2)).grid(row=2,column=1,sticky=(N,S,E,W))
Button(root,text="3", font=("Arial", 14, "bold"), bg = 'sea green',command = lambda :get_variables(3)).grid(row=2,column=2,sticky=(N,S,E,W))
 
Button(root,text="4", font=("Arial", 14, "bold"), bg = 'sea green',command = lambda :get_variables(4)).grid(row=3,column=0,sticky=(N,S,E,W))
Button(root,text="5",font=("Arial", 14, "bold"), bg = 'sea green',command = lambda :get_variables(5)).grid(row=3,column=1,sticky=(N,S,E,W))
Button(root,text="6",font=("Arial", 14, "bold"), bg = 'sea green',command = lambda :get_variables(6)).grid(row=3,column=2,sticky=(N,S,E,W))
 
Button(root,text="7",font=("Arial", 14, "bold"), bg = 'sea green',command = lambda :get_variables(7)).grid(row=4,column=0,sticky=(N,S,E,W))
Button(root,text="8",font=("Arial", 14, "bold"), bg = 'sea green',command = lambda :get_variables(8)).grid(row=4,column=1,sticky=(N,S,E,W))
Button(root,text="9",font=("Arial", 14, "bold"), bg = 'sea green',command = lambda :get_variables(9)).grid(row=4,column=2,sticky=(N,S,E,W))
 
#adding other buttons to the calculator
Button(root,text="AC",font=("Arial", 14), bg = 'dark sea green',command=lambda :clear_all()).grid(row=5,column=0,sticky=(N,S,E,W))
Button(root,text="0",font=("Arial", 14, "bold"), bg = 'sea green',command = lambda :get_variables(0)).grid(row=5,column=1,sticky=(N,S,E,W))
Button(root,text="=",font=("Arial", 14), bg = 'dark sea green',command=lambda :calculate()).grid(row=5,column=2,sticky=(N,S,E,W))
  
Button(root,text="+",font=("Arial", 14),bg = 'dark sea green',command= lambda :get_operation("+")).grid(row=2,column=3,sticky=(N,S,E,W))
Button(root,text="-",font=("Arial", 14),bg = 'dark sea green',command= lambda :get_operation("-")).grid(row=3,column=3,sticky=(N,S,E,W))
Button(root,text="*",font=("Arial", 14),bg = 'dark sea green',command= lambda :get_operation("*")).grid(row=4,column=3,sticky=(N,S,E,W))
Button(root,text="/",font=("Arial", 14),bg = 'dark sea green',command= lambda :get_operation("/")).grid(row=5,column=3,sticky=(N,S,E,W))
 
# adding other operations
Button(root,text="pi",font=("Arial", 14),bg = 'dark sea green',command= lambda :get_operation("*3.14")).grid(row=2,column=4,sticky=(N,S,E,W))
Button(root,text="%",font=("Arial", 14),bg = 'dark sea green',command= lambda :get_operation("%")).grid(row=3,column=4,sticky=(N,S,E,W))
Button(root,text="(",font=("Arial", 14),bg = 'dark sea green',command= lambda :get_operation("(")).grid(row=4,column=4,sticky=(N,S,E,W))
Button(root,text="exp",font=("Arial", 14),bg = 'dark sea green',command= lambda :get_operation("**")).grid(row=5,column=4,sticky=(N,S,E,W))
 
Button(root,text="<-",font=("Arial", 14),bg = 'dark sea green',command= lambda :undo()).grid(row=2,column=5,sticky=(N,S,E,W))
Button(root,text="x!",font=("Arial", 14),bg = 'dark sea green',command= lambda :get_operation("!")).grid(row=3,column=5,sticky=(N,S,E,W))
Button(root,text=")",font=("Arial", 14),bg = 'dark sea green',command= lambda :get_operation(")")).grid(row=4,column=5,sticky=(N,S,E,W))
Button(root,text="^2",font=("Arial", 14),bg = 'dark sea green',command= lambda :get_operation("**2")).grid(row=5,column=5,sticky=(N,S,E,W))

# adding padding to the rows
root.rowconfigure(0, weight = 1, pad = 5)
root.rowconfigure(1, weight = 1, pad = 5)
root.rowconfigure(2, weight = 1, pad = 5)
root.rowconfigure(3, weight = 1, pad = 5)
root.rowconfigure(4, weight = 1, pad = 5)
root.rowconfigure(5, weight = 1, pad = 5)

# adding padding to the columns
root.columnconfigure(0, weight = 1, pad = 5)
root.columnconfigure(1, weight = 1, pad = 5)
root.columnconfigure(2, weight = 1, pad = 5)
root.columnconfigure(3, weight = 1, pad = 5)
root.columnconfigure(4, weight = 1, pad = 5)
root.columnconfigure(5, weight = 1, pad = 5)

root.mainloop()