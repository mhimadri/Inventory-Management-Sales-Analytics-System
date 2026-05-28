import tkinter as tk
from tkinter import ttk
import subprocess
import sys
import os

from inventory_operations import (
    inventory_data,
    dashboard_data
)


# ==========================
# ROOT
# ==========================
root = tk.Tk()

root.title("Smart Inventory")
root.geometry("1000x700")
root.configure(bg="white")


# ==========================
# SCANNER FUNCTIONS
# ==========================
def open_entry_scanner():

    current_folder = os.path.dirname(
        os.path.abspath(__file__)
    )

    subprocess.Popen(
        [
            sys.executable,
            "scan_engine.py",
            "entry"
        ],
        cwd=current_folder
    )


def open_exit_scanner():

    current_folder = os.path.dirname(
        os.path.abspath(__file__)
    )

    subprocess.Popen(
        [
            sys.executable,
            "scan_engine.py",
            "exit"
        ],
        cwd=current_folder
    )


# ==========================
# DASHBOARD
# ==========================
def dashboard_page():

    for widget in root.winfo_children():
        widget.destroy()

    total_products, total_stock = dashboard_data()

    title = tk.Label(
        root,
        text="Dashboard",
        font=("Arial", 22, "bold")
    )
    title.pack(pady=20)

    product_label = tk.Label(
        root,
        text=f"Total Products: {total_products}",
        font=("Arial", 16)
    )
    product_label.pack(pady=20)

    stock_label = tk.Label(
        root,
        text=f"Total Stock: {total_stock}",
        font=("Arial", 16)
    )
    stock_label.pack(pady=20)

    bottom_navigation()


# ==========================
# INVENTORY PAGE
# ==========================
def inventory_page():

    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(
        root,
        text="Inventory",
        font=("Arial", 22, "bold")
    )
    title.pack(pady=10)

    columns = (
        "Batch",
        "Product ID",
        "Buying Price",
        "Quantity"
    )

    tree = ttk.Treeview(
        root,
        columns=columns,
        show="headings",
        height=20
    )

    for col in columns:

        tree.heading(
            col,
            text=col
        )

        tree.column(
            col,
            width=200,
            anchor="center"
        )

    tree.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    rows = inventory_data()

    for row in rows:

        tree.insert(
            "",
            "end",
            values=row
        )

    bottom_navigation()


# ==========================
# NAVIGATION
# ==========================
def bottom_navigation():

    nav_frame = tk.Frame(
        root,
        bg="white"
    )

    nav_frame.pack(
        side="bottom",
        pady=20
    )

    tk.Button(
        nav_frame,
        text="Home",
        width=15,
        command=home_page
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        nav_frame,
        text="Dashboard",
        width=15,
        command=dashboard_page
    ).grid(row=0, column=1, padx=10)

    tk.Button(
        nav_frame,
        text="Inventory",
        width=15,
        command=inventory_page
    ).grid(row=0, column=2, padx=10)


# ==========================
# HOME PAGE
# ==========================
def home_page():

    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(
        root,
        text="Smart Inventory",
        font=("Arial", 28, "bold")
    )
    title.pack(pady=60)

    tk.Button(
        root,
        text="Entry",
        width=25,
        height=2,
        command=open_entry_scanner
    ).pack(pady=20)

    tk.Button(
        root,
        text="Exit",
        width=25,
        height=2,
        command=open_exit_scanner
    ).pack(pady=20)

    bottom_navigation()


# ==========================
# START APP
# ==========================
if __name__ == "__main__":

    home_page()

    root.mainloop()