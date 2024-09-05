from Customer import Customer
from Product import Product
from OrderItem import OrderItem
from Order import Order
from Payment import Payment
from tkinter import messagebox
import datetime
class CompanyController:

    def __init__(self):
        self.allCustomer = [] # store all customers info
        self.customerNames = [] # store customer names 
        self.productList = []
        self.added_product_list = []
        self.orderItemList = []
        self.currentOrder = []  # To keep track of the current order
        self.customerOrder=[] # To keep track of the current customer's order
        self.all_payments_info = []# To keep track of the current customer's payment
        self.load_customers()
        self.load_products()
        self.total_price = 0

    
    #read customer data from file and create Customer objects
    def load_customers(self):
        """Load customer data from file and populate self.allCustomer and self.customerNames."""
        self.customerNames = []
        try:
            with open('customer.txt', 'r') as filename:
                for line in filename:
                    data = line.strip().split(',')
                    acustomer = Customer(data[0])
                    self.allCustomer.append(acustomer)
                    self.customerNames.append(data[0])
        except FileNotFoundError:
            print("Customer file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    # read product data from file and create Product objects
    def load_products(self):
        """Load product data from file and populate self.productList."""
        try:
            with open('product.txt', 'r') as filename:
                for line in filename:
                    data = line.strip().split(",")
                    productName = data[0]
                    productPrice = float(data[1])
                    aproduct = Product(productName, productPrice)
                    self.productList.append(aproduct)
        except FileNotFoundError:
            print("Product file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


    #Return the list of customer names
    def get_customer_names(self):
        return self.customerNames
    #Return a single customer info by name
    def get_single_customer(self, customer_name):
            for customer in self.allCustomer:
                if customer.customer_name == customer_name:
                    return customer
            return None

    def add_product(self, product_name, qty):
        """Add a product to the order and return the order details."""
        for product in self.productList:
            if product.product_name == product_name:
                subtotal = product.getPrice(int(qty))
                self.total_price += subtotal
                info = (product_name, qty, subtotal)
                self.added_product_list.append(info)
                self.orderItemList.append(OrderItem(product_name, qty))
                return info
            
        print("Product not found.")
        return None

        
    def place_order(self, customer_name, date):
        aOrder = Order(customer_name, date)
        for item in self.orderItemList:
            aOrder.addProdList(item)
        
        totalPrice = self.total_price
        aOrder.getTotalPrice(totalPrice)

        customer = self.get_single_customer(customer_name)
        if customer:
            customer.addCustomerBalance(totalPrice)
        self.currentOrder.append(aOrder)
        self.orderItemList = []
        self.added_product_list = []
        self.total_price = 0  # Reset total price after placing the order
    def selected_customer_orders(self, customer_name):
        """선택된 고객의 모든 주문을 반환합니다."""
        orders = [order for order in self.currentOrder if order.customer == customer_name]
        if orders:
            return orders
        else:
            return "No orders found for this customer."
    def process_payment(self, amount,customer_name):
        date = datetime.datetime.now()
        amount=float(amount)
        customer = self.get_single_customer(customer_name)
        result = customer.deleteCustomerBalance(amount)
        
        if "No balance." in result:
            return ("Error", result)
        elif "exceeds" in result:
            return ("Error", result)
        else:
            aPayment = Payment(date, amount)
            customer.addPayment(aPayment)
            return ("success", result)
    def selected_customer_payment(self, customer_name):
        customer = self.get_single_customer(customer_name)
        customer.payment
        return customer.payment
    def get_all_payments(self):
        for customer in self.allCustomer:
            customer_name = customer.customer_name
            for payment in customer.payment:
                payment_info = f"Customer: {customer_name}, {payment}"
                self.all_payments_info.append(payment_info)
        return self.all_payments_info