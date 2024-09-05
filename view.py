import tkinter as tk
import datetime
from tkinter import messagebox
from CompanyController import CompanyController

company = CompanyController()

def btnGetAllCustomer():
    """Display a list of all customers."""
    all_customers = company.allCustomer
    customer_info = "\n".join(str(customer) for customer in all_customers)
    messagebox.showinfo("Customer List", customer_info)
def btnGetAllOrders():
    # 모든 주문을 문자열로 변환
    all_orders_str = '\n\n'.join(str(order) for order in company.currentOrder)
    
    # 정보 표시
    if all_orders_str:
        messagebox.showinfo("Order List", all_orders_str)
    else:
        messagebox.showinfo("Order List", "No orders found.")
def btnGetCustomerOrder():
    customer_name = selected_customer.get()
    if customer_name == "Choose":
        messagebox.showwarning("Customer Selection Required", "Please select a customer before proceeding.")
        return
    orders = company.selected_customer_orders(customer_name)
    if isinstance(orders, str):  # Check if the result is a string
        messagebox.showinfo("Order List", orders)
    else:
        if orders:
            list_customer_order = '\n\n'.join(str(order) for order in orders)
            messagebox.showinfo("Order List", f"{customer_name}'s orders:\n{list_customer_order}")
        else:
            messagebox.showinfo("Payment List", f"{customer_name}'s orders: No order found.")
def btnGetCustomerPayment():
    customer_name = selected_customer.get()
    if customer_name == "Choose":
        messagebox.showwarning("Customer Selection Required", "Please select a customer before proceeding.")
        return
    payments = company.selected_customer_payment(customer_name)
    if isinstance(payments, str):  # Check if the result is a string
        messagebox.showinfo("Payment List", payments)
    else:
        if payments:
            list_customer_payment = '\n\n'.join(str(order) for order in payments)
            messagebox.showinfo("Payment List", f"{customer_name}'s Payment:\n{list_customer_payment}")
        else :
            messagebox.showinfo("Payment List", f"{customer_name}'s Payment: No payment found.")
def update_customer_info(customer):
    """Update the customer info display"""
    customer_info_display.config(state=tk.NORMAL)
    customer_info_display.delete(1.0, tk.END)
    customer_info_display.insert(tk.END, str(customer))
    customer_info_display.config(state=tk.DISABLED)
def customerSelected(*args):
    """Display selected customer's details."""
    customer_name = selected_customer.get()
    customer = company.get_single_customer(customer_name) # get customer info by name
    if customer:
        customer.addUpdate(update_customer_info)  # 옵저버 추가
        update_customer_info(customer)
    else:
        customer_info_display.config(state=tk.NORMAL)
        customer_info_display.delete(1.0, tk.END)
        customer_info_display.insert(tk.END, "No customer selected")
        customer_info_display.config(state=tk.DISABLED)

def added_product_list():
    """Add selected product to the order and update order details display."""
    customer = selected_customer.get()
    qty = quantity_entry.get()
    product_name = selected_product.get()
    if customer == "Choose":
        messagebox.showwarning("Customer Selection Required", "Please select a customer before proceeding.")
        return
    elif product_name == "Choose":
        messagebox.showwarning("Product Selection Required", "Please select a product before proceeding.")
        return
    elif not qty.isdigit():
        messagebox.showwarning("Invalid Input", "Quantity must be a number.")
        return
    company.add_product(product_name, qty)
    detail = company.added_product_list
    order_details_display.config(state=tk.NORMAL)
    order_details_display.delete(1.0, tk.END)
    total = 0
    for item in detail:
        product, item_qty, subtotal = item
        total += subtotal
        order_details_display.insert(tk.END, f"{product} X {item_qty} = ${subtotal:.2f}\n")
    order_details_display.insert(tk.END, f"====================\nTotal: ${total:.2f}")
    order_details_display.config(state=tk.DISABLED)
    quantity_entry.delete(0, 'end')
    selected_product.set(products[0])

def btn_place_order():
    """Place a new order and reset the order details."""
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    selectCustomer = selected_customer.get()
    company.place_order(selectCustomer,date)
    order_details_display.config(state=tk.NORMAL)
    order_details_display.delete(1.0, tk.END)
    order_details_display.insert(tk.END, "Order placed successfully.")
    order_details_display.config(state=tk.DISABLED)

def btn_process_payment():
    """Process the payment with the entered amount."""
    amount = payment_amount_entry.get()
    customer_name = selected_customer.get()

    if customer_name == "Choose":
        messagebox.showwarning("Customer Selection Required", "Please select a customer before proceeding.")
        return
    elif not amount.isdigit():
        messagebox.showwarning("Invalid Input", "Quantity must be a number.")
        return
    else:
        type,message = company.process_payment(amount, customer_name)
        if type == "success":
            messagebox.showinfo("Payment Success", message)
        else:
            messagebox.showinfo("Payment Failed", message)
  
        payment_amount_entry.delete(0, 'end')
        
def btn_all_payment():
    # Retrieve all payments information
    all_payments_info = company.get_all_payments()
    
    # Check if there are payments to display
    if all_payments_info:
        # Create a message to display all payments
        payment_details = "\n".join(all_payments_info)
        messagebox.showinfo("All Payments", payment_details)
    else:
        # Notify the user if there are no payments
        messagebox.showinfo("All Payments", "No payments available.")

       
root = tk.Tk() 
root.title("Lincoln Office Supplies Order App by Seunguk Hong")

# Center the window
root.minsize(1000, 1000)
root.maxsize(1100, 1100)
root.columnconfigure(0, weight=1)

# Main title label
mainTitle = tk.Label(root, text="Lincoln Office Supplies", width=30, height=2)
mainTitle.pack(fill=tk.X, padx=10, pady=10)

# Customer section
customer_info_section = tk.LabelFrame(root, text="Customer Informations", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, relief=tk.RAISED)
customer_info_section.pack(pady=20, padx=20, fill=tk.X)
customer_frame = tk.Frame(customer_info_section)
customer_frame.pack(fill=tk.X)

selectCustomer = tk.Label(customer_frame, text="Select Customer:")
selectCustomer.pack(side=tk.LEFT, padx=5)
customerNames = company.get_customer_names() # Get customer names from CompanyController
customers = ["Choose"] + customerNames
selected_customer = tk.StringVar(root)
selected_customer.set(customers[0])

customer_dropdown = tk.OptionMenu(customer_frame, selected_customer, *customers)
customer_dropdown.pack(side=tk.LEFT, padx=5)
selected_customer.trace("w", customerSelected)

customer_info_display = tk.Text(customer_frame, bg="blue", fg="white", height=5, width=50)
customer_info_display.insert(tk.END, "empty")
customer_info_display.config(state=tk.DISABLED)
customer_info_display.pack(side=tk.LEFT, padx=5)

# Process order section
process_order_section = tk.LabelFrame(root, text="Process Order", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, relief=tk.RAISED)
process_order_section.pack(pady=20, padx=20, fill=tk.X)
process_frame = tk.Frame(process_order_section)
process_frame.pack(fill=tk.X)

selectProduct = tk.Label(process_frame, text="Select Product:")
selectProduct.pack(side=tk.LEFT, padx=5)

productList = [product.product_name for product in company.productList]
products = ["Choose"] + productList
selected_product = tk.StringVar(root)
selected_product.set(products[0])

product_dropdown = tk.OptionMenu(process_frame, selected_product, *products)
product_dropdown.pack(side=tk.LEFT, padx=5)

quantity_entry_Label = tk.Label(process_frame, text="Quantity: ")
quantity_entry_Label.pack(side=tk.LEFT, padx=5)
quantity_entry = tk.Entry(process_frame, width=50)
quantity_entry.pack(side=tk.LEFT, padx=5)

add_product_button = tk.Button(process_frame, text="Add Product", command=added_product_list)
add_product_button.pack(side=tk.RIGHT, padx=5)

# Order Detail section
order_details_section = tk.LabelFrame(root, text="Order Details", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, relief=tk.RAISED)
order_details_section.pack(pady=20, padx=20, fill=tk.X)
order_details_frame = tk.Frame(order_details_section)
order_details_frame.pack(fill=tk.X)

order_details_display = tk.Text(order_details_frame, bg="blue", fg="white", height=10, width=50)
order_details_display.insert(tk.END, "empty")
order_details_display.config(state=tk.DISABLED)
order_details_display.pack(side=tk.LEFT, padx=5)

new_order_button = tk.Button(order_details_frame, text="Place Order", command=btn_place_order)
new_order_button.pack(side=tk.RIGHT, padx=5)

# Payment Process section
process_payment_section = tk.LabelFrame(root, text="Process Payment", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, relief=tk.RAISED)
process_payment_section.pack(pady=20, padx=20, fill=tk.X)
process_payment_frame = tk.Frame(process_payment_section)
process_payment_frame.pack(fill=tk.X)

payment_amount_label = tk.Label(process_payment_frame, text="Amount: ")
payment_amount_label.pack(side=tk.LEFT, padx=5)
payment_amount_entry = tk.Entry(process_payment_frame, width=50)
payment_amount_entry.pack(side=tk.LEFT, padx=5)

process_payment_button = tk.Button(process_payment_frame, text="Process Payment", command=btn_process_payment)
process_payment_button.pack(side=tk.RIGHT, padx=5)

# Reports section
reports_section = tk.LabelFrame(root, text="Reports", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, relief=tk.RAISED)
reports_section.pack(pady=20, padx=20, fill=tk.X)
reports_frame = tk.Frame(reports_section)
reports_frame.pack(fill=tk.X)

list_customer_orders_btn = tk.Button(reports_frame, text="List Customer Orders", command=btnGetCustomerOrder)
list_customer_orders_btn.pack(side=tk.LEFT, padx=5)

list_customer_payments_btn = tk.Button(reports_frame, text="List Customer Payments", command=btnGetCustomerPayment)
list_customer_payments_btn.pack(side=tk.LEFT, padx=5)

list_all_customers_btn = tk.Button(reports_frame, text="List All Customers", command=btnGetAllCustomer)
list_all_customers_btn.pack(side=tk.LEFT, padx=5)

list_all_orders_btn = tk.Button(reports_frame, text="List All Orders", command=btnGetAllOrders)
list_all_orders_btn.pack(side=tk.LEFT, padx=5)

list_all_payments_btn = tk.Button(reports_frame, text="List All Payments", command=btn_all_payment)
list_all_payments_btn.pack(side=tk.LEFT, padx=5)

exit_btn = tk.Button(reports_frame, text="EXIT", command=root.quit)
exit_btn.pack(side=tk.RIGHT, padx=5)

root.mainloop()