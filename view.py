import tkinter as tk
from tkinter import messagebox
from CompanyController import CompanyController
from Customer import Customer



company=CompanyController()
customerNames=company.customerName()
def btnGetAllCustomer():
    all_customers = company.allCustomers()
    customer_info = "\n".join(str(customer) for customer in all_customers)
    messagebox.showinfo("Customer List",customer_info)

def customerSelected(*args):
    customer_name = selected_customer.get()
    customer_info = company.getsingleCustomer(customer_name)
    customer_info_display.config(state=tk.NORMAL)
    customer_info_display.delete(1.0, tk.END) 
    customer_info_display.insert(tk.END, customer_info)
    customer_info_display.config(state=tk.DISABLED)


    
def new_order():
    print("New Order")
    
def add_product():
    print("Add Product")


root = tk.Tk()
root.title("Lincoln Office Supplies Order App by Seunguk Hong")

# Center the window
root.minsize(1000, 1000)
root.maxsize(1100, 1100)
root.columnconfigure(0, weight=1)

# Main title label
mainTitle = tk.Label(root, text="Lincoln Office Supplies", width=30, height=2)
mainTitle.pack(fill=tk.X, padx=10, pady=10)

#=========================================================================================================
# Customer section
# Customer info section with border
customer_info_section = tk.LabelFrame(root, text="Customer Informations", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, relief=tk.RAISED)
customer_info_section.pack(pady=20, padx=20, fill=tk.X)
customer_frame = tk.Frame(customer_info_section)
customer_frame.pack(fill=tk.X)

# Select customer label
selectCustomer = tk.Label(customer_frame, text="Select Customer:")
selectCustomer.pack(side=tk.LEFT, padx=5)

# Sample customer options
customers =["Choose"]+customerNames
selected_customer = tk.StringVar(root)
selected_customer.set(customers[0])  # Default value

# Dropdown menu for customer selection
customer_dropdown = tk.OptionMenu(customer_frame, selected_customer, *customers)
customer_dropdown.pack(side=tk.LEFT, padx=5)
selected_customer.trace("w", customerSelected)

# Customer info display
customer_info_display = tk.Text(customer_frame, bg="blue", fg="white", height=4.5, width=50)
customer_info_display.insert(tk.END, "empty")
customer_info_display.config(state=tk.DISABLED)  # Make the Text widget read-only
customer_info_display.pack(side=tk.LEFT, padx=5)

#=========================================================================================================

#=========================================================================================================
# Process order section
process_order_section = tk.LabelFrame(root, text="Process Order", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, relief=tk.RAISED)
process_order_section.pack(pady=20, padx=20, fill=tk.X)
process_frame = tk.Frame(process_order_section)
process_frame.pack(fill=tk.X)

# Select product label
selectProduct = tk.Label(process_frame, text="Select Product:")
selectProduct.pack(side=tk.LEFT, padx=5)

# Sample product options
products = ["Product A", "Product B", "Product C"]
selected_product = tk.StringVar(root)
selected_product.set(products[0])  # Default value

# Dropdown menu for product selection
product_dropdown = tk.OptionMenu(process_frame, selected_product, *products)
product_dropdown.pack(side=tk.LEFT, padx=5)

# Entry widget for quantity input
quantity_entry_Label = tk.Label(process_frame, text="Quantity: ")
quantity_entry_Label.pack(side=tk.LEFT, padx=5)  
quantity_entry = tk.Entry(process_frame, width=50)
quantity_entry.pack(side=tk.LEFT, padx=5)

# Button for adding product
add_product_button = tk.Button(process_frame, text="Add Product", command=add_product)
add_product_button.pack(side=tk.RIGHT, padx=5)  # Align the button to the right
#=========================================================================================================
#=========================================================================================================
# Order Detail section

order_details_section = tk.LabelFrame(root, text="Order Details", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, relief=tk.RAISED)
order_details_section.pack(pady=20, padx=20, fill=tk.X)
order_details_frame = tk.Frame(order_details_section)
order_details_frame.pack(fill=tk.X)

# Order details display
order_details_display = tk.Text(order_details_frame, bg="blue", fg="white", height=4, width=50)
order_details_display.insert(tk.END, "empty")
order_details_display.config(state=tk.DISABLED)  # Make the Text widget read-only
order_details_display.pack(side=tk.LEFT, padx=5)

# Button for new order
new_order_button = tk.Button(order_details_frame, text="New Order", command=new_order)
new_order_button.pack(side=tk.RIGHT, padx=5)  # Align the button to the right
#=========================================================================================================
#=========================================================================================================
# Payment Process section
process_payment_section = tk.LabelFrame(root, text="Process Payment", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, relief=tk.RAISED)
process_payment_section.pack(pady=20, padx=20, fill=tk.X)
process_payment_frame = tk.Frame(process_payment_section)
process_payment_frame.pack(fill=tk.X)

# Entry widget for payment amount input
payment_amount_label = tk.Label(process_payment_frame, text="Amount: ")
payment_amount_label.pack(side=tk.LEFT, padx=5)
payment_amount_entry = tk.Entry(process_payment_frame, width=50)
payment_amount_entry.pack(side=tk.LEFT, padx=5)

# Button for processing payment
process_payment_button = tk.Button(process_payment_frame, text="Process Payment", command=add_product)
process_payment_button.pack(side=tk.RIGHT, padx=5)  # Align the button to the right
#=========================================================================================================
#=========================================================================================================
# Reports section
reports_section = tk.LabelFrame(root, text="Reports", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, relief=tk.RAISED)
reports_section.pack(pady=20, padx=20, fill=tk.X)
reports_frame = tk.Frame(reports_section)
reports_frame.pack(fill=tk.X)

list_customer_orders_btn = tk.Button(reports_frame, text="List Customer Orders", command=add_product)
list_customer_orders_btn.pack(side=tk.LEFT, padx=5)

list_customer_payments_btn = tk.Button(reports_frame, text="List Customer Payments", command=add_product)
list_customer_payments_btn.pack(side=tk.LEFT, padx=5)

list_all_customers_btn = tk.Button(reports_frame, text="List All Customers", command=btnGetAllCustomer)
list_all_customers_btn.pack(side=tk.LEFT, padx=5)

list_all_orders_btn = tk.Button(reports_frame, text="List All Orders", command=add_product)
list_all_orders_btn.pack(side=tk.LEFT, padx=5)

list_all_payments_btn = tk.Button(reports_frame, text="List All Payments", command=add_product)
list_all_payments_btn.pack(side=tk.LEFT, padx=5)

exit_btn = tk.Button(reports_frame, text="EXIT", command=root.quit)
exit_btn.pack(side=tk.RIGHT, padx=5)

#=========================================================================================================
root.mainloop()
