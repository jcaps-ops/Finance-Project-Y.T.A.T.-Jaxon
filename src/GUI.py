#This will be the set up for the menu using the GUI
import tkinter as tk
import time

root = tk.Tk()

root.title("FINANCE PROJECT")
root.configure(background="light grey")
root.minsize(900,300)
root.maxsize(1500,500)
root.geometry("1200x400+100+100")
#Here is the concept is to make pre loaded and planed areas where we will load with the diffrent labels and buttons
def SignupGUI():
    
    btn.place_forget()
    root.singuplabel = tk.Label(root, text="This is tempory text while we add the sign in function", bg="Light grey", font=("Times new roman", 14, "bold"))
    root.singuplabel.place(relx=.5, rely=0, anchor="n")

    btn1 = tk.Button(root, text="To move forward",command=EnteriesGUI)
    btn1.place(relx=.2, rely=0.4, anchor="n")
    
def EnteriesGUI():
    root.singuplabel.place_forget()
    vent = tk.Button(root, text="View your entries")
    vent.place(relx=.52, rely=0.4, anchor="n")
    aent = tk.Button(root, text="Add an entry")
    aent.place(relx=.48, rely=0.4, anchor="n")

#Here is the starting buttons
btn = tk.Button(root, text="Sign in", command=SignupGUI)
btn.place(relx=.52, rely=0.4, anchor="n")

root.mainloop()