import os
from tkinter import *
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage

for_qr = Tk()
for_qr.title("QR Generator by Cyber | Spider")
for_qr.iconbitmap(r'icon/logo.ico')
for_qr.geometry("900x500+220+70")
for_qr.resizable(False, False)


def generate():
    message_area_variable = message_entry.get('1.0', END)
    for_checking_int_or_str = mobile_no_entry.get()
    if for_checking_int_or_str.isdigit():
        if len(message_entry.get('1.0', END)) <= 1:
                messagebox.showwarning("Warning!", "Message Field Can't be Empty!")
        else:
            x = ''.join(['%' + hex(ord(i))[2:] for i in str(mobile_var.get())])
            y = ''.join(['%' + hex(ord(i))[2:] for i in message_area_variable])
            generated_url = 'https://api.whatsapp.com/send?phone=' + x + '&text=' + y
            qr_code = qrcode.make(generated_url)
            qr_code = resizeimage.resize_cover(qr_code, [180, 180])
            img = ImageTk.PhotoImage(qr_code)
            qr_code_img.config(image=img)
            qr_code.save(str(mobile_no_entry.get()) + ".png")
            qr_generated = "QR Generated Sucessfully!!!"
            label_for_qr_generated.config(text=qr_generated)
            
            
    else:
        messagebox.showwarning("Warning!", "Mobile No. Field Can't be Empty and String!")


def clear():
    mobile_var.set('')
    message_entry.delete('1.0', END)
    qr_code_img.config(image='')
    qr_generated = ""
    label_for_qr_generated.config(text=qr_generated)
        


name = Label(for_qr, text="QR Generator for Whatsapp", font=("times new roman", 30), bg='#053246', fg='White')
name.place(x=0, y=0, relwidth=1)

nu_and_message_frame = Frame(for_qr, bd=2, relief=RIDGE, bg='White')
nu_and_message_frame.place(x=30, y=70, width=500, height=400)
mess = Label(nu_and_message_frame, text="Entry Fields", font=("times new roman", 20), bg='#043256', fg='White')
mess.place(x=0, y=0, relwidth=1)

mobile_no = Label(nu_and_message_frame, text="Mobile No.", font=("times new roman", 15, "bold"), bg='White')
mobile_no.place(x=25, y=50)

mobile_var = StringVar()
mobile_no_entry = Entry(nu_and_message_frame, font=("times new roman", 12), bg='lightyellow', textvariable=mobile_var)
mobile_no_entry.place(x=140, y=52, width=300)

frame_for_message = Frame(nu_and_message_frame)
frame_for_message.place(x=140, y=102, width=300, height=180)

scrollbar_for_message = Scrollbar(frame_for_message, orient=VERTICAL, cursor="hand2")
scrollbar_for_message.pack(side=RIGHT, fill=Y)

message = Label(nu_and_message_frame, text="Message:", font=("times new roman", 15, "bold"), bg='White')
message.place(x=25, y=100)
message_entry = Text(frame_for_message, font=("times new roman", 12), bg='lightyellow', yscrollcommand=scrollbar_for_message.set)
message_entry.pack(fill=BOTH, expand=1)
scrollbar_for_message.config(command=message_entry.yview)


gen_btn = Button(nu_and_message_frame, text="Generate QR", font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", activebackground="lightyellow", command=generate)
gen_btn.place(x=140, y=295)


clear_btn = Button(nu_and_message_frame, text="Clear", font=("times new roman", 15, "bold"), bg="grey", fg="white", cursor="hand2", activebackground="lightyellow", command=clear)
clear_btn.place(x=375, y=295)


qr_field = Frame(for_qr, bd=2, relief=RIDGE, bg='White')
qr_field.place(x=570, y=70, width=295, height=400)
mess = Label(qr_field, text="QR Field", font=("times new roman", 20), bg='#043256', fg='White')
mess.place(x=0, y=0, relwidth=1)

qr_code_img = Label(qr_field, text="No QR\nAvailable", font=("times new roman", 15), bg="#3f51b5", fg="white", bd=1, relief=RIDGE)
qr_code_img.place(x=55, y=100, width=180, height=180)



qr_generated = ""
label_for_qr_generated = Label(qr_field, text=qr_generated, font=("times new roman", 15, "bold"), fg="green", bg='White')
label_for_qr_generated.place(x=0, y=365, relwidth=1)



for_qr.mainloop()
