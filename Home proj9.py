from tkinter import *
import random
root = Tk()
root.title("password Generator")
root.geometry("500x500")
root.configure(background = "black")

GL = Label(root)
label = Label(root)

Input = Entry(root)

array_3d = [[['1','2','3','4','5','6',], ["Head","Tail"], ["A","B","C","D","E","F","G","H"]]]
print(array_3d[0][0][4])

def new_password():
    random_no_1 = random.randint(0,5)
    random_no_2 = random.randint(0,1)
    random_no_3 = random.randint(0,7)

    letter1 = str(array_3d[0][0][random_no_1])
    letter2 = (array_3d[0][1][random_no_2])
    letter3 = (array_3d[0][2][random_no_3])
    label["text"] = letter1 + "" + letter2 + "" + letter3

    
def GP():
    GL["text"] = Input.get()   
    
    
GBTN = Button(root, text = "Guess Password", command = GP)    
GBTN.place(relx = 0.8, rely = 0.25, anchor = CENTER)

btn = Button(root, text = "New Password", command = new_password)
btn.place(relx = 0.5, rely = 0.8, anchor = CENTER)

GL.place(relx = 0.5, rely = 0.6, anchor = CENTER)
label.place(relx = 0.5, rely = 0.97, anchor = CENTER)

Input.place(relx = 0.2, rely = 0.25, anchor = CENTER)

root.mainloop()    