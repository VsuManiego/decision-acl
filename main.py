# Project Title: Present and Future Value Calculator for Engineering Decision Using Python
# By:   Aresgado, Cleofe Manuel
#       Cañega, Aaron
#       Laude, Sheenielyn



#Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications.
#Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox



# Root - main system (if you put a code under 'root', it will be made accessible for all the tab systems)
root = Tk()
root.title("Time Value")


#========================
tab_control = ttk.Notebook(root)
tab_control.pack(pady=15)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text = "Future Value")
tab_control.pack(expand=1, fill = "both")

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text = "Present Value")
tab_control.pack (expand=1, fill = "both")

tab_i = ttk.Frame(tab_control)
tab_control.add(tab_i, text= "Investment Value")
tab_control.pack (expand=1, fill= "both")

tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text= "Loan Payment")
tab_control.pack (expand=1, fill="both")

tab4 = ttk.Frame(tab_control)
tab_control.add(tab4, text = "Inflation Rate")
tab_control.pack (expand=1, fill="both")

tab5 = ttk.Frame(tab_control)
tab_control.add(tab5, text = "Payment Value")
tab_control.pack (expand=1, fill="both")

#=====================
#Exit Tab

exit_button1 = tk.Button(tab1, text= "Exit", command= root.destroy, height = 1, width= 10, bg= 'brown', fg= 'white')
exit_button1.pack(pady= 20, side= 'bottom')

exit_button2 = tk.Button(tab2, text= "Exit", command= root.destroy, height = 1, width= 10, bg= 'brown', fg= 'white')
exit_button2.pack(pady= 20, side= 'bottom')

exit_button_i = tk.Button(tab_i, text= "Exit", command= root.destroy, height = 1, width= 10, bg= 'brown', fg= 'white')
exit_button_i.pack(pady= 20, side= 'bottom')

exit_button3 = tk.Button(tab3, text= "Exit", command= root.destroy, height = 1, width= 10, bg= 'brown', fg= 'white')
exit_button3.pack(pady= 20, side= 'bottom')

exit_button4 = tk.Button(tab4, text= "Exit", command= root.destroy, height = 1, width= 10, bg= 'brown', fg= 'white')
exit_button4.pack(pady= 20, side= 'bottom')

exit_button5 = tk.Button(tab5, text= "Exit", command= root.destroy, height = 1, width= 10, bg= 'brown', fg= 'white')
exit_button5.pack(pady= 20, side= 'bottom')


#=====================
#Tab1: Future Value

canvas1 = tk.Canvas(tab1, width=470, height=560)
canvas1.pack()


label1 = tk.Label(tab1, text='Calculate Future Value')
label1.config(font=('helvetica', 14))
canvas1.create_window(235, 40, window=label1)

entry1 = tk.Entry(tab1)
canvas1.create_window(330, 210, window=entry1)

entry2 = tk.Entry(tab1)
canvas1.create_window(330, 250, window=entry2)

entry3 = tk.Entry(tab1)
canvas1.create_window(330, 290, window=entry3)

entry4 = tk.Entry(tab1)
entry4.insert(0, "₱   ")
canvas1.create_window(240, 520, window=entry4)

label1 = tk.Label(tab1, text='     Present Value (PV) in ₱:')
label1.config(font=('helvetica', 10))
canvas1.create_window(170, 210, window=label1)

label2 = tk.Label(tab1, text='Interest Rate (r) in %:')
label2.config(font=('helvetica', 10))
canvas1.create_window(173, 250, window=label2)

label3 = tk.Label(tab1, text='Number of Periods (n):')
label3.config(font=('helvetica', 10))
canvas1.create_window(176, 290, window=label3)

label3a = tk.Label(tab1, text='Compounding Period:')
label3a.config(font=('helvetica', 10))
canvas1.create_window(175, 330, window=label3a)

label_dif1 = tk.Label(tab1, text='Future value (FV) is the value of a current asset at some ')
label_dif1.config(font=('helvetica', 10))
canvas1.create_window(250, 80, window=label_dif1)

label_dif11 = tk.Label(tab1, text='point in the future based on an assumed growth rate. Investors are ')
label_dif11.config(font=('helvetica', 10))
canvas1.create_window(250, 100, window=label_dif11)

label_dif12 = tk.Label(tab1, text='able to reasonably assume an investment’s profit using the FV calculation.')
label_dif12.config(font=('helvetica', 10))
canvas1.create_window(250, 120, window=label_dif12)
#===========
#Radio Buttons
var = IntVar ()
var.set(1) # initializing the choice, i.e. Python

R1 = Radiobutton(tab1, text= ("Monthly"), variable=var, value=12)
R1.place (x= 280, y=320)


R2 = Radiobutton(tab1, text="Quarterly", variable=var, value=4)
R2.place (x= 280, y = 350)

R3 = Radiobutton(tab1, text="Semi-Annually", variable=var, value=2)
R3.place (x=280, y = 380)

R3 = Radiobutton(tab1, text="Annually", variable=var, value=1)
R3.place (x=280, y= 410)
label = Label(tab1)
label.pack()

#==============
def calcFV():
    try:
        PV = float(entry1.get())
        r = float(entry2.get())
        n = float(entry3.get())
        c = float(str(var.get()))

    except ValueError:
        messagebox.showerror("Error","You Must Enter an Integer. Try Again.")


    else:
        r_cp1 = (r/100)
        n_cp1 = (n*c)
        FV = PV * ((((1 + r_cp1) ** n_cp1)-1)/r_cp1)
        format_FV = "{:.2f}".format(FV)

        label4 = tk.Label(tab1, text=format_FV, font=('helvetica', 10, 'bold'), bg='white')
        canvas1.create_window(240, 520, window=label4)



button1 = tk.Button(text='Calculate Future Value', command=calcFV, bg='green', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(240, 480, window=button1)

img1 = tkinter.PhotoImage(file= "FV of Ordinary Annuity.png").zoom(60).subsample(150)
canvas1_img= canvas1.create_image(250,160,image= img1)

#=============
#Tab2: Present Value

canvas2 = tk.Canvas(tab2, width = 470, height = 560)
canvas2.pack()

label5 = tk.Label(tab2, text='Calculate Present Value')
label5.config(font=('helvetica', 14))
canvas2.create_window(235, 40, window=label5)

entry5 = tk.Entry(tab2)
canvas2.create_window(330, 270, window=entry5)

entry6 = tk.Entry(tab2)
canvas2.create_window(330, 310, window=entry6)

entry7 = tk.Entry(tab2)
canvas2.create_window(330, 350, window=entry7)

entry8 = tk.Entry(tab2)
entry8.insert(0, "₱   ")
canvas2.create_window(240, 570, window=entry8)

label5 = tk.Label(tab2, text='   Future Value (FV) in ₱:')
label5.config(font=('helvetica', 10))
canvas2.create_window(173, 270, window=label5)

label6 = tk.Label(tab2, text='Interest Rate (r):')
label6.config(font=('helvetica', 10))
canvas2.create_window(160, 310, window=label6)

label7 = tk.Label(tab2, text='         Number of Periods (n):')
label7.config(font=('helvetica', 10))
canvas2.create_window(160, 350, window=label7)

label_dif2 = tk.Label (tab2, text= 'Present value states that an amount of money today is worth more ')
label_dif2.config(font=('helvetica', 10))
canvas2.create_window(240, 80, window=label_dif2)

label_dif21 = tk.Label (tab2, text= 'than the same amount in the future. In other words, it shows that money ')
label_dif21.config(font=('helvetica', 10))
canvas2.create_window(240, 100, window=label_dif21)

label_dif22 = tk.Label (tab2, text= 'received in the future is not worth as much as an equal amount received today.')
label_dif22.config(font=('helvetica', 10))
canvas2.create_window(240, 120, window=label_dif22)

label_dif23 = tk.Label(tab2, text='Compounding Period:')
label_dif23.config(font=('helvetica', 10))
canvas2.create_window(175, 390, window=label_dif23)
#===========
#Radio Buttons

R2_a = Radiobutton(tab2, text= "Monthly", variable=var, value=12)
R2_a.place (x= 280, y=390)


R2_b = Radiobutton(tab2, text="Quarterly", variable=var, value=4)
R2_b.place (x= 280, y = 420)

R2_c = Radiobutton(tab2, text="Semi-Annually", variable=var, value=2)
R2_c.place (x=280, y = 450)

R2_d = Radiobutton(tab2, text="Annually", variable=var, value=1)
R2_d.place (x=280, y= 480)

#==============

def calcPV():
    try:
        FV = float(entry5.get())
        r_2 = float(entry6.get())
        n_2 = float(entry7.get())
        c_2 = float(str(var.get()))

    except ValueError:
        messagebox.showerror("Error", "You Must Enter an Integer. Try Again")

    else:

        r_cp2 = (r_2/100)
        n_cp2 = (n_2*c_2)
        PV = FV*((1-(1/(1+r_cp2)**n_cp2))/r_cp2)
        format_PV = "{:.2f}".format(PV)

        label8 = tk.Label(tab2, text=format_PV, font=('helvetica', 10, 'bold'), bg='white')
        canvas2.create_window(240, 570, window=label8)


button2 = tk.Button(text='Calculate Present Value', command=calcPV, bg='green', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas2.create_window(240, 530, window=button2)

img2 = tkinter.PhotoImage(file= "PV of Ordinary Annuity.png").zoom(50).subsample(140)
canvas2_img= canvas2.create_image(250,180,image= img2)

#==================
#Tab3: Investment

canvas_i = tk.Canvas(tab_i, width = 470, height = 480)
canvas_i.pack()

label_i3 = tk.Label(tab_i, text="....definition....")
label_i3.config(font=('helvetica', 10))
canvas_i.create_window(240, 80, window=label_i3)

label_i1 = tk.Label(tab_i, text="Draft: Not the actual formula of investment. For Layout Purposes Only. ")
label_i1.config(font=('helvetica', 10))
canvas_i.create_window(240, 100, window=label_i1)

label_i2 = tk.Label(tab_i, text='Calculate for Investment Value')
label_i2.config(font=('helvetica', 14))
canvas_i.create_window(235, 40, window=label_i2)

entry_i = tk.Entry(tab_i)
canvas_i.create_window(330, 160, window=entry_i)

entry_i1 = tk.Entry(tab_i)
canvas_i.create_window(330, 200, window=entry_i1)

entry_i2 = tk.Entry(tab_i)
entry_i2.insert(0, "₱   ")
canvas_i.create_window(240, 380, window=entry_i2)

label_ia = tk.Label(tab_i, text='Previous Consumer Price Tax:')
label_ia.config(font=('helvetica', 10))
canvas_i.create_window(160, 160, window=label_ia)

label_ib = tk.Label(tab_i, text='Current Consumer Price Tax: ')
label_ib.config(font=('helvetica', 10))
canvas_i.create_window(160, 200, window=label_ib)

#Draft: Not the actual formula of investment. For Layout Purposes Only.

def calcInvestment():
    try:
        investment_p = float(entry_i.get())
        investment_c = float(entry_i1.get())

    except ValueError:
        messagebox.showerror("Error", "You Must Enter an Integer. Try Again.")

    else:
        #Draft: Not the actual formula of investment. For Layout Purposes Only.

        Investment = ((investment_c - investment_p) / investment_p) * 100

    # Draft: Not the actual formula of investment. For Layout Purposes Only.

        label_ic = tk.Label(tab_i, text=Investment, font=('helvetica', 9, 'bold'), bg='white')
        canvas_i.create_window(240, 380, window=label_ic)

#Draft: Not the actual formula of investment. For Layout Purposes Only.

button_id = tk.Button(text='Calculate Investment Rate', command=calcInvestment, bg='green', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas_i.create_window(240, 330, window=button_id)

#==================
#Loan Payment

canvas_3= tk.Canvas(tab3, width= 470, height= 560)
canvas_3.pack()

label_3a = tk.Label(tab3, text='Calculate for Loan Payment')
label_3a.config(font=('helvetica', 14))
canvas_3.create_window(235, 40, window=label_3a)

label_3b = tk.Label(tab3, text="The loan payment formula is used to calculate the payments on a loan.")
label_3b.config(font=('helvetica', 10))
canvas_3.create_window(240, 80, window=label_3b)

label_3c = tk.Label(tab3, text="By definition, it is an annuity that consists of a series of future periodic payments.")
label_3c.config(font=('helvetica', 10))
canvas_3.create_window(240, 100, window=label_3c)

entry_3a = tk.Entry(tab3)
canvas_3.create_window(330, 220, window=entry_3a)

entry_3b = tk.Entry(tab3)
canvas_3.create_window(330, 260, window=entry_3b)

entry_3c = tk.Entry(tab3)
canvas_3.create_window(330, 300, window=entry_3c)

entry_3d = tk.Entry(tab3)
entry_3d.insert(0, "₱   ")
canvas_3.create_window(240, 540, window=entry_3d)

label_3e = tk.Label(tab3, text='   Present Value (FV) in ₱:')
label_3e.config(font=('helvetica', 10))
canvas_3.create_window(173, 220, window=label_3e)

label_3f = tk.Label(tab3, text='Interest Rate (r):')
label_3f.config(font=('helvetica', 10))
canvas_3.create_window(160, 260, window=label_3f)

label_3g = tk.Label(tab3, text='         Number of Periods (n):')
label_3g.config(font=('helvetica', 10))
canvas_3.create_window(160, 300, window=label_3g)

label_dif3a = tk.Label(tab3, text='Compounding Period:')
label_dif3a.config(font=('helvetica', 10))
canvas_3.create_window(175, 340, window=label_dif3a)
#===========
#Radio Buttons

R4_a = Radiobutton(tab3, text= "Monthly", variable=var, value=12)
R4_a.place (x= 280, y=340)


R4_b = Radiobutton(tab3, text="Quarterly", variable=var, value=4)
R4_b.place (x= 280, y = 370)

R4_c = Radiobutton(tab3, text="Semi-Annually", variable=var, value=2)
R4_c.place (x=280, y = 400)

R4_d = Radiobutton(tab3, text="Annually", variable=var, value=1)
R4_d.place (x=280, y= 430)

#==============

def calcLP():
    try:
        PV = float(entry_3a.get())
        r_4 = float(entry_3b.get())
        n_4 = float(entry_3c.get())
        c_4 = float(str(var.get()))

    except ValueError:
        messagebox.showerror("Error", "You Must Enter an Integer. Try Again")

    else:

        r_cp4 = (r_4/100)
        n_cp4 = (n_4*c_4)
        P= ((r_cp4*PV)/(1-(1+r_cp4)**-n_cp4))
        format_P = "{:.2f}".format(P)

        label_3h = tk.Label(tab3, text=format_P, font=('helvetica', 10, 'bold'), bg='white')
        canvas_3.create_window(240, 540, window=label_3h)


button4= tk.Button(text='Calculate Loan Payment', command=calcLP, bg='green', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas_3.create_window(240, 500, window=button4)

img3 = tkinter.PhotoImage(file= "LoanPaymemt.png").zoom(80).subsample(140)
canvas_3_img= canvas_3.create_image(250,150,image= img3)

#==================
#Tab4: Inflation

canvas4 = tk.Canvas(tab4, width = 470, height = 560)
canvas4.pack()

label_dif4 = tk.Label(tab4, text="The inflation rate is a measurement of the rise in price of ")
label_dif4.config(font=('helvetica', 10))
canvas4.create_window(240, 80, window=label_dif4)

label_dif41 = tk.Label(tab4, text="a good or service over a period of time reflected as a percentage.")
label_dif41.config(font=('helvetica', 10))
canvas4.create_window(240, 100, window=label_dif41)

label9 = tk.Label(tab4, text='Calculate for Inflation Rate')
label9.config(font=('helvetica', 14))
canvas4.create_window(235, 40, window=label9)

entry9 = tk.Entry(tab4)
canvas4.create_window(330, 200, window=entry9)

entry10 = tk.Entry(tab4)
canvas4.create_window(330, 240, window=entry10)

entry11 = tk.Entry(tab4)
canvas4.create_window(240, 380, window=entry11)

label9 = tk.Label(tab4, text='Previous Consumer Price Tax:')
label9.config(font=('helvetica', 10))
canvas4.create_window(160, 200, window=label9)

label10 = tk.Label(tab4, text='Current Consumer Price Tax: ')
label10.config(font=('helvetica', 10))
canvas4.create_window(160, 240, window=label10)


def calcInflation():
    try:
        inflation_p = float(entry9.get())
        inflation_c = float(entry10.get())

    except ValueError:
        messagebox.showerror("Error", "You Must Enter an Integer. Try Again.")

    else:
        Inflation = ((inflation_c-inflation_p)/inflation_p)*100
        format_Inflation = "{:g}%".format(Inflation)

        label11 = tk.Label(tab4, text= format_Inflation, font=('helvetica', 9, 'bold'), bg='white')
        canvas4.create_window(240, 380, window=label11)


button4 = tk.Button(text='Calculate Inflation Rate', command=calcInflation, bg='green', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas4.create_window(240, 330, window=button4)

img4 = tkinter.PhotoImage(file= "Inflation.png").zoom(40).subsample(100)
canvas4_img= canvas4.create_image(250,150,image= img4)
#=====================
#Payment Value

canvas_5 = tk.Canvas(tab5, width = 470, height = 480)
canvas_5.pack()

label_51 = tk.Label(tab5, text='Calculate for Payment Value')
label_51.config(font=('helvetica', 14))
canvas_5.create_window(235, 40, window=label_51)

label_dif5 = tk.Label(tab5, text="The annuity payment formula is used to calculate the periodic payment")
label_dif5.config(font=('helvetica', 10))
canvas_5.create_window(240, 80, window=label_dif5)

label_52 = tk.Label(tab5, text="on an annuity. The annuity payment formula can be used for amortized loans,")
label_52.config(font=('helvetica', 10))
canvas_5.create_window(240, 100, window=label_52)

label_53 = tk.Label(tab5, text=" income annuities, structured settlements, and  other constant periodic payments.")
label_53.config(font=('helvetica', 10))
canvas_5.create_window(240, 120, window=label_53)

entry_5a = tk.Entry(tab5)
canvas_5.create_window(330, 160, window=entry_5a)

entry_5b = tk.Entry(tab5)
canvas_5.create_window(330, 200, window=entry_5b)

entry_5c = tk.Entry(tab5)
canvas_5.create_window(330, 240, window=entry_5c)

entry_5d = tk.Entry(tab5)
entry_5d.insert(0, "₱   ")
canvas_5.create_window(240, 380, window=entry_5d)

label_54 = tk.Label(tab5, text='Present Value (PV) in ₱:')
label_54.config(font=('helvetica', 10))
canvas_5.create_window(160, 160, window=label_54)

label_55 = tk.Label(tab5, text='Rate Per Period (r) in %: ')
label_55.config(font=('helvetica', 10))
canvas_5.create_window(160, 200, window=label_55)

label_56 = tk.Label(tab5, text='Number of Periods (n): ')
label_56.config(font=('helvetica', 10))
canvas_5.create_window(160, 240, window=label_56)

def calcPayment():
    try:
        payment_pv = float(entry_5a.get())
        payment_r = float(entry_5b.get())
        payment_n = float(entry_5c.get())

    except ValueError:
        messagebox.showerror("Error", "You Must Enter an Integer. Try Again.")

    else:
        payment_ri = payment_r/100
        Payment = (payment_ri*payment_pv)/(1-(1+payment_ri)**-payment_n)
        format_Payment = "{:.2f}".format(Payment)

        label_57 = tk.Label(tab5, text=format_Payment, font=('helvetica', 9, 'bold'), bg='white')
        canvas_5.create_window(240, 380, window=label_57)


button_p = tk.Button(text='Calculate Payment Value', command=calcPayment, bg='green', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas_5.create_window(240, 330, window=button_p)

#=========================

root.mainloop()

