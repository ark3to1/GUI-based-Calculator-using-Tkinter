from tkinter import *

#----------------------------------------------------------------------- (Back End) -----------------------------------------------------------------------

operator = ""

def button_click(numbers):
    global operator
    operator += str(numbers)
    text.set(operator)

def button_equal():
    global operator

    ans = str(eval(operator))
    text.set(ans)
    operator = ans

def button_clear():
    global operator
    operator = ""
    text.set(operator)

#----------------------------------------------------------------------- (Front End) -----------------------------------------------------------------------

cal = Tk()

cal.title("GUI CALCULATOR")

# Display
text = StringVar()
display = Entry(cal, textvariable=text, bg="sky blue", fg="black", border=10, justify="right", insertwidth=8, font=("Arial", 15, "bold")).grid(columnspan=4)

# Buttons (Numbers)
btn0 = Button(cal, text="0", font=("Arial", 14, "bold") , border=2, padx=15, pady=7, command=lambda:button_click("0")).grid(row=4, column=1)
btn1 = Button(cal, text="1", font=("Arial", 15, "bold") , border=2, padx=15, pady=10, command=lambda:button_click("1")).grid(row=3, column=0)
btn2 = Button(cal, text="2", font=("Arial", 15, "bold") , border=2, padx=15, pady=10, command=lambda:button_click("2")).grid(row=3, column=1)
btn3 = Button(cal, text="3", font=("Arial", 15, "bold") , border=2, padx=15, pady=10, command=lambda:button_click("3")).grid(row=3, column=2)
btn4 = Button(cal, text="4", font=("Arial", 15, "bold") , border=2, padx=15, pady=10, command=lambda:button_click("4")).grid(row=2, column=0)
btn5 = Button(cal, text="5", font=("Arial", 15, "bold") , border=2, padx=15, pady=10, command=lambda:button_click("5")).grid(row=2, column=1)
btn6 = Button(cal, text="6", font=("Arial", 15, "bold") , border=2, padx=15, pady=10, command=lambda:button_click("6")).grid(row=2, column=2)
btn7 = Button(cal, text="7", font=("Arial", 15, "bold") , border=2, padx=15, pady=10, command=lambda:button_click("7")).grid(row=1, column=0)
btn8 = Button(cal, text="8", font=("Arial", 15, "bold") , border=2, padx=15, pady=10, command=lambda:button_click("8")).grid(row=1, column=1)
btn9 = Button(cal, text="9", font=("Arial", 15, "bold") , border=2, padx=15, pady=10, command=lambda:button_click("9")).grid(row=1, column=2)

# Buttons (Operators)
btn_plus = Button(cal, text="+", font=("Arial", 14, "bold"), border=2, padx=15, pady=10, bg="black", fg="white", command=lambda:button_click("+")).grid(row=1, column=3)
btn_minus = Button(cal, text="-", font=("Arial", 15, "bold"), border=2, padx=17, pady=9, bg="black", fg="white", command=lambda:button_click("-")).grid(row=2, column=3)
btn_mul = Button(cal, text="x", font=("Arial", 14, "bold"), border=2, padx=15, pady=10, bg="black", fg="white", command=lambda:button_click("*")).grid(row=3, column=3)
btn_div = Button(cal, text="/", font=("Arial", 14, "bold"), border=2, padx=17, pady=8, bg="black", fg="white", command=lambda:button_click("/")).grid(row=4, column=3)
btn_equal = Button(cal, text="=", font=("Arial", 13, "bold"), border=2, padx=16, pady=10, bg="black", fg="white", command=lambda:button_equal()).grid(row=4, column=2)
btn_C = Button(cal, text="C", font=("Arial", 13, "bold"), border=2, padx=15, pady=10, bg="red", fg="white", command=lambda:button_clear()).grid(row=4, column=0)

cal.mainloop()


