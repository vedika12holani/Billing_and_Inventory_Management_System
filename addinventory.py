
from tkinter import *
from tkinter import font, ttk, messagebox
import sqlite3
from PIL import Image, ImageTk, ImageFilter

class AddProductToInventory:
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
        title_label = Label(title_frame, text="Inventory Manager", font=title_font, bg='#430808', fg='white')
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

        # Defining variables
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.var_nm = StringVar()
        self.var_pri = StringVar()
        self.var_qua = StringVar()
        self.var_sts = StringVar()

        self.var_searchby = StringVar()
        self.var_searchtct = StringVar()


        # First frame
        product_Frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        product_Frame.place(x=20, y=200, width=450, height=480)

        # Frame title
        title = Label(product_Frame, text="Manage Product Details", font=("times new roman", 20), bg="#4682B4", fg="white")
        title.pack(side=TOP, fill='x')

        lbl_category = Label(product_Frame, text="Category", font=("times new roman", 20), bg="white", fg="black")
        lbl_category.place(x=30, y=60)

        lbl_supplier = Label(product_Frame, text="Supplier", font=("times new roman", 20), bg="white", fg="black")
        lbl_supplier.place(x=30, y=110)

        lbl_name = Label(product_Frame, text="Name", font=("times new roman", 20), bg="white", fg="black")
        lbl_name.place(x=30, y=160)

        lbl_price = Label(product_Frame, text="Price", font=("times new roman", 20), bg="white", fg="black")
        lbl_price.place(x=30, y=210)

        lbl_quantity = Label(product_Frame, text="Quantity", font=("times new roman", 20), bg="white", fg="black")
        lbl_quantity.place(x=30, y=260)

        lbl_status = Label(product_Frame, text="Status", font=("times new roman", 20), bg="white", fg="black")
        lbl_status.place(x=30, y=310)

        # Entry fields
        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=("Select","Electronics","Grocery","Books","Essentials","Cosmetics"), state='readonly', justify=CENTER, font=("times new roman", 15))
        cmb_cat.place(x=150, y=60, width=200)
        cmb_cat.current(0)

        cmb_sup = ttk.Combobox(product_Frame, textvariable=self.var_sup, values=("Select","Dell","Intel","HP","D-mart","Big-Bazaar","The Penguin Publication","Crossword","Purple","Sugar"), state='readonly', justify=CENTER, font=("times new roman", 15))
        cmb_sup.place(x=150, y=110, width=200)
        cmb_sup.current(0)

        txt_nm = Entry(product_Frame, textvariable=self.var_nm, font=("times new roman", 15), bg="#a0d2eb")
        txt_nm.place(x=150, y=160, width=200)

        txt_pri = Entry(product_Frame, textvariable=self.var_pri, font=("times new roman", 15), bg="#a0d2eb")
        txt_pri.place(x=150, y=210, width=200)

        txt_qua = Entry(product_Frame, textvariable=self.var_qua, font=("times new roman", 15), bg="#a0d2eb")
        txt_qua.place(x=150, y=260, width=200)

        cmb_sts = ttk.Combobox(product_Frame, textvariable=self.var_sts, values=("Select","Refurbished","Packaged","Un-Packaged"), state='readonly', justify=CENTER, font=("times new roman", 15))
        cmb_sts.place(x=150, y=310, width=200)
        cmb_sts.current(0)

        # Buttons
        btn_add = Button(product_Frame, text="Save", command=self.add, font=("times new roman", 15), bg="#4682B4", fg="white", cursor="hand2")
        btn_add.place(x=10, y=400, width=100, height=40)
        btn_update = Button(product_Frame, text="Update",command=self.update, font=("times new roman", 15), bg="#4682B4", fg="white", cursor="hand2")
        btn_update.place(x=120, y=400, width=100, height=40)
        btn_delete = Button(product_Frame, text="Delete",command=self.delete, font=("times new roman", 15), bg="#4682B4", fg="white", cursor="hand2")
        btn_delete.place(x=230, y=400, width=100, height=40)
        btn_clear = Button(product_Frame, text="Clear", command=self.clear,
        font=("times new roman", 15), bg="#4682B4", fg="white", cursor="hand2")
        btn_clear.place(x=340, y=400, width=100, height=40)


        # Search bar
        SearchFrame = LabelFrame(self.root, text="Search Product", font=("times new roman", 12, "bold"), bd=3, relief=RIDGE, bg="white")
        SearchFrame.place(x=680, y=200, width=600, height=80)

        # Search criteria dropdown
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Name", "Category", "Supplier"), state='readonly', justify=CENTER, font=("times new roman", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)  # Set default value to "Select"

    # Search input field
        txt_search = Entry(SearchFrame, textvariable=self.var_searchtct, font=("times new roman", 15), bg="#a0d2eb")
        txt_search.place(x=200, y=10)


        # Search button
        btn_search = Button(SearchFrame, text="Search", command=self.search, font=("times new roman", 15), bg="#4682B4", fg="white", cursor="hand2")
        btn_search.place(x=410, y=9, width=150, height=30)

        # Database display frame
        data_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        data_frame.place(x=500, y=300, width=970, height=370)

        # Scrollbar
        scroll_x = Scrollbar(data_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(data_frame, orient=VERTICAL)
        self.product_table = ttk.Treeview(data_frame, columns=("category", "supplier", "name", "price", "quantity", "status"),
                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.product_table.xview)
        scroll_y.config(command=self.product_table.yview)

        self.product_table.heading("category", text="Category")
        self.product_table.heading("supplier", text="Supplier")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("quantity", text="Quantity")
        self.product_table.heading("status", text="Status")

        self.product_table['show'] = 'headings'
        self.product_table.pack(fill=BOTH, expand=1)

        # Call function to display all records initially
        self.display_data()

        # Add clear button
        btn_clear_product = Button(self.root, text="Clear", command=self.display_data, font=("times new roman", 15), bg="#4682B4", fg="white", cursor="hand2")
        btn_clear_product.place(x=1200, y=680, width=200, height=40)

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

        if new_x > self.root.winfo_width():
            new_x = -self.welcome_label.winfo_width()

        self.welcome_label.place(x=new_x, rely=0.5, anchor=W)
        self.root.after(20, self.move_text)

    def add(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_nm.get() == "" or self.var_pri.get() == "" or self.var_qua.get() == "":
                messagebox.showerror("Error", "Name, Price, and Quantity are required", parent=self.root)
            else:
                query = "INSERT INTO products (category, supplier, name, price, quantity, status) VALUES (?, ?, ?, ?, ?, ?)"
                data = (self.var_cat.get(), self.var_sup.get(), self.var_nm.get(), self.var_pri.get(), self.var_qua.get(), self.var_sts.get())
                cur.execute(query, data)
                con.commit()
                messagebox.showinfo("Success", "Product added successfully", parent=self.root)
                self.display_data()

                self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    def update(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_nm.get() == "" or self.var_pri.get() == "" or self.var_qua.get() == "":
                messagebox.showerror("Error", "Name, Price, and Quantity are required", parent=self.root)
            else:
            # Update the product details
                query = "UPDATE products SET category=?, supplier=?, price=?, quantity=?, status=? WHERE name=?"
                data = (self.var_cat.get(), self.var_sup.get(), self.var_pri.get(), self.var_qua.get(), self.var_sts.get(), self.var_nm.get())
                cur.execute(query, data)
                con.commit()
                messagebox.showinfo("Success", "Product updated successfully", parent=self.root)
                self.display_data()
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def delete(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_nm.get() == "":
                messagebox.showerror("Error", "Please enter the Name to delete", parent=self.root)
            else:
                # Check if the product exists
                cur.execute("SELECT * FROM products WHERE name=?", (self.var_nm.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", f"No product found with name '{self.var_nm.get()}'", parent=self.root)
                else:
                    # Confirm deletion
                    confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{self.var_nm.get()}'?", parent=self.root)
                    if confirm:
                        # Delete the product
                        query = "DELETE FROM products WHERE name=?"
                        cur.execute(query, (self.var_nm.get(),))
                        con.commit()
                        messagebox.showinfo("Success", f"Product '{self.var_nm.get()}' deleted successfully", parent=self.root)
                        self.display_data()
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
        self.var_cat.set("select")
        self.var_sup.set("select")
        self.var_nm.set("")
        self.var_pri.set("")
        self.var_qua.set("")
        self.var_sts.set("Active")
    


    def search(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            selected_search = self.var_searchby.get()  # Get selected search criteria from combobox
            search_term = self.var_searchtct.get().strip()  # Get search term from entry field and strip whitespace

            if selected_search == "Select":
                messagebox.showerror("Error", "Please select a search criteria", parent=self.root)
            elif not search_term:  # Check if search term is empty or only whitespace
                messagebox.showerror("Error", "Please enter a search term", parent=self.root)
            else:
                # Initialize query variable
                query = ""

                # Construct query based on selected search criteria
                if selected_search == "Name":
                    query = "SELECT category, supplier, name, price, quantity, status FROM products WHERE name LIKE ?"
                elif selected_search == "Category":
                    query = "SELECT category, supplier, name, price, quantity, status FROM products WHERE category LIKE ?"
                elif selected_search == "Supplier":
                    query = "SELECT category, supplier, name, price, quantity, status FROM products WHERE supplier LIKE ?"

                # Check if query is not empty
                if query:
                    # Execute query with wildcard search (using %)
                    cur.execute(query, ('%' + search_term + '%',))
                    rows = cur.fetchall()

                    # Clear previous table data
                    self.product_table.delete(*self.product_table.get_children())

                    if not rows:
                        messagebox.showinfo("Info", "No matching records found", parent=self.root)
                    else:
                        # Insert fetched data into table
                        for row in rows:
                            self.product_table.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error during search: {str(ex)}", parent=self.root)
        finally:
            con.close()

    
    def display_data(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            query = "SELECT category, supplier, name, price, quantity, status FROM products"
            cur.execute(query)
            rows = cur.fetchall()

            # Clear previous table data
            self.product_table.delete(*self.product_table.get_children())

            if not rows:
                messagebox.showinfo("Info", "No records found", parent=self.root)
            else:
                # Insert fetched data into table
                for row in rows:
                    self.product_table.insert('', END, values=row)

        except sqlite3.Error as ex:
            messagebox.showerror("SQLite Error", f"SQLite error: {str(ex)}", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching data: {str(ex)}", parent=self.root)
        finally:
            con.close()



if __name__ == "__main__":
    root = Tk()
    obj = AddProductToInventory(root)
    root.mainloop()

