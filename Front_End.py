from tkinter import *

import random
from tkinter import messagebox
import tkinter as tk
import tkinter.font as font
from tkinter import ttk
import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Dbms1234$",
    database="SSM"
)
cursor = db.cursor()

root=Tk()
root.geometry("750x750")
root.configure(bg="yellow")
img=PhotoImage(file="Image_1.png")
label=Label(root,image=img)
label.place(x=0,y=0)

myFont = font.Font(size=10)
MMFont = font.Font(size=15)
MyFont = font.Font(size=30)
l1=Label(root,text="SENSEX MANAGEMENT",fg="black")
l1.place(x=150,y=100)
l1['font'] = MyFont

import tkinter as tk
from tkinter import ttk
import mysql.connector

# Function to add data to the user and login_details tables
def new_stock():
    nw1=Toplevel(root)
    nw1.configure(bg="blue")
    nw1.title("New stock details")
    nw1.geometry("1366x1366")
    img=PhotoImage(file="Image_2.png")
    label=Label(nw1,image=img,bd=0)
    label.image=img
    label.place(x=0,y=0)



    '''
    nw1=Toplevel(root)
    nw1.title("GAME OPTIONS")
    nw1.geometry("750x750")
    
    img=PhotoImage(file="1p2p.png")
    label=Label(nw1,image=img)
    label.image=img
    label.place(x=0,y=0)
    '''


    def execute_query(query):
        try:
            cursor.execute(query)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Error: {e}")
            return False

    # Create a function to update the treeview widget with the data from the database
    def update_treeview():
        for i in treeview.get_children():
            treeview.delete(i)
        data = fetch_data()
        for record in data:
            treeview.insert('', 'end', values=record)

    # Create a function to fetch data from the database
    def fetch_data():
        query = "SELECT * FROM stock_info"
        cursor.execute(query)
        data = cursor.fetchall()
        return data

    
    # Create a function to handle the "Add" button click
    def add_record():
        stock_id = stock_id_entry.get()
        date_time = date_time_entry.get()
        change_abs = change_abs_entry.get()
        perf = perf_entry.get()
        price=price_entry.get()
        query = f"INSERT INTO stock_info(stock_id, date_time, change_abs, perf,price) VALUES('{stock_id}', '{date_time}', {change_abs}, '{perf}','{price}')"
        if execute_query(query):
            update_treeview()
        else:
            messagebox.showerror("Error", "Failed to insert record. Check for duplicate stock_id.")

    # Create a function to handle the "Update" button click
    def update_record():
        stock_id = stock_id_entry.get()
        date_time = date_time_entry.get()
        change_abs = change_abs_entry.get()
        perf = perf_entry.get()
        query = f"UPDATE stock_info SET date_time = '{date_time}', change_abs = {change_abs}, perf = '{perf}' WHERE stock_id = '{stock_id}'"
        if execute_query(query):
            update_treeview()

    # Create a function to handle the "Delete" button click
    def delete_record():
        stock_id = stock_id_entry.get()
        query = f"DELETE FROM stock_info WHERE stock_id = '{stock_id}'"
        if execute_query(query):
            update_treeview()
            
    def get_stock_count():
        query = "SELECT COUNT(*) FROM stock_info"
        cursor.execute(query)
        result = cursor.fetchone()[0]  # Fetch the result using fetchone
        print(result)
        return result
        if result is not None:
            return result
        else:
            return None
        
    def show_stock_count():
        count = get_stock_count()
        if count is not None:
            messagebox.showinfo("Stock Count", f"Total Stocks: {count}")
        else:
            messagebox.showerror("Error", "Failed to retrieve stock count.")

    # Create a LabelFrame for data entry
    data_frame = ttk.LabelFrame(nw1, text="Data Entry")
    data_frame.grid(row=0, column=0, padx=10, pady=10)

    # Create data entry fields
    stock_id_label = tk.Label(nw1, text="Stock ID:")
    stock_id_label.place(x=10,y=70)
    stock_id_entry = tk.Entry(nw1)
    stock_id_entry.place(x=130,y=70)

    date_time_label = tk.Label(nw1, text="Date Time:")
    date_time_label.place(x=10,y=100)
    date_time_entry = tk.Entry(nw1)
    date_time_entry.place(x=130,y=100)

    change_abs_label = tk.Label(nw1, text="Change Abs:")
    change_abs_label.place(x=10,y=130)
    change_abs_entry = tk.Entry(nw1)
    change_abs_entry.place(x=130,y=130)

    perf_label = tk.Label(nw1, text="Performance:")
    perf_label.place(x=10,y=160)
    perf_entry = tk.Entry(nw1)
    perf_entry.place(x=130,y=160)

    price_label = tk.Label(nw1, text="Price:")
    price_label.place(x=10,y=190)
    price_entry = tk.Entry(nw1)
    price_entry.place(x=130,y=190)

    # Create buttons for CRUD operations
    add_button = tk.Button(nw1, text="Add", command=add_record)
    add_button.place(x=10,y=220)
    
    update_button = tk.Button(nw1, text="Update", command=update_record)
    update_button.place(x=90,y=220)

    delete_button = tk.Button(nw1, text="Delete", command=delete_record)
    delete_button.place(x=170,y=220)

    show_count_button = tk.Button(nw1, text="Show Stock Count", command=show_stock_count)
    show_count_button.place(x=220,y=220)

    # Create a treeview widget to display data
    treeview = ttk.Treeview(nw1, columns=("Stock ID", "Date Time", "Change Abs", "Performance","Price"))
    treeview.heading("#1", text="Stock ID")
    treeview.heading("#2", text="Date Time")
    treeview.heading("#3", text="Change Abs")
    treeview.heading("#4", text="Performance")
    treeview.heading("#5", text="Price")
    treeview.grid(row=1, column=0, padx=0, pady=280)

    # Populate the treeview with data
    update_treeview()

b1=Button(root,text="NEW STOCKS",command=lambda:new_stock())
b1.place(x=200,y=300)
b1['font'] = MMFont


# Function to add data to the user and login_details tables
def add_user_and_login():
    nw2=Toplevel(root)
    nw2.configure(bg="black")
    nw2.title("New user details")
    nw2.geometry("1366x1366")
    img=PhotoImage(file="Image_2.png")
    label=Label(nw2,image=img,bd=0)
    label.image=img
    label.place(x=0,y=0)


    def execute_query(query):
        try:
            cursor.execute(query)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Error: {e}")
            return False
            
    # Create a function to update the treeview widget with the data from the database
    def update_treeview():
        for i in treeview.get_children():
            treeview.delete(i)
        data = fetch_data()
        for record in data:
            treeview.insert('', 'end', values=record)

    # Create a function to fetch data from the database
    def fetch_data():
        query = "SELECT * FROM user"
        cursor.execute(query)
        data = cursor.fetchall()
        return data

    def add_user_record():
        # Get user input from tkinter Entry widgets
        email_id = email_id_entry.get()
        f_name = f_name_entry.get()
        l_name = l_name_entry.get()
        gender = gender_var.get()
        dob = dob_entry.get()
        password = password_entry.get()
        balance_amt=balance_amt_entry.get()
        login_id=login_id_entry.get()

        
        user_insert_query = f"INSERT INTO user (email_id, f_name, l_name, gender, dob, balance_amt,stocks) VALUES ('{email_id}', '{f_name}', '{l_name}', '{gender}', '{dob}','{balance_amt}','NULL')"
        if execute_query(user_insert_query):
            update_treeview()
            
        # SQL query to insert data into the login_details table
        login_insert_query = f"INSERT INTO login_details (email_id, password, status, login_id) VALUES ('{email_id}', '{password}', 'A','{login_id}')"
        if execute_query(login_insert_query):
            update_treeview()
    
   
    def update_user_record():
        # Get user input from tkinter Entry widgets
        email_id = email_id_entry.get()
        f_name = f_name_entry.get()
        l_name = l_name_entry.get()
        gender = gender_var.get()
        dob = dob_entry.get()
        password = password_entry.get()
        balance_amt=balance_amt_entry.get()
        login_id=login_id_entry.get()

        # SQL query to update data in the user table
        user_update_query = f"UPDATE user SET f_name = '{f_name}', l_name = '{l_name}', gender = '{gender}', dob = '{dob}',balance_amt = '{balance_amt}' WHERE email_id = '{email_id}'"


        if execute_query(user_update_query):
            update_treeview()
            

    def delete_user_record():
        # Get user input from tkinter Entry widgets
        email_id = email_id_entry.get()

        # SQL query to delete a user record from the user and login_details tables
        user_delete_query = f"DELETE FROM user WHERE email_id = '{email_id}'"
        login_delete_query = f"DELETE FROM login_details WHERE email_id = '{email_id}'"

        if execute_query(user_delete_query):
            update_treeview()
        if execute_query(login_delete_query):
            update_treeview()
        

    # Create a LabelFrame for data entry
    data_frame = ttk.LabelFrame(nw2, text="Data Entry")
    data_frame.grid(row=0, column=0, padx=10, pady=10)

    # Create data entry fields
    email_id_label = tk.Label(nw2, text="Email ID:")
    email_id_label.place(x=10,y=50)
    email_id_entry = tk.Entry(nw2)
    email_id_entry.place(x=130,y=50)

    f_name_label = tk.Label(nw2, text="First Name:")
    f_name_label.place(x=10,y=100)
    f_name_entry = tk.Entry(nw2)
    f_name_entry.place(x=130,y=100)

    l_name_label = tk.Label(nw2, text="Last Name:")
    l_name_label.place(x=10,y=130)
    l_name_entry = tk.Entry(nw2)
    l_name_entry.place(x=130,y=130)

    gender_label = tk.Label(nw2, text="Gender:")
    gender_label.place(x=10,y=160)
    gender_var = tk.StringVar()
    gender_combo = ttk.Combobox(nw2, textvariable=gender_var, values=["M", "F"])
    gender_combo.place(x=130,y=160)

    dob_label = tk.Label(nw2, text="Date of Birth:")
    dob_label.place(x=10,y=190)
    dob_entry = tk.Entry(nw2)
    dob_entry.place(x=130,y=190)

    password_label = tk.Label(nw2, text="Password:")
    password_label.place(x=10,y=220)
    password_entry = tk.Entry(nw2, show="*")
    password_entry.place(x=130,y=220)

    login_id_label = tk.Label(nw2, text="Login_ID:")
    login_id_label.place(x=10,y=250)
    login_id_entry = tk.Entry(nw2)
    login_id_entry.place(x=130,y=250)

    balance_amt_label = tk.Label(nw2, text="Wallet:")
    balance_amt_label.place(x=10,y=280)
    balance_amt_entry = tk.Entry(nw2)
    balance_amt_entry.place(x=130,y=280)
    
    # Create buttons for CRUD operations
    add_button = tk.Button(nw2, text="Add", command=add_user_record)
    add_button.place(x=10,y=320)
    
    update_button = tk.Button(nw2, text="Update", command=update_user_record)
    update_button.place(x=50,y=320)

    delete_button = tk.Button(nw2, text="Delete", command=delete_user_record)
    delete_button.place(x=140,y=320)

    # Create a treeview widget to display data
    treeview = ttk.Treeview(nw2, columns=("Email_id","First Name","Last Name","Gender","DOB","Balance Amount"))
    treeview.heading("#1", text="Email_id")
    treeview.heading("#2", text="First Name")
    treeview.heading("#3", text="Last Name")
    treeview.heading("#4", text="Gender")
    treeview.heading("#5", text="DOB")
    treeview.heading("#6", text="Balance Amount")
    

    treeview.grid(row=1, column=0, padx=0, pady=400)

    # Populate the treeview with data
    update_treeview()

b2=Button(root,text="NEW USER",command=lambda:add_user_and_login())
b2.place(x=500,y=300)
b2['font'] = MMFont


def buy_sell():
    nw3=Toplevel(root)
    nw3.configure(bg="black")
    nw3.title("Purchase details")
    nw3.geometry("1366x1366")
    img=PhotoImage(file="Image_2.png")
    label=Label(nw3,image=img,bd=0)
    label.image=img
    label.place(x=0,y=0)

    l1=Label(nw3,text="STOCK PURCHASE",fg="black")
    l1.place(x=0,y=20)
    l1['font'] = MyFont

    l1=Label(nw3,text="General View",fg="black")
    l1.place(x=0,y=350)
    l1['font'] = MyFont

    img2=PhotoImage(file="buy_sell.png")
    label2=Label(nw3,image=img2)
    label2.image=img2
    label2.place(x=400,y=0)
                 
    def execute_query(query):
        try:
            cursor.execute(query)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Error: {e}")
            return False
        
    def update_treeview():
        for i in treeview.get_children():
            treeview.delete(i)
        data = fetch_data()
        for record in data:
            treeview.insert('', 'end', values=record)

    # Create a function to fetch data from the database
    def fetch_data():
        query = "SELECT * FROM user_stocks"
        cursor.execute(query)
        data = cursor.fetchall()
        return data
        
    def buy_stock():
        email_id = email_id_entry.get()
        stock_id = stock_id_entry.get()

        # Check if the user and stock exist
        query_check = f"SELECT * FROM stock_info WHERE stock_id = '{stock_id}'"
        cursor.execute(query_check)
        data = cursor.fetchall()
        print(data)

        # Check if the user has enough balance
        query = f"SELECT balance_amt FROM user WHERE email_id = '{email_id}'"
        cursor.execute(query)
        new = cursor.fetchone()[0]
        print(new)
        balance = int(new)
        if balance is None:
            messagebox.showerror("Error", "Invalid user.")
            return

        # Get the stock price
        query_price = f"SELECT price FROM stock_info WHERE stock_id = '{stock_id}'"
        cursor.execute(query_price)
        result = cursor.fetchone()

        if result is not None:
            stock_price = int(result[0])
            print(f"Stock Price: {stock_price}")
        else:
            print(f"Error: Stock with stock_id {stock_id} not found.")

        # Buy the stock
        new_balance = balance - stock_price
        print(new_balance)
        if new_balance < 0:
            messagebox.showerror("Error", "Insufficient balance.")
            return

        # Update user balance
        if update_user_balance(email_id, new_balance):
            # Add the stock to user_stocks table
            query_buy_stock = f"INSERT INTO user_stocks (email_id, stock_id) VALUES ('{email_id}', '{stock_id}')"
            if execute_query(query_buy_stock):
                messagebox.showinfo("Success", f"Stock {stock_id} bought successfully.\nNew Balance: {new_balance}")
                update_treeview()
            else:
                messagebox.showerror("Error", "Failed to buy stock.")
        else:
            messagebox.showerror("Error", "Failed to update user balance.")
            
    treeview = ttk.Treeview(nw3, columns=("Email ID", "Stock ID","Price"))
    treeview.heading("#0", text="Index")
    treeview.heading("#1", text="Email ID")
    treeview.heading("#2", text="Stock ID")
    treeview.heading("#3", text="Price")
    treeview.grid(row=1, column=0, padx=0, pady=450)

    # Populate the treeview with data
    update_treeview()

    def sell_stock():
        email_id = email_id_entry.get()
        stock_id = stock_id_entry.get()

        # Check if the user and stock exist
        query_check = f"SELECT * FROM stock_info WHERE stock_id = '{stock_id}'"
        cursor.execute(query_check)
        data = cursor.fetchall()
        print(data)
        
        # Check if the user has the stock
        query_stock_count = f"SELECT COUNT(*) FROM user_stocks WHERE email_id = '{email_id}' AND stock_id = '{stock_id}'"
        cursor.execute(query_stock_count)
        new = cursor.fetchone()[0]
        print(new)
        stock_count = int(new)
        
        #stock_count = execute_query(query_stock_count)[0][0]
        if stock_count == 0:
            messagebox.showerror("Error", "User does not own this stock.")
            return

        # Get the stock price
        query_price = f"SELECT price FROM stock_info WHERE stock_id = '{stock_id}'"
        cursor.execute(query_price)
        hell = cursor.fetchone()[0]
        print("Stock price is", hell)

        # Get user balance
        balance = get_user_balance_amt(email_id)

        # Sell the stock
        new_balance = int(balance) + int(hell)

        # Update user balance
        if update_user_balance(email_id, new_balance):
            # Remove one stock from user_stocks table
            query_sell_stock = f"DELETE FROM user_stocks WHERE email_id = '{email_id}' AND stock_id = '{stock_id}' LIMIT 1"
            if execute_query(query_sell_stock):
                messagebox.showinfo("Success", f"Stock {stock_id} sold successfully.\nNew Balance: {new_balance}")
                update_treeview()
            else:
                messagebox.showerror("Error", "Failed to sell stock.")
        else:
            messagebox.showerror("Error", "Failed to update user balance.")

    def get_user_balance_amt(user):
        user_email = email_id_entry.get()
        query = f"SELECT balance_amt FROM user WHERE email_id = '{user_email}'"
        cursor.execute(query)
        data = cursor.fetchone()[0]
        print(data)
        if data:
            return data
        else:
            return None

    def update_user_balance(user, new_balance):
        user_email = email_id_entry.get()
        query = f"UPDATE user SET balance_amt = {new_balance} WHERE email_id = '{user_email}'"
        cursor.execute(query)
        return True

    # Create buttons for buying and selling stocks

    email_id_label = tk.Label(nw3, text="User email id:")
    email_id_label.place(x=10,y=150)
    email_id_entry = tk.Entry(nw3)
    email_id_entry.place(x=100,y=150)


    stock_id_label = tk.Label(nw3, text="Stock ID:")
    stock_id_label.place(x=10,y=200)
    stock_id_entry = tk.Entry(nw3)
    stock_id_entry.place(x=100,y=200)


    buy_button = Button(nw3, text="Buy Stock", command=buy_stock)
    buy_button.place(x=10, y=300)

    sell_button = Button(nw3, text="Sell Stock", command=sell_stock)
    sell_button.place(x=120, y=300)


    def get_stock_data(stock_id):
        query = f"SELECT stock_id, balance_amt FROM stock_info WHERE stock_id = '{stock_id}'"
        result = execute_query(query)

        return result if result else None

    def show_balance():
        stock_id = stock_id_entry.get()

        if not stock_id:
            messagebox.showerror("Error", "Please enter a valid Stock ID.")
            return

        stock_data = get_stock_data(stock_id)

        if stock_data:
            # Clear existing items in the Treeview
            for item in treeview.get_children():
                treeview.delete(item)

            # Populate the Treeview with stock data
            for data in stock_data:
                treeview.insert("", "end", values=data)
        else:
            messagebox.showerror("Error", f"Failed to retrieve data for Stock ID: {stock_id}")

    '''
    def display_user_specific_data(email_id):
        #email_id = email_id_entry.get()
        query = "SELECT stock_id,price FROM user_stocks WHERE email_id = '{email_id}'"
        cursor.execute(query)
        hell = cursor.fetchall()
        print(hell)

        result_window = tk.Toplevel(root)
        result_window.title("User-Specific Data")

        treeview = ttk.Treeview(result_window, columns=("Stock ID", "Email ID", "Price"))
        treeview.heading("#0", text="Index")
        treeview.heading("#1", text="Stock ID")
        treeview.heading("#2", text="Email ID")
        treeview.heading("#3", text="Price")
        update_treeview()

        # Create an entry widget to input user email ID
        email_entry = tk.Entry(root)
        email_entry.pack(pady=10)

        # Create a button to display user-specific data
        display_button = tk.Button(root, text="Display User-Specific Data", command=lambda: display_user_specific_data(email_entry.get()))
        display_button.pack(pady=10)

        # Create an exit button
        exit_button = tk.Button(root, text="Exit", command=root.destroy)
        exit_button.pack(pady=10)

def execute_stored_procedure(email_id, stock_id):
        # Call the stored procedure
        query=f"CALL CalculateStockCost('{email_id}','{stock_id'});"
        #cursor.callproc('CalculateStockCost', (email_id, stock_id))

        # Fetch the result
        result = cursor.fetchone()[0]
        prnt(result)

        cursor.execute(query_check)
        data = cursor.fetchall()
        print(data)

        # Display the result in a Tkinter window
        display_result(result)

def display_result(result):
    total_cost = result[0]
    messagebox.showinfo("Total Cost", f"The total cost of the stock is: ${total_cost}")

# Create the Tkinter root window
root = tk.Tk()
root.title("Calculate Stock Cost Example")

# Create entry widgets to input user email ID and stock ID
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=10, padx=10)
stock_id_entry = tk.Entry(root, width=10)
stock_id_entry.pack(pady=10, padx=10)

# Create a button to calculate stock cost
calculate_button = tk.Button(root, text="Calculate Stock Cost", command=lambda: execute_stored_procedure(email_entry.get(), stock_id_entry.get()))
calculate_button.pack(pady=10)

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=10)
'''

b3=Button(root,text="STOCK PURCHASE",command=lambda:buy_sell())
b3.place(x=300,y=500)
b3['font'] = MMFont


import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk


def draw_bar_chart():

    def execute_query(query):
        try:
            cursor.execute(query)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Error: {e}")
            return False
        
    # SQL query to fetch data from the database
    query = "SELECT stock_id FROM sensex_val"
    result = cursor.execute(query)
    hell = cursor.fetchall()
    print(hell)

    flat_list_ids = [item[0] for item in hell]
    print(flat_list_ids)


    query = "SELECT sensex_per FROM sensex_val"
    result = cursor.execute(query)
    hell2 = cursor.fetchall()
    print(hell2)

    flat_list_per = [item[0] for item in hell2]
    print(flat_list_per)
    

        # Create a figure
    fig = Figure(figsize=(6, 4), dpi=100)
        
        # Add a subplot
    ax = fig.add_subplot(111)

        # Plotting the bar chart
    ax.bar(flat_list_ids, flat_list_per, color='skyblue')

        # Create a Tkinter canvas to embed the matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Add labels and title
    ax.set_xlabel('Stock ID')
    ax.set_ylabel('Sensex Percentage')
    ax.set_title('Sensex Percentage Bar Chart')

        # Show the bar chart
    canvas.draw()


# Create a button to draw the bar chart
draw_button = tk.Button(root, text="VIEW STOCKS", command=draw_bar_chart)
draw_button.place(x=350,y=600)


# Run the Tkinter event loop
