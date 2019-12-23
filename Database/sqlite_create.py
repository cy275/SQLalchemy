# This python file uses the following encoding: utf-8
import sqlite3

conn = sqlite3.connect('/web/Sqlite-Data/example.db')

c = conn.cursor()
c.execute('''
            CREATE TABLE Customer
            (id INTEGER PRIMARY KEY ASC, 
            first_name varchar(250) NOT NULL,
            last_name varchar(250) NOT NULL,
            username varchar(250) NOT NULL,
            email varchar(250) NOT NULL,
            address varchar(250) NOT NULL,
            town varchar(250) NOT NULL)
            ''')

c.execute('''
            INSERT INTO Customer VALUES(1, 'Toby', 'Miller', 'tmiller',
            'tmiller@example.com', '1662 Kinney Street', 'Wolfden')
            ''')

c.execute('''
            INSERT INTO Customer VALUES(2, 'Scott', 'Harvey', 'scottharvey', 
            'scottharvey@example.com', '424 Patterson Street', 'Beckinsdale')
            ''')
c.execute('''
            INSERT INTO Customer VALUES(3, 'John', 'Lara', 'johnlara', 
            'johnlara@mail.com', '3073 Derek Drive', 'Norfolk')
            ''')
c.execute('''
            INSERT INTO Customer VALUES(4, 'Sarah', 'Sarah', 'sarahtomlin',
            'sarahtomlin@mail.com', '3572 Poplar Avenue', 'Norfolk')
            ''')
c.execute('''
            INSERT INTO Customer VALUES(5, 'Toby', 'Miller', 'tmiller', 
            'tmiller@example.com', '1662 Kinney Street', 'Wolfden')
            ''')
c.execute('''
            INSERT INTO Customer VALUES(6, 'Scott', 'Harvey', 'scottharvey', 
            'scottharvey@example.com', '424 Patterson Street', 'Beckinsdale')
            ''')

conn.commit()

c.execute('''
            CREATE TABLE Item
            (id INTEGER PRIMARY KEY ASC, 
            name varchar(250), 
            cost_price FLOAT NOT NULL,
            selling_price FLOAT NOT NULL, 
            quantity INTEGER NOT NULL)
            ''')

c.execute('''
            INSERT INTO Item VALUES(1, 'Chair', 9.21, 10.81, 5)''')
c.execute('''
            INSERT INTO Item VALUES(2, 'Pen', 3.45, 4.51, 3)''')
c.execute('''
            INSERT INTO Item VALUES(3, 'Headphone', 15.52, 16.81, 50)''')
c.execute('''
            INSERT INTO Item VALUES(4, 'Travel Bag', 20.1, 22.11, 50)''')
c.execute('''
            INSERT INTO Item VALUES(5, 'Keyboard', 20.1, 22.11, 50)''')
c.execute('''
            INSERT INTO Item VALUES(6, 'Monitor', 200.14, 212.89, 50)''')
c.execute('''
            INSERT INTO Item VALUES(7, 'Watch', 100.58, 104.41, 50)''')
c.execute('''
            INSERT INTO Item VALUES(8, 'Water Bottle', 20.89, 25, 50)''')

conn.commit()

c.execute('''
            CREATE TABLE orders
            (id INTEGER PRIMARY KEY ASC,
            customer_id INTEGER,
            FOREIGN KEY(customer_id) REFERENCES Customer(id),
            item_id INTEGER,
            FOREIGN KEY(item_id) REFERENCES Item(id),
            quantity INTEGER NOT NULL)
            ''')

c.execute('''
            INSERT INTO orders VALUES(1, 1, 1, 3)''')
c.execute('''
            INSERT INTO orders VALUES(1, 1, 2, 2)''')
c.execute('''
            INSERT INTO orders VALUES(2, 2, 1, 1)''')
c.execute('''
            INSERT INTO orders VALUES(2, 2, 2, 4)''')

conn.commit()

conn.close()


