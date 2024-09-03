from Customer import Customer


class CompanyController:

    def __init__(self):
        self.allCustomer = []
        self.customerNames = []
        self.productList = []  # Initialize product list
        self.load_customers()  # Initialize and load customer data
        self.load_products()  # Initialize and load product data
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

    def allCustomers(self):
        """Return the list of all customers. Load customers if not already loaded."""
        if not self.allCustomer:  # Check if data is already loaded
            self._load_customers()
        return self.allCustomer

    def customerName(self):
        """Return the list of customer names."""
        return self.customerNames

    def getsingleCustomer(self, selected_customer):
        """Get a single customer by name."""
        customer = next((c for c in self.allCustomer if c.customer_name == selected_customer), None)
        if customer:
            return str(customer)
        return "Customer not found"
    def load_products(self):
        """Load product data from file and populate self.productList."""
        try:
            with open('product.txt', 'r') as filename:
                for line in filename:
                    data = line.strip().split(",")
                    productName = data[0]
                    self.productList.append(str(productName))
        except FileNotFoundError:
            print("Product file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
            