import sqlite3


DB_NAME = "inventory.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    # PRODUCTS
    cursor.execute("""

    CREATE TABLE IF NOT EXISTS products (

        product_id TEXT PRIMARY KEY,

        product_name TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    # INVENTORY
    cursor.execute("""

    CREATE TABLE IF NOT EXISTS inventory (

        sl_no INTEGER PRIMARY KEY AUTOINCREMENT,

        batch_id TEXT UNIQUE NOT NULL,

        product_id TEXT NOT NULL,

        buying_price REAL NOT NULL,

        current_quantity INTEGER DEFAULT 0,

        FOREIGN KEY(product_id)
        REFERENCES products(product_id)

    )

    """)

    # SALES
    cursor.execute("""

    CREATE TABLE IF NOT EXISTS sales (

        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,

        batch_id TEXT NOT NULL,

        product_id TEXT NOT NULL,

        sell_quantity INTEGER NOT NULL,

        buying_price REAL NOT NULL,

        selling_price REAL NOT NULL,

        profit_or_loss REAL NOT NULL,

        sold_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":

    initialize_database()