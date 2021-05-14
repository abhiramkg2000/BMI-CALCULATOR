from tkinter import *

#function to respond to button event
def click():
    output1.delete(0.0,END)
    output2.delete(0.0,END)
    output1.insert(END,calc())
    output2.insert(END,message())

#function to calculate bmi    
def calc():
    num1=float(t1.get())
    num2=float(t2.get())
    num1=num1/100
    result=num2/(num1**2)
    return round(result,2)

#function to set message
def message():
    bmi=calc()
    if bmi<18.50:
        msg="Underweight"
    elif bmi>=18.50 and bmi<=24.99:
        msg="Healthy"
    elif bmi>=25.00 and bmi<=29.99:
        msg="Overweight"
    elif bmi>30.00:
        msg="Obese"
    return msg
#hover effect on button
def onbutton(e):
    b1['bg']='green'
def leavebutton(e):
    b1['bg']='#013DC4'

#creating a window using Tk() function
window=Tk();
window.title("BMI calculator")
window.config(bg="#013DC4")
window.geometry("830x600")

#code for adding 2 images
photo1=PhotoImage(file="C:\\Users\\abhiram\\Downloads\\bmi.png")
photo2=PhotoImage(file="C:\\Users\\abhiram\\Desktop\\bmi1.png")
l4=Label(window,image=photo1,bg="#013DC4")
l5=Label(window,image=photo2,bg="#013DC4",width="850")

#creating 3 labels
l1=Label(window,text="Enter height(in cm):",bg="#013DC4",fg="#E2D3F4",font="calibri 12 bold")
l2=Label(window,text="Enter weight(in kg):",bg="#013DC4",fg="#E2D3F4",font="calibri 12 bold")
l3=Label(window,text="BMI:",bg="#013DC4",fg="#E2D3F4",font="calibri 12 bold")
l6=Label(window,text="Report:",bg="#013DC4",fg="#E2D3F4",font="calibri 12 bold")

#creating 2 textfields
t1=Entry(window,bg="#E2D3F4")
t2=Entry(window,bg="#E2D3F4")

#creating a button
b1=Button(window,text="Calculate",bg="#013DC4",fg="#E2D3F4",font="calibri 12 bold",command=click)
b1.bind('<Enter>',onbutton)
b1.bind('<Leave>',leavebutton)
#creating 2 textboxes 
output1=Text(window,width="15",height="1",bg="#E2D3F4")
output2=Text(window,width="15",height="1",bg="#E2D3F4")

l1.place(x=20,y=350)
l2.place(x=20,y=400)
l3.place(x=20,y=500)
l4.place(x=350,y=350)
l5.place(x=-7,y=-2)
l6.place(x=20,y=550)
t1.place(x=170,y=350)
t2.place(x=170,y=400)
b1.place(x=170,y=450)
output1.place(x=170,y=500)
output2.place(x=170,y=550)
window.mainloop()