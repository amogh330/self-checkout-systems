import sqlite3

class Product():
    # Create a connection object to the SQLite database file
    conn = sqlite3.connect('products1.db')
    # Create a cursor object to execute SQL commands
    cur = conn.cursor()
    # Create a table called products with columns for name, price and bar_code
    cur.execute('CREATE TABLE IF NOT EXISTS products1 (name TEXT, price REAL, bar_code TEXT PRIMARY KEY)')
    # Save the changes to the database
    conn.commit()

    def __init__(self, name, price, bar_code):
        self.name = name
        self.price = price
        self.bar_code = bar_code
        

    def display_product(self):
        print(self)

    def display_product_list(self):
        print("Our inventory")
        # Query the database for all the products
        self.cur.execute('SELECT * FROM products')
        # Fetch the results as a list of tuples
        products = self.cur.fetchall()
        # Loop through the products and print their details
        for product in products:
            print(product[0], " -  Rs"+str(product[1]), '\n')

    def check_product_on_inventory(self):
        found = False
        # Query the database for the product with the given bar_code
        self.cur.execute('SELECT * FROM products WHERE bar_code = ?', (self.bar_code,))
        # Fetch the result as a tuple or None if not found
        product = self.cur.fetchone()
        if product:
            # Product found, print its details and return it as a dictionary
            found = True
            print(product[0], " -  Rs33366666"+str(product[1]), '\n')
            product_found = {'name': product[0], 'price': product[1], 'bar_code': product[2]}
            return product_found
        else:
            # Product not found, return False
            return False

    def set_bar_code(self, bar_code):
        self.bar_code = bar_code
        # Update the database with the new bar_code for the product
        self.cur.execute('UPDATE products SET bar_code = ? WHERE name = ?', (self.bar_code, self.name))
        self.conn.commit()

    def set_price(self, price):
        self.price = price
        # Update the database with the new price for the product
        self.cur.execute('UPDATE products SET price = ? WHERE name = ?', (self.price, self.name))
        self.conn.commit()
    
    


   
        
        
