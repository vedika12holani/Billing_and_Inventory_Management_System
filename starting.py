from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import viewinventory
import addinventory
import print

class BillingInventory:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x750+0+0")
        self.root.title("Billing and Inventory Management System")
        self.root.iconbitmap('image/logo1.ico')
        self.root.config(bg='white')

        # Create a frame for the title
        title_frame = Frame(root, bg='#f0f0f0')
        title_frame.place(relx=0.5, rely=0.1, anchor=CENTER, relwidth=1, height=70)

        # Add title label inside the frame
        title_font = font.Font(family="Helvetica", size=36, weight="bold")
        title_label = Label(title_frame, text="Billing and Inventory Management", font=title_font, bg='#430808', fg='white')
        title_label.pack(fill=BOTH, expand=True, pady=10)

        # Create a frame for the moving text
        moving_text_frame = Frame(root, bg='#f0f0f0')
        moving_text_frame.place(relx=0.5, rely=0.2, anchor=CENTER, relwidth=1, height=40)

        # Add welcome message inside the frame
        welcome_font = font.Font(family="Helvetica", size=15, weight="normal")
        self.welcome_label = Label(moving_text_frame, text="Welcome to our billing and inventory management website.", font=welcome_font, bg='#f0f0f0', fg='#333333')
        self.welcome_label.place(x=-500, rely=0.5, anchor=W)

        # Start the animation
        self.move_text()

        # Create frames for the three boxes with opaque background
        box_frame1 = Frame(root, bg='#a0d2eb', bd=2, relief=RIDGE)
        box_frame2 = Frame(root, bg='#a0d2eb', bd=2, relief=RIDGE)
        box_frame3 = Frame(root, bg='#a0d2eb', bd=2, relief=RIDGE)

        box_frame1.place(relx=0.15, rely=0.6, anchor=CENTER, relwidth=0.25, relheight=0.50)
        box_frame2.place(relx=0.5, rely=0.6, anchor=CENTER, relwidth=0.25, relheight=0.50)
        box_frame3.place(relx=0.85, rely=0.6, anchor=CENTER, relwidth=0.25, relheight=0.50)

        # Add content to the first box
        title1 = Label(box_frame1, text="View Inventory", font=("Helvetica", 18, "bold"), bg='#4682B4', fg='white')
        title1.pack(pady=10)

        # Load and blend the logo image with box background
        logo1 = Image.open("image/inventory.jpg")
        logo1 = logo1.resize((200, 200), Image.LANCZOS)
        logo1 = logo1.convert("RGBA")

        # Create a blank image with the same size and background as the box
        box_bg1 = Image.new("RGBA", (200, 200), "#800020")

        # Blend the logo onto the box background
        blended_image1 = Image.alpha_composite(box_bg1, logo1)
        blended_photo1 = ImageTk.PhotoImage(blended_image1)

        image_label1 = Label(box_frame1, image=blended_photo1, bg='#800020')
        image_label1.image = blended_photo1
        image_label1.pack()

        button1 = Button(box_frame1, text="View Inventory", command=self.button_1, font=("Helvetica", 14), bd=2)
        button1.pack(pady=24)

        # Add content to the second box
        title2 = Label(box_frame2, text="Add to Inventory", font=("Helvetica", 18, "bold"), bg='#4682B4', fg='white')
        title2.pack(pady=10)

        # Load and blend the logo image with box background
        logo2 = Image.open("image/add.jpg")
        logo2 = logo2.resize((200, 200), Image.LANCZOS)
        logo2 = logo2.convert("RGBA")

        # Create a blank image with the same size and background as the box
        box_bg2 = Image.new("RGBA", (200, 200), "#800020")

        # Blend the logo onto the box background
        blended_image2 = Image.alpha_composite(box_bg2, logo2)
        blended_photo2 = ImageTk.PhotoImage(blended_image2)

        image_label2 = Label(box_frame2, image=blended_photo2, bg='#800020')
        image_label2.image = blended_photo2
        image_label2.pack()

        button2 = Button(box_frame2, text="Add to Inventory", command=self.button_2, font=("Helvetica", 14), bd=2)
        button2.pack(pady=24)

        # Add content to the third box
        title3 = Label(box_frame3, text="Billing Section", font=("Helvetica", 18, "bold"), bg='#4682B4', fg='white')
        title3.pack(pady=10)

        # Load and blend the logo image with box background
        logo3 = Image.open("image/bill.png")
        logo3 = logo3.resize((200, 200), Image.LANCZOS)
        logo3 = logo3.convert("RGBA")

        # Create a blank image with the same size and background as the box
        box_bg3 = Image.new("RGBA", (200, 200), "#800020")

        # Blend the logo onto the box background
        blended_image3 = Image.alpha_composite(box_bg3, logo3)
        blended_photo3 = ImageTk.PhotoImage(blended_image3)

        image_label3 = Label(box_frame3, image=blended_photo3, bg='#800020')
        image_label3.image = blended_photo3
        image_label3.pack()

        button3 = Button(box_frame3, text="Billing Section", command=self.button_3, font=("Helvetica", 14), bd=2)
        button3.pack(pady=24)

        # Footer background
        footer_bg = Image.new("RGBA", (1500, 30), "#8E8A8A")
        footer_photo = ImageTk.PhotoImage(footer_bg)

        # Footer background label
        lbl_footer_bg = Label(root, image=footer_photo, bg="#8E8A8A")
        lbl_footer_bg.place(relx=0.5, rely=1.0, anchor=S)

        # Footer text label
        lbl_footer_text = Label(root, text="BIMS-Billing and Inventory Management System\nFor any technical issue contact: 762*****10", font=("times new roman", 12), bg="#8E8A8A", fg="white")
        lbl_footer_text.place(relx=0.5, rely=1.0, anchor=S)

    def move_text(self):
        current_x = self.welcome_label.winfo_x()
        new_x = current_x + 2

        # Reset to start position when the text moves out of the window
        if new_x > self.root.winfo_width():
            new_x = -self.welcome_label.winfo_width()

        self.welcome_label.place(x=new_x, rely=0.5, anchor=W)
        self.root.after(20, self.move_text)  # Adjust the delay for smoothness

    # Define the callback function for Button 1
    def button_1(self):
        new_window = Toplevel(self.root)  # Open a new window
        viewinventory.ViewInventory(new_window)  # Call the class from viewinventory.py

    # Define the callback function for Button 2
    def button_2(self):
        new_window = Toplevel(self.root)  # Open a new window
        addinventory.AddProductToInventory(new_window)  # Call the class from addinventory.py

    # Define the callback function for Button 3
    def button_3(self):
        new_window = Toplevel(self.root)  # Open a new window
        print.GeneratingPrintingBill(new_window)  # Call the class from print.py

if __name__ == "__main__":
    root = Tk()
    obj = BillingInventory(root)
    root.mainloop()
