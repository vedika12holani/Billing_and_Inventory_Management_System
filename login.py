from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import starting
class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("800x500")

        # Load images and resize
        bg_img = Image.open("image/cat.jpg").resize((800, 500), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(bg_img)

        user_icon = Image.open("image/im2.png").resize((30, 30), Image.LANCZOS)
        self.user_icon = ImageTk.PhotoImage(user_icon)

        pass_icon = Image.open("image/im1.png").resize((30, 30), Image.LANCZOS)
        self.pass_icon = ImageTk.PhotoImage(pass_icon)

        logo_icon = Image.open("image/im3.png").resize((150, 150), Image.LANCZOS)
        self.logo_icon = ImageTk.PhotoImage(logo_icon)

        # Variables
        self.uname = StringVar()
        self.pass_ = StringVar()

        # Background image
        bg_lbl = Label(self.root, image=self.bg_img)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame for login form
        login_frame = Frame(self.root, bg="white", bd=5)
        login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Logo
        logolbl = Label(login_frame, image=self.logo_icon, bd=0)
        logolbl.grid(row=0, columnspan=2, pady=20)

        # Username entry
        lbl_user = Label(login_frame, text="Username", image=self.user_icon, compound=LEFT, font=("Arial", 15, "bold"), bg="white", fg="#333333")
        lbl_user.grid(row=1, column=0, padx=20, pady=10, sticky=W)
        txt_user = Entry(login_frame, textvariable=self.uname, bd=5, relief=GROOVE, font=("Arial", 15), width=20)
        txt_user.grid(row=1, column=1, padx=20, pady=10, sticky=W)

        # Password entry
        lbl_pass = Label(login_frame, text="Password", image=self.pass_icon, compound=LEFT, font=("Arial", 15, "bold"), bg="white", fg="#333333")
        lbl_pass.grid(row=2, column=0, padx=20, pady=10, sticky=W)
        txt_pass = Entry(login_frame, textvariable=self.pass_, bd=5, relief=GROOVE, font=("Arial", 15), show="*", width=20)
        txt_pass.grid(row=2, column=1, padx=20, pady=10, sticky=W)

        # Login button
        btn_log = Button(login_frame, text="Login", width=15, command=self.login, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", bd=5)
        btn_log.grid(row=3, columnspan=2, pady=20)

    def login(self):
        if self.uname.get() == "" or self.pass_.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.uname.get() == "admin" and self.pass_.get() == "password":
            messagebox.showinfo("Success", f"Welcome, {self.uname.get()}")
            self.root.withdraw()  # Hide the login window
            self.open_main_window()  # Open the main application window
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    def open_main_window(self):
        new_window=Toplevel(self.root)
        starting.BillingInventory(new_window)
        '''root = Tk()
        obj = print(root)
        root.mainloop()'''

# Main application window
if __name__ == "__main__":
    root = Tk()
    app = LoginSystem(root)
    root.mainloop()
