# Intelligent Inventory Management System

## Overview

The **Intelligent Inventory Management System** is a Python-based backend project designed to help businesses efficiently manage stock operations, inventory tracking, and profit/loss monitoring. The system allows users to add stock, sell products, automatically update inventory quantities, and calculate profit dynamically using SQLite database integration.

This project was built with a modular and scalable architecture to simulate real-world backend development practices.

---

# Features

* Add new products and stock entries
* Sell products with stock validation
* Automatic inventory quantity management
* Real-time profit/loss calculation
* SQLite database integration
* Modular API-style Python functions
* Error handling and database transaction management
* Clean and maintainable project structure

---

# Tech Stack

* **Programming Language:** Python
* **Database:** SQLite3
* **Concepts Used:**

  * SQL Queries
  * CRUD Operations
  * Database Relationships
  * Modular Programming
  * Exception Handling

---

# Project Structure

```bash id="1cpm9d"
inventory-management-system/
│
├── __pycache__/              # Compiled Python cache files
│
├── app.py                    # Main application execution file
│
├── database.py               # Database connection and table creation
│
├── inventory.db              # SQLite database file
│
├── inventory.sqbpro          # SQLite Browser project file
│
├── inventory_operations.py   # Stock entry, selling, inventory logic
│
└── scan_engine.py            # Barcode scanning / scanning utilities
```

## File Description

### app.py

* Main entry point of the project.
* Used to execute inventory operations and test functionalities.

---

### database.py

Handles:

* SQLite database connection
* Table creation
* Database initialization

---

### inventory_operations.py

Contains all core business logic:

* Add stock
* Sell stock
* Update inventory
* Profit/loss calculations

---

### scan_engine.py

Responsible for barcode-related operations and future scanner integration.

---

### inventory.db

Main SQLite database file storing:

* Stock Entry
* Stock Exit
* Inventory Data

---

### inventory.sqbpro

SQLite Browser project configuration file used for database inspection and management.

---

### **pycache**/

Automatically generated Python cache files for faster execution.

```
```


---

# Database Tables

## 1. Stock Entry

Stores product purchase information.

| Column Name     | Description               |
| --------------- | ------------------------- |
| product_id      | Unique product identifier |
| product_name    | Product name              |
| buying_price    | Product buying price      |
| buying_quantity | Purchased quantity        |

---

## 2. Stock Exit

Stores product selling information.

| Column Name      | Description               |
| ---------------- | ------------------------- |
| product_id       | Unique product identifier |
| product_name     | Product name              |
| selling_price    | Product selling price     |
| selling_quantity | Sold quantity             |

---

## 3. Inventory

Stores current inventory and profit details.

| Column Name      | Description               |
| ---------------- | ------------------------- |
| product_id       | Unique product identifier |
| product_name     | Product name              |
| current_quantity | Available stock           |
| profit_or_loss   | Total profit/loss         |

---

# Installation & Setup

## Clone Repository

```bash
git clone https://github.com/your-username/inventory-management-system.git
```

## Navigate to Project Folder

```bash
cd inventory-management-system
```

## Run the Project

```bash
python main.py
```

---

# Example Usage

## Add Stock

```python
add_stock(
    "8904104708973",
    "Good Night Coil",
    10,
    5
)
```

## Sell Stock

```python
sell_stock(
    "8904104708973",
    15,
    2
)
```

---

# Profit Calculation

```text
Profit = (Selling Price - Buying Price) × Sold Quantity
```

---

# Future Improvements

* Flask REST API integration
* Streamlit dashboard
* Sales analytics visualization
* AI-based demand forecasting
* Barcode scanner support
* CSV/Excel export
* Multi-user authentication
* PostgreSQL migration for scalability

---

# Learning Outcome

This project helped in understanding:

* Database design fundamentals
* Inventory management logic
* Python modular architecture
* SQL CRUD operations
* Backend-oriented project structure
* Error handling and transaction management

---

# Author

**Himadri Maity**

Computer Science Graduate
