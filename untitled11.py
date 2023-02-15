from tkinter import*
import random

root=Tk()
root.title("sales application")
root.geometry("500x500")
root.configure(background = "blue")


label_month = Label(root)
label_profit = Label(root)


label_max = Label(root)
label_min = Label(root)



month = ("January","February","March","April","May","June","July","August","September","October","'November","December")
profits = (309829,35445837,4364749,45383638,1037390,1000,3990,12407,30239,284002,273957,3638)
  
label_month["text"] = "months:"+str(month)
label_profit["text"] = "profits:"+str(profits)

def maxProfit():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    max_profit_month[max_profit_index]
    label_max_profit["text"] = "maximum profit of"+str(max_profit)+" was given in the month of "+str(max_profit_month)
    
def minProfit():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    min_profit_month[min_profit_index]
    label_min_profit["text"] = "minimum profit of"+str(max_profit)+" was given in the month of "+str(min_profit_month)   
    
    
label_month.place(relx=0.5, rely=0.2, anchor=CENTER)
label_pofits.place(relx=0.5, rely=0.3, anchor=CENTER)



btn_max = Button(root, text="Show max Profitable Month"), command=max_Profit, bg = "Royal blue", fg = "white")
btn_min = Button(root, text="Show min Profitable Month"), command=min_Profit, bg = "Royal blue", fg = "white")
     
btn_max.place(relx=0.5, rely=0.4, anchor=CENTER)
label_max_profit.place(relx=0.5, rely=0.5, anchor=CENTER)

btn_min.place(relx=0.5, rely=0.6, anchor=CENTER)

label_min_profit.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()    
    
 
    
    
    