import sqlite3


def get_connection():
    return sqlite3.connect("inventory.db")


# ==========================
# PRODUCT CHECK
# ==========================
def get_product(product_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT product_name
        FROM products
        WHERE product_id = ?
        """,
        (product_id,)
    )

    data = cursor.fetchone()

    conn.close()

    return data


# ==========================
# BATCH ID
# ==========================
def generate_batch_id(product_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM inventory
        WHERE product_id = ?
        """,
        (product_id,)
    )

    count = cursor.fetchone()[0]

    conn.close()

    return f"{product_id[-3:]}B{count+1}"


# ==========================
# ENTRY
# ==========================
def add_stock(
    product_id,
    product_name,
    buying_price,
    quantity
):

    conn = get_connection()
    cursor = conn.cursor()

    # save product
    cursor.execute(
        """
        INSERT OR IGNORE INTO products(
            product_id,
            product_name
        )
        VALUES (?, ?)
        """,
        (
            product_id,
            product_name
        )
    )

    # existing batch
    cursor.execute(
        """
        SELECT sl_no,current_quantity
        FROM inventory
        WHERE product_id = ?
        AND buying_price = ?
        """,
        (
            product_id,
            buying_price
        )
    )

    old = cursor.fetchone()

    if old:

        sl_no = old[0]

        new_qty = old[1] + quantity

        cursor.execute(
            """
            UPDATE inventory
            SET current_quantity = ?
            WHERE sl_no = ?
            """,
            (
                new_qty,
                sl_no
            )
        )

        batch_id = None

    else:

        batch_id = generate_batch_id(
            product_id
        )

        cursor.execute(
            """
            INSERT INTO inventory(

                batch_id,
                product_id,
                buying_price,
                current_quantity

            )
            VALUES (?, ?, ?, ?)
            """,
            (
                batch_id,
                product_id,
                buying_price,
                quantity
            )
        )

    conn.commit()
    conn.close()

    return batch_id


# ==========================
# BATCH LIST
# ==========================
def show_batches(product_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            batch_id,
            buying_price,
            current_quantity

        FROM inventory

        WHERE product_id = ?
        AND current_quantity > 0
        """,
        (product_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


# ==========================
# SELL
# ==========================
def sell_stock(
    batch_id,
    selling_price,
    sell_quantity
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            product_id,
            buying_price,
            current_quantity

        FROM inventory

        WHERE batch_id = ?
        """,
        (batch_id,)
    )

    row = cursor.fetchone()

    if not row:

        conn.close()
        return None

    product_id = row[0]
    buying_price = row[1]
    current_qty = row[2]

    if sell_quantity > current_qty:

        conn.close()
        return None

    # quantity update
    new_qty = current_qty - sell_quantity

    cursor.execute(
        """
        UPDATE inventory

        SET current_quantity = ?

        WHERE batch_id = ?
        """,
        (
            new_qty,
            batch_id
        )
    )

    # profit
    profit = (
        selling_price -
        buying_price
    ) * sell_quantity

    # sales save
    cursor.execute(
        """
        INSERT INTO sales(

            batch_id,
            product_id,
            sell_quantity,
            buying_price,
            selling_price,
            profit_or_loss

        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            batch_id,
            product_id,
            sell_quantity,
            buying_price,
            selling_price,
            profit
        )
    )

    conn.commit()
    conn.close()

    return {

        "remaining_qty": new_qty,
        "profit": profit

    }


# ==========================
# DASHBOARD 
# ==========================
def dashboard_data():

    conn = get_connection()
    cursor = conn.cursor()

    # Total unique products
    cursor.execute(
        """
        SELECT COUNT(DISTINCT product_id)
        FROM inventory
        """
    )

    total_products = cursor.fetchone()[0] or 0


    # Total stock
    cursor.execute(
        """
        SELECT SUM(current_quantity)
        FROM inventory
        """
    )

    total_stock = cursor.fetchone()[0] or 0


    conn.close()

    return (
        total_products,
        total_stock
    )

# ==========================
# INVENTORY VIEW
# ==========================
def inventory_data():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            batch_id,
            product_id,
            buying_price,
            current_quantity
        FROM inventory
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows