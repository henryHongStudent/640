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
def customerSelected(*args):
    """Display selected customer's details."""
    customer_name = selected_customer.get()
    customer_info = company.get_single_customer(customer_name) # get customer info by name
    customer_info_display.config(state=tk.NORMAL)
    customer_info_display.delete(1.0, tk.END)
    customer_info_display.insert(tk.END, customer_info)
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

def btn_place_order():
    """Place a new order and reset the order details."""
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    selectCustomer = selected_customer.get()
    company.place_order(selectCustomer,date)
    order_details_display.config(state=tk.NORMAL)
    order_details_display.delete(1.0, tk.END)
    order_details_display.insert(tk.END, "Order placed successfully.")
    order_details_display.config(state=tk.DISABLED)

def process_payment():
    """Process the payment with the entered amount."""
    amount = payment_amount_entry.get()
    if not amount.replace('.', '', 1).isdigit():
        messagebox.showwarning("Invalid Input", "Amount must be a number.")
        return

    # Add payment processing logic here
    # Example: Update customer balance, create a payment record, etc.

    messagebox.showinfo("Payment", f"Payment of ${amount} processed.")

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

process_payment_button = tk.Button(process_payment_frame, text="Process Payment", command=process_payment)
process_payment_button.pack(side=tk.RIGHT, padx=5)

# Reports section
reports_section = tk.LabelFrame(root, text="Reports", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, relief=tk.RAISED)
reports_section.pack(pady=20, padx=20, fill=tk.X)
reports_frame = tk.Frame(reports_section)
reports_frame.pack(fill=tk.X)

list_customer_orders_btn = tk.Button(reports_frame, text="List Customer Orders", command=lambda: messagebox.showinfo("Not Implemented", "Feature not implemented."))
list_customer_orders_btn.pack(side=tk.LEFT, padx=5)

list_customer_payments_btn = tk.Button(reports_frame, text="List Customer Payments", command=lambda: messagebox.showinfo("Not Implemented", "Feature not implemented."))
list_customer_payments_btn.pack(side=tk.LEFT, padx=5)

list_all_customers_btn = tk.Button(reports_frame, text="List All Customers", command=btnGetAllCustomer)
list_all_customers_btn.pack(side=tk.LEFT, padx=5)

list_all_orders_btn = tk.Button(reports_frame, text="List All Orders", command=btnGetAllOrders)
list_all_orders_btn.pack(side=tk.LEFT, padx=5)

list_all_payments_btn = tk.Button(reports_frame, text="List All Payments", command=lambda: messagebox.showinfo("Not Implemented", "Feature not implemented."))
list_all_payments_btn.pack(side=tk.LEFT, padx=5)

exit_btn = tk.Button(reports_frame, text="EXIT", command=root.quit)
exit_btn.pack(side=tk.RIGHT, padx=5)

root.mainloop()