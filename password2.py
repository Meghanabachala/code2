
import random                           
import tkinter as tk                     
from tkinter import *                   
from tkinter import messagebox as mb     
def generate_password(len):  
    "This function accepts a parameter 'len' and returns a randomly generated password"   
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"    
    selected_char = random.sample(list_of_chars, len) 
    pass_str = "".join(selected_char)  
    pass_label.config(text = pass_str)  
    print("Generated Password is :", pass_str, "\n")   
def selection():      
    len = length.get()   
    if len != 0:  
        generate_password(len)  
    else:  
        mb.showerror("Invalid Selection", "Length of Password is not defined.")  
def get_length():     
    print("Selected Length of Password :", length.get(), "characters")   
def reset():  
    "This function will reset everything in the application"  
    length.set(0)   
    pass_label.config(text = "")  
if __name__ == "__main__":    
    gui_root = Tk()  
    gui_root.title("Random Password Generator")   
    gui_root.geometry("500x450+400+200")    
    gui_root.config(bg = "green")   
    heading_frame = Frame(gui_root, bg = "#7B68EE")  
    radiobtn_frame = Frame(gui_root, bg = "#E6E6FA")  
    button_frame = Frame(gui_root, bg = "#E6E6FA")  
    result_frame = Frame(gui_root, bg = "#E6E6FA")    
    heading_frame.pack(fill = "both")  
    radiobtn_frame.pack(pady = 10)  
    button_frame.pack(pady = 10)  
    result_frame.pack(pady = 10)      
    heading = Label(  
        heading_frame,  
        text = "RANDOM PASSWORD GENERATOR",  
        font = ("Bahnschrift SemiBold", "17"),  
        bg = "#7B68EE",  
        fg = "#FFFFFF"  
        )  
    subheading = Label(  
        heading_frame,  
        text = "Customize the Length of the Password:",  
        font = ("Bahnschrift SemiBold", "14"),  
        bg = "#4B0082",  
        fg = "#FFFFFF"  
        )    
    heading.pack(pady = 10)  
    subheading.pack(fill = "both")  
    length = IntVar()   
    length.set(0)   
    radiobuttonOne = Radiobutton(  
        radiobtn_frame,  
        text = '4 Characters',  
        variable = length,  
        value = 4,  
        font = ("Times New Roman", "12"),  
        bg = "#E6E6FA",  
        command = get_length  
        )    
    radiobuttonTwo = Radiobutton(  
        radiobtn_frame,  
        text = '6 Characters',  
        variable = length,  
        value = 6,  
        font = ("Times New Roman", "12"),  
        bg = "#E6E6FA",  
        command = get_length  
        )   
    radiobuttonThree = Radiobutton(  
        radiobtn_frame,  
        text = '8 Characters',  
        variable = length,  
        value = 8,  
        font = ("Times New Roman", "12"),  
        bg = "#E6E6FA",  
        command = get_length  
        )   
    radiobuttonFour = Radiobutton(  
        radiobtn_frame,  
        text = '10 Characters',  
        variable = length,  
        value = 10,  
        font = ("Times New Roman", "12"),  
        bg = "#E6E6FA",  
        command = get_length  
        )   
    radiobuttonFive = Radiobutton(  
        radiobtn_frame,  
        text = '12 Characters',  
        variable = length,  
        value = 12,  
        font = ("Times New Roman", "12"),  
        bg = "#E6E6FA",  
        command = get_length  
        )  
    radiobuttonSix = Radiobutton(  
        radiobtn_frame,  
        text = '16 Characters',  
        variable = length,  
        value = 16,  
        font = ("Times New Roman", "12"),  
        bg = "#E6E6FA",  
        command = get_length  
        )   
    radiobuttonOne.grid(row = 0, column = 0, padx = 10, pady = 2, sticky = W)  
    radiobuttonTwo.grid(row = 0, column = 1, padx = 10, pady = 2, sticky = W)  
    radiobuttonThree.grid(row = 1, column = 0, padx = 10, pady = 2, sticky = W)  
    radiobuttonFour.grid(row = 1, column = 1, padx = 10, pady = 2, sticky = W)  
    radiobuttonFive.grid(row = 2, column = 0, padx = 10, pady = 2, sticky = W)  
    radiobuttonSix.grid(row = 2, column = 1, padx = 10, pady = 2, sticky = W)  
    get_pass = Button(  
        button_frame,  
        text = "Get Password",  
        font = ("Bahnschrift SemiBold", "12"),  
        width = 14,  
        bg = "#32CD32",  
        fg = "#FFFFFF",  
        activebackground = "#006400",  
        activeforeground = "#FFFFFF",  
        relief = GROOVE,  
        command = selection  
        )   
    clear_all = Button(  
        button_frame,  
        text = "Reset",  
        font = ("Bahnschrift SemiBold", "12"),  
        width = 14,  
        bg = "#FF0000",  
        fg = "#FFFFFF",  
        activebackground = "#8B0000",  
        activeforeground = "#FFFFFF",  
        relief = GROOVE,  
        command = reset  
        )    
    get_pass.grid(row = 0, column = 0, padx = 5, pady = 2)  
    clear_all.grid(row = 0, column = 1, padx = 5, pady = 2)    
    pass_label = Label(  
        result_frame,  
        text = "",  
        font = ("Consolas", "15", "bold"),  
        bg = "#E6E6FA",  
        fg = "#000000"  
        )  
    pass_label.pack()    
    gui_root.mainloop()  
