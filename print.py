
from tkinter import *
from tkinter import font, ttk, messagebox
from PIL import Image, ImageTk, ImageFilter
import sqlite3

class GeneratingPrintingBill:
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

        # Buyer details
        self.buyer_name = StringVar()
        self.buyer_contact = StringVar()

        # Product details
        self.product_name = StringVar()
        self.product_quantity = IntVar()
        self.total_amount = DoubleVar(value=0.0)

        # Initialize product list
        self.product_list = []

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Buyer Details Frame
        buyer_frame = LabelFrame(self.root, text="Buyer Details", font=("times new roman", 15, "bold"), bg="white")
        buyer_frame.place(x=10, y=220, width=700, height=120)

        lbl_name = Label(buyer_frame, text="Name:", font=("times new roman", 15, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5)
        txt_name = Entry(buyer_frame, textvariable=self.buyer_name, font=("times new roman", 13, "bold"), bg="lightyellow").grid(row=0, column=1, padx=10, pady=5)

        lbl_contact = Label(buyer_frame, text="Contact No:", font=("times new roman", 15, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=5)
        txt_contact = Entry(buyer_frame, textvariable=self.buyer_contact, font=("times new roman", 13, "bold"), bg="lightyellow").grid(row=1, column=1, padx=10, pady=5)

        # Product Details Frame
        product_frame = LabelFrame(self.root, text="Product Details", font=("times new roman", 15, "bold"), bg="white")
        product_frame.place(x=10, y=350, width=700, height=150)

        lbl_product_name = Label(product_frame, text="Product Name:", font=("times new roman", 15, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5)
        txt_product_name = Entry(product_frame, textvariable=self.product_name, font=("times new roman", 13, "bold"), bg="lightyellow").grid(row=0, column=1, padx=10, pady=5)

        lbl_product_quantity = Label(product_frame, text="Quantity:", font=("times new roman", 15, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=5)
        txt_product_quantity = Entry(product_frame, textvariable=self.product_quantity, font=("times new roman", 13, "bold"), bg="lightyellow").grid(row=1, column=1, padx=10, pady=5)

        btn_add_product = Button(product_frame, text="Add Product", command=self.add_product, font=("times new roman", 13, "bold"), bg="green", fg="white").grid(row=2, column=1, padx=10, pady=5)

        # Bill Area
        self.bill_area = Text(self.root, font=("times new roman", 15, "bold"), bg="lightyellow")
        self.bill_area.place(x=750, y=230, width=740, height=400)

        # Save Bill Button
        btn_save_bill = Button(self.root, text="Save Bill", command=self.save_bill, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        btn_save_bill.place(x=10, y=520, width=150, height=40)

        # Initialize Bill
        self.update_bill()

    def update_bill(self):
        self.bill_area.delete("1.0", END)
        self.bill_area.insert(END, "\t\t\tXYZ Store\n")
        self.bill_area.insert(END, "\t\t123 Market Street, City\n")
        self.bill_area.insert(END, "\t\tPhone: (123) 456-7890\n")
        self.bill_area.insert(END, "\t\t=====================\n\n")
        self.bill_area.insert(END, f"Buyer Name:\t{self.buyer_name.get()}\n")
        self.bill_area.insert(END, f"Contact No:\t{self.buyer_contact.get()}\n")
        self.bill_area.insert(END, "="*60 + "\n")
        self.bill_area.insert(END, f"{'Product':<20}{'Qty':<10}{'Price':<10}\n")
        self.bill_area.insert(END, "="*60 + "\n")
        
        for product in self.product_list:
            self.bill_area.insert(END, f"{product['name']:<20}{product['quantity']:<10}{product['price']:<10}\n")
        
        self.bill_area.insert(END, "="*60 + "\n")
        self.bill_area.insert(END, f"{'Total':<30}{self.total_amount.get():<10.2f}\n")
        self.bill_area.insert(END, "="*60 + "\n")

    def add_product(self):
        conn = sqlite3.connect('ims.db')
        cur = conn.cursor()
        cur.execute("SELECT price, quantity FROM products WHERE name=?", (self.product_name.get(),))
        result = cur.fetchone()
        if result:
            price, available_quantity = result
            quantity = self.product_quantity.get()
            if quantity > available_quantity:
                messagebox.showerror("Error", f"Only {available_quantity} items available in stock.")
            else:
                total_price = price * quantity
                self.total_amount.set(self.total_amount.get() + total_price)

                self.product_list.append({
                    'name': self.product_name.get(),
                    'quantity': quantity,
                    'price': total_price
                })

                # Update the quantity in the database
                new_quantity = available_quantity - quantity
                cur.execute("UPDATE products SET quantity=? WHERE name=?", (new_quantity, self.product_name.get()))
                conn.commit()

                self.update_bill()
        else:
            messagebox.showerror("Error", "Product not found in the inventory.")
        conn.close()

    def save_bill(self):
        self.update_bill()
        bill_content = self.bill_area.get("1.0", END)
        with open("bill.txt", "w") as f:
            f.write(bill_content)
        messagebox.showinfo("Saved", "Bill has been saved successfully!")

    def move_text(self):
        current_x = self.welcome_label.winfo_x()
        new_x = current_x + 2

        # Reset to start position when the text moves out of the window
        if new_x > self.root.winfo_width():
            new_x = -self.welcome_label.winfo_width()

        self.welcome_label.place(x=new_x, rely=0.5, anchor=W)
        self.root.after(20, self.move_text)  # Adjust the delay for smoothness

if __name__ == "__main__":
    root = Tk()
    obj = GeneratingPrintingBill(root)
    root.mainloop()
