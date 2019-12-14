from tkinter import *
from tkinter.messagebox import *
import decimal
D=decimal.Decimal
decimal.getcontext().prec=7
import time
start_time = time.time()
def CalcPrice():
   # compute the bond price.
   pv = 0.0
   end_time=0
   try:
      c = couponVar.get()
   except TclError:
      showerror('Coupon Error', 'Enter decimal value between 0 to 1')
   try:
      f = faceValueVar.get()
   except TclError:
      showerror('Face Value Error', 'Enter integer value greater than 0')
   try:
      r = rateVar.get()
   except TclError:
      showerror('Rate Error','Enter decimal value between 0 to 1')
   try:
      t = timeVar.get()
   except TclError:
      showerror('Time Error', 'Enter integer value greater than 0')

   if r < 0.00:
      showerror('Rate Error', 'Enter decimal value between 0 to 1')
      exit()
   if t < 0 or isinstance(t, float):
      showerror('Time Error', 'Enter integer value greater than 0')
      exit()
   if c < 0 or c > 1:
      showerror('Coupon Error', 'Enter decimal value between 0 to 1')
      exit()
   cf = c * f
   for i in range(1, t+1):
      pv += (cf / (1 + r) ** i)
   pv1 = pv + (f / (1 + r) ** t)
   pv1 = D(pv1)
   pv2 = pv1.quantize(D('0.01'), rounding=decimal.ROUND_UP)
   bondPriceVar.set("{0:.7f}".format(pv2))
   end_time=time.time()
   diff = end_time - start_time
   codeTimeVar.set(diff)

def CalcYield():
   # compute the bond yield.
   pv = 0.0
   try:
      c = couponVar.get()
   except TclError:
      showerror('Coupon Error', 'Enter decimal value between 0 to 1')
   try:
      f = faceValueVar.get()
   except TclError:
      showerror('Face Value Error', 'Enter integer value greater than 0')
   try:
      r = rateVar.get()
   except TclError:
      showerror('Rate Error','Enter decimal value between 0 to 1')
   try:
      t = timeVar.get()
   except TclError:
      showerror('Time Error', 'Enter integer value greater than 0')

   if r < 0.00:
      showerror('Rate Error', 'Enter decimal value between 0 to 1')
      exit()
   if t < 0 or isinstance(t, float):
      showerror('Time Error', 'Enter integer value greater than 0')
      exit()
   if c < 0 or c > 1:
      showerror('Coupon Error', 'Enter decimal value between 0 to 1')
      exit()
   cf = c * f
   for i in range(1, t + 1):
      rate=(1+r)**i
      pv += (cf / rate)
   pv1 = pv + (f / (1 + r) ** t)
   pv1=D(pv1)
   pv2= pv1.quantize(D('0.01'), rounding=decimal.ROUND_UP)
   bondYieldVar.set("{0:.7f}".format(pv2))
   end_time=time.time()
   diff = end_time - start_time
   codeTimeVar.set(diff)

# Create a window
window = Tk()
window.title("Bond Yield Calculator")  # Set title
window.geometry("300x200")  # You want the size of the app to be 300x200
window.resizable(0, 0)  # Don't allow resizing in the x or y direction

# create the input boxes.
Label(window, text="Coupon").grid(row=1, column=1, sticky=W)

Label(window, text="Number of Years").grid(row=2, column=1, sticky=W)

Label(window, text="Face Value").grid(row=3, column=1, sticky=W)

Label(window, text="Rate").grid(row=4, column=1, sticky=W)

Label(window, text="Bond Price").grid(row=5, column=1, sticky=W)

Label(window, text="Bond Yield").grid(row=6, column=1, sticky=W)

Label(window, text="Time").grid(row=7, column=1, sticky=W)
# for taking inputs
couponVar = DoubleVar()
Entry(window, textvariable=couponVar, justify=RIGHT).grid(row=1, column=2)

timeVar = IntVar()
Entry(window, textvariable=timeVar, justify=RIGHT).grid(row=2, column=2)

faceValueVar = DoubleVar()
Entry(window, textvariable=faceValueVar, justify=RIGHT).grid(row=3, column=2)

rateVar = DoubleVar()
Entry(window, textvariable=rateVar, justify=RIGHT).grid(row=4, column=2)

bondPriceVar = DoubleVar()
bprice=Label(window, textvariable= bondPriceVar).grid(row=5,column=2, sticky=E)

bondYieldVar = DoubleVar()
byield=Label(window, textvariable= bondYieldVar).grid(row=6,column=2, sticky=E)

codeTimeVar = DoubleVar()
btime = Label(window, textvariable=codeTimeVar).grid(row=7, column=2, sticky=E)
# create the button
b1 = Button(window, text="Compute Price",state = NORMAL, command=CalcPrice).grid(row=8, column=1, sticky=E)

# create the button
b2 = Button(window, text="Compute Yield", state = NORMAL, command=CalcYield).grid(row=8, column=2, sticky=E)

if __name__ == '__main__':
   # Create an event loop
   window.mainloop()

