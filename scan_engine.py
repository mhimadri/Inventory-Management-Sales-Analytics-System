import cv2
from pyzbar.pyzbar import decode

import tkinter as tk
from tkinter import simpledialog, messagebox

import sys

from inventory_operations import (
    get_product,
    add_stock,
    show_batches,
    sell_stock
)


def start_scanner(mode):

    popup = tk.Tk()
    popup.withdraw()

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():

        messagebox.showerror(
            "Camera Error",
            "Camera not found."
        )

        return

    scanned_products = set()

    while True:

        success, frame = camera.read()

        if not success:
            break

        barcodes = decode(frame)

        for barcode in barcodes:

            product_id = barcode.data.decode(
                "utf-8"
            )

            # duplicate scan stop
            if product_id in scanned_products:
                continue

            scanned_products.add(
                product_id
            )

            print(
                "Scanned:",
                product_id
            )

            # ==========================
            # ENTRY MODE
            # ==========================
            if mode == "entry":

                product = get_product(
                    product_id
                )

                # existing product
                if product:

                    product_name = product[0]

                    messagebox.showinfo(
                        "Existing Product",
                        product_name
                    )

                # new product
                else:

                    product_name = simpledialog.askstring(
                        "New Product",
                        "Enter Product Name:"
                    )

                    if not product_name:
                        continue

                quantity = simpledialog.askinteger(
                    "Quantity",
                    "Enter Quantity:"
                )

                if quantity is None:
                    continue

                buying_price = simpledialog.askfloat(
                    "Buying Price",
                    "Enter Buying Price:"
                )

                if buying_price is None:
                    continue

                batch_id = add_stock(

                    product_id,
                    product_name,
                    buying_price,
                    quantity

                )

                messagebox.showinfo(

                    "Success",

                    f"Product Added Successfully\n\n"
                    f"Batch ID: {batch_id}"

                )

                camera.release()
                cv2.destroyAllWindows()

                return

            # ==========================
            # EXIT MODE
            # ==========================
            elif mode == "exit":

                batches = show_batches(
                    product_id
                )

                if not batches:

                    messagebox.showerror(
                        "Error",
                        "No Stock Found"
                    )

                    continue

                batch_text = ""

                for batch in batches:

                    batch_text += (
                        f"{batch[0]}"
                        f" | Buy:{batch[1]}"
                        f" | Qty:{batch[2]}\n"
                    )

                batch_id = simpledialog.askstring(

                    "Select Batch",

                    batch_text

                )

                if not batch_id:
                    continue

                sell_qty = simpledialog.askinteger(

                    "Sell Quantity",

                    "Enter Sell Quantity:"

                )

                if sell_qty is None:
                    continue

                selling_price = simpledialog.askfloat(

                    "Selling Price",

                    "Enter Selling Price:"

                )

                if selling_price is None:
                    continue

                result = sell_stock(

                    batch_id,
                    selling_price,
                    sell_qty

                )

                if not result:

                    messagebox.showerror(
                        "Error",
                        "Sell Failed"
                    )

                    continue

                messagebox.showinfo(

                    "Sale Summary",

                    f"Product: {result['product_name']}\n\n"
                    f"Remaining Stock: {result['remaining_qty']}\n\n"
                    f"Profit/Loss: {result['profit']}"

                )

                camera.release()
                cv2.destroyAllWindows()

                return

        cv2.imshow(
            "Scanner",
            frame
        )

        if cv2.waitKey(1) == 27:
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":

    # default safe mode
    mode = "entry"

    if len(sys.argv) > 1:

        mode = sys.argv[1]

    start_scanner(mode)