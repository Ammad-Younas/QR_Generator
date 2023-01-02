import os
from tkinter import *
from tkinter import messagebox, filedialog
try:
    import qrcode
    from PIL import ImageTk
    from PIL import Image
    from pyzbar.pyzbar import decode
    from resizeimage import resizeimage
except ImportError:
    to_be_install_module = ["pillow", "qrcode", "pyzbar", "python-resize-image"]
    for i in to_be_install:
        os.system("cls || clear")
        print("Installing required packages...")
        os.system(f'pip install {i}')
class decoderHome:
    def __init__(self, decoder_window):
        self.decoder_window = decoder_window
        self.decoder_window.title("QR Decoder by Ammad - Younas")
        self.decoder_window.iconbitmap(r'images/logo.ico')
        self.decoder_window.geometry("900x500+220+70")
        self.decoder_window.resizable(False, False)
        self.decoder_window.focus_force()

        name = Label(self.decoder_window, text="QR Decoder", font=("times new roman", 30), bg='#053246', fg='White')
        name.place(x=0, y=0, relwidth=1)

        upload_qr_field = Frame(self.decoder_window, bd=2, relief=RIDGE, bg='White')
        upload_qr_field.place(x=20, y=70, width=295, height=300)

        upload_mess = Label(upload_qr_field, text="QR Field", font=("times new roman", 20), bg='#043256', fg='White')
        upload_mess.place(x=0, y=0, relwidth=1)

        self.upload_qr_code_img = Label(upload_qr_field, text="No QR\nAvailable", font=("times new roman", 15), bg="#3f51b5", fg="white", bd=1, relief=RIDGE)
        self.upload_qr_code_img.place(x=55, y=60, width=180, height=180)

        self.upload_qr_generated = ""
        self.upload_label_for_qr_generated = Label(upload_qr_field, text=self.upload_qr_generated, font=("times new roman", 15, "bold"), fg="green", bg='White')
        self.upload_label_for_qr_generated.place(x=0, y=255, relwidth=1)

        self.load_before = PhotoImage(file=r'images/select_qr_before.png')
        self.load_after = PhotoImage(file=r'images/select_qr_after.png')

        def on_hover_load(e):
            self.load_btn['image'] = self.load_after

        def on_leave_load(e):
            self.load_btn['image'] = self.load_before

        self.load_btn = Button(self.decoder_window, image=self.load_before, bg="white", activebackground="white", bd=0, cursor='hand2', command=self.load_qr)
        self.load_btn.bind('<Enter>', on_hover_load)
        self.load_btn.bind('<Leave>', on_leave_load)
        self.load_btn.place(x=12, y=400)

        self.clear_decode_before = PhotoImage(file=r'images/clear_decode_before.png')
        self.clear_decode_after = PhotoImage(file=r'images/clear_decode_after.png')

        def on_hover_load(e):
            self.clear_button['image'] = self.clear_decode_after

        def on_leave_load(e):
            self.clear_button['image'] = self.clear_decode_before

        self.clear_button = Button(self.decoder_window, image=self.clear_decode_before, bg="white", activebackground="white", bd=0, cursor='hand2', command=self.clear_decoding)
        self.clear_button.bind('<Enter>', on_hover_load)
        self.clear_button.bind('<Leave>', on_leave_load)
        self.clear_button.place(x=200, y=400)

        decoded_data_frame = Frame(self.decoder_window, bd=2, relief=RIDGE, bg='White')
        decoded_data_frame.place(x=370, y=70, width=500, height=400)

        data = Label(decoded_data_frame, text="Decoded Data", font=("times new roman", 20), bg='#043256', fg='White')
        data.place(x=0, y=0, relwidth=1)

        data_label = Label(decoded_data_frame, text="Decoded Data:", font=("times new roman", 15, "bold"), bg='White')
        data_label.place(x=0, y=50, relwidth=1)

        frame_for_decoded_data = Frame(decoded_data_frame)
        frame_for_decoded_data.place(x=13, y=90, width=470, height=240)

        self.scrollbar_for_decoded_data = Scrollbar(frame_for_decoded_data, orient=VERTICAL, cursor="hand2")
        self.scrollbar_for_decoded_data.pack(side=RIGHT, fill=Y)

        self.data_entry = Text(frame_for_decoded_data, font=("times new roman", 12), bg='#fffee9', state=DISABLED, yscrollcommand=self.scrollbar_for_decoded_data.set)
        self.data_entry.pack(fill=BOTH, expand=1)
        self.scrollbar_for_decoded_data.config(command=self.data_entry.yview)

        self.decode_qr_before = PhotoImage(file=r'images/decode_before.png')
        self.decode_qr_after = PhotoImage(file=r'images/decode_after.png')

        def on_hover_decode(e):
            self.decoder_button['image'] = self.decode_qr_after

        def on_leave_decode(e):
            self.decoder_button['image'] = self.decode_qr_before

        self.decoder_button = Button(decoded_data_frame, image=self.decode_qr_before, bg="white", activebackground="white", bd=0, cursor='hand2', command=self.decode_qr)
        self.decoder_button.bind('<Enter>', on_hover_decode)
        self.decoder_button.bind('<Leave>', on_leave_decode)
        self.decoder_button.place(x=12, y=345)

        self.save_data_before = PhotoImage(file=r'images/save_data_before.png')
        self.save_data_after = PhotoImage(file=r'images/save_data_after.png')

        def on_hover_save_data(e):
            self.save_data['image'] = self.save_data_after

        def on_leave_save_data(e):
            self.save_data['image'] = self.save_data_before

        self.save_data = Button(decoded_data_frame, image=self.save_data_before, bg="white", activebackground="white", bd=0, cursor='hand2', command=self.save_data)
        self.save_data.bind('<Enter>', on_hover_save_data)
        self.save_data.bind('<Leave>', on_leave_save_data)
        self.save_data.place(x=320, y=345)


    # Functioning of Decoder starting here

    def load_qr(self):
        self.open_img = filedialog.askopenfilename(title="Open QR", filetypes=(("PNG Files", "*.png"), ("All Files", "*.*")), parent=self.decoder_window)
        if self.open_img:
            self.get_image = Image.open(self.open_img)
            self.resized_image = resizeimage.resize_cover(self.get_image, [180, 180])
            self.final_loaded_image = ImageTk.PhotoImage(self.resized_image)
            self.upload_qr_code_img.config(image=self.final_loaded_image)
            self.upload_qr_generated = "QR Loaded Sucessfully!"
            self.upload_label_for_qr_generated.config(text=self.upload_qr_generated)
        else:
            pass


    def decode_qr(self):
        if self.upload_qr_generated == "":
            messagebox.showwarning("Warning!", "First select QR code then decoded it", parent=self.decoder_window)
        else:
            self.decoder_data = decode(Image.open(self.open_img))
            self.final_decoded_data = self.decoder_data[0].data.decode('ascii')
            self.data_entry.config(state=NORMAL)
            self.data_entry.delete('1.0', END)
            self.data_entry.insert('1.0', self.final_decoded_data)
            self.upload_qr_generated = "QR Decoded Sucessfully!"
            self.upload_label_for_qr_generated.config(text=self.upload_qr_generated)
            self.data_entry.config(state=DISABLED)


    def clear_decoding(self):
        self.upload_qr_generated = ""
        self.upload_label_for_qr_generated.config(text=self.upload_qr_generated)
        self.data_entry.config(state=NORMAL)
        self.data_entry.delete('1.0', END)
        self.data_entry.config(state=DISABLED)
        self.upload_qr_code_img.config(image="")



    def save_data(self):
        global file_name
        self.data_entry.config(state=NORMAL)
        if len(self.data_entry.get('1.0', END)) <= 1:
            messagebox.showwarning("Warning!", "First decode QR code then save decoded data", parent=self.decoder_window)
        else:
            self.file_name = filedialog.asksaveasfilename(title="Save As", filetypes=(("TXT Files", "*.txt"), ("All Files", "*.*")), parent=self.decoder_window)
            if self.file_name:
                if self.file_name.endswith(".txt"):
                    with open(self.file_name, 'w') as f:
                        f.write(self.data_entry.get('1.0', END))
                    messagebox.showinfo("Info!", "Successfully Saved!", parent=self.decoder_window)
                else:
                    self.file_name = f'{self.file_name}.txt'
                    with open(self.file_name, 'w') as f:
                        f.write(self.data_entry.get('1.0', END))
                    messagebox.showinfo("Info!", "Successfully Saved!", parent=self.decoder_window)
            else:
                pass

class Qr:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Generator by Ammad - Younas")
        self.root.iconbitmap(r'images/logo.ico')
        self.root.geometry("900x500+220+70")
        self.root.resizable(False, False)

        name = Label(self.root, text="QR Generator", font=("times new roman", 30), bg='#053246', fg='White')
        name.place(x=0, y=0, relwidth=1)

        nu_and_message_frame = Frame(self.root, bd=2, relief=RIDGE, bg='White')
        nu_and_message_frame.place(x=30, y=70, width=500, height=400)

        mess = Label(nu_and_message_frame, text="Entry Fields", font=("times new roman", 20), bg='#043256', fg='White')
        mess.place(x=0, y=0, relwidth=1)

        mobile_no = Label(nu_and_message_frame, text="Enter Data:", font=("times new roman", 15, "bold"), bg='White')
        mobile_no.place(x=0, y=50, relwidth=1)

        frame_for_message = Frame(nu_and_message_frame)
        frame_for_message.place(x=13, y=90, width=470, height=240)

        self.scrollbar_for_message = Scrollbar(frame_for_message, orient=VERTICAL, cursor="hand2")
        self.scrollbar_for_message.pack(side=RIGHT, fill=Y)

        self.message_entry = Text(frame_for_message, font=("times new roman", 12), bg='#fffee9', yscrollcommand=self.scrollbar_for_message.set)
        self.message_entry.pack(fill=BOTH, expand=1)
        self.scrollbar_for_message.config(command=self.message_entry.yview)

        self.gen_before = PhotoImage(file=r'images/generate_before.png')
        self.gen_after = PhotoImage(file=r'images/generate_after.png')

        def on_hover_gen(e):
            self.gen_btn['image'] = self.gen_after

        def on_leave_gen(e):
            self.gen_btn['image'] = self.gen_before

        self.gen_btn = Button(nu_and_message_frame, image=self.gen_before, bg="white", activebackground="white", bd=0, cursor='hand2', command=self.generate)
        self.gen_btn.bind('<Enter>', on_hover_gen)
        self.gen_btn.bind('<Leave>', on_leave_gen)
        self.gen_btn.place(x=12, y=345)

        self.clear_create_before = PhotoImage(file=r'images/clear_before.png')
        self.clear_create_after = PhotoImage(file=r'images/clear_after.png')

        def on_hover_clear_create(e):
            self.clear_create_btn['image'] = self.clear_create_after

        def on_leave_clear_create(e):
            self.clear_create_btn['image'] = self.clear_create_before

        self.clear_create_btn = Button(nu_and_message_frame, image=self.clear_create_before, bg="white", activebackground="white", bd=0, cursor='hand2', command=self.clear)
        self.clear_create_btn.bind('<Enter>', on_hover_clear_create)
        self.clear_create_btn.bind('<Leave>', on_leave_clear_create)
        self.clear_create_btn.place(x=365, y=345)

        qr_field = Frame(self.root, bd=2, relief=RIDGE, bg='White')
        qr_field.place(x=570, y=70, width=295, height=300)

        mess = Label(qr_field, text="QR Field", font=("times new roman", 20), bg='#043256', fg='White')
        mess.place(x=0, y=0, relwidth=1)

        self.qr_code_img = Label(qr_field, text="No QR\nAvailable", font=("times new roman", 15), bg="#3f51b5", fg="white", bd=1, relief=RIDGE)
        self.qr_code_img.place(x=55, y=60, width=180, height=180)


        self.qr_generated = ""
        self.label_for_qr_generated = Label(qr_field, text=self.qr_generated, font=("times new roman", 15, "bold"), fg="green", bg='White')
        self.label_for_qr_generated.place(x=0, y=255, relwidth=1)

        self.save_as_before = PhotoImage(file=r'images/save_as_before.png')
        self.save_as_after = PhotoImage(file=r'images/save_as_after.png')

        def on_hover_save_as(e):
            self.save_as_btn['image'] = self.save_as_after

        def on_leave_save_as(e):
            self.save_as_btn['image'] = self.save_as_before

        self.save_as_btn = Button(self.root, image=self.save_as_before, bg="white", activebackground="white", bd=0, cursor='hand2', command=self.save)
        self.save_as_btn.bind('<Enter>', on_hover_save_as)
        self.save_as_btn.bind('<Leave>', on_leave_save_as)
        self.save_as_btn.place(x=550, y=400)

        self.decoder_before = PhotoImage(file=r'images/decoder_before.png')
        self.decoder_after = PhotoImage(file=r'images/decoder_after.png')

        def on_hover_decoder(e):
            self.decoder_btn['image'] = self.decoder_after

        def on_leave_decoder(e):
            self.decoder_btn['image'] = self.decoder_before

        self.decoder_btn = Button(self.root, image=self.decoder_before, bg="white", activebackground="white", bd=0, cursor='hand2', command=self.decoder)
        self.decoder_btn.bind('<Enter>', on_hover_decoder)
        self.decoder_btn.bind('<Leave>', on_leave_decoder)
        self.decoder_btn.place(x=700, y=400)


    def generate(self):
        if len(self.message_entry.get('1.0', END)) <= 1:
            messagebox.showwarning("Warning!", "Input Field Can't be Empty!")
        else:
            self.input_data = self.message_entry.get('1.0', END)
            self.qr_code = qrcode.make(self.input_data)
            self.qr_code = resizeimage.resize_cover(self.qr_code, [180, 180])
            self.img = ImageTk.PhotoImage(self.qr_code)
            self.qr_code_img.config(image=self.img)
            self.qr_generated = "QR Generated Sucessfully!!!"
            self.label_for_qr_generated.config(text=self.qr_generated)


    def clear(self):
        self.message_entry.delete('1.0', END)
        self.qr_code_img.config(image='')
        self.qr_generated = ""
        self.label_for_qr_generated.config(text=self.qr_generated)


    def save(self):
        if self.qr_generated == "":
            messagebox.showwarning("Warning!", "First create QR code then save it")
        else:
            self.save_img = filedialog.asksaveasfilename(title="Save As", filetypes=(("PNG Files", "*.png"), ("All Files", "*.*")))
            if self.save_img:
                if self.save_img.endswith(".png"):
                    self.qr_code.save(self.save_img)
                    messagebox.showinfo("Info!", "Successfully Saved!")
                else:
                    self.save_img = f'{self.save_img}.png'
                    self.qr_code.save(self.save_img)
                    messagebox.showinfo("Info!", "Successfully Saved!")
            else:
                pass



    def decoder(self):
        self.newdecoderwin = Toplevel(self.root)
        self.newdecoderwinobj = decoderHome(self.newdecoderwin)


if __name__ == "__main__":
    root = Tk()
    obj = Qr(root)
    root.mainloop()