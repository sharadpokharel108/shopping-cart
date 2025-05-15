# Welcome to the Shopping Cart API Documentation

Welcome to the official documentation for the **Shopping Cart API**. This API allows users to manage a shopping cart by adding items, viewing the total price, and checking the quantity of each item.

This documentation will guide you through the setup, usage, and features of the API.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)

---

## Introduction

The **Shopping Cart API** is built using **FastAPI**, and it allows you to manage items in a shopping cart for e-commerce or retail applications. This simple yet powerful API allows you to:
- Add items to the cart.
- View the cart summary, including total price and item quantities.

## Getting Started

Follow these steps to get started with the Shopping Cart API:

### Prerequisites
Make sure you have the following installed:
- Python 3.7 or higher
- `pip` (Python package installer)

### Installation
1. Clone the repository.
2. Navigate into the project directory.
3. Create a virtual environment.
4. Activate the virtual environment.
5. Install the dependencies using `pip install -r requirements.txt`.
6. Run the FastAPI server with `uvicorn app.main:app --reload`.

### Access the Swagger UI
Once the server is running, visit the interactive API documentation at `http://127.0.0.1:8000/docs` to explore the available API endpoints.

---

## Features

The **Shopping Cart API** provides the following features:

- **Add items to cart**: Allows you to add items with a name, price, and quantity to the cart.
- **View cart summary**: Displays the total price of items and the quantity of each item in the cart.

---

## API Endpoints

### 1. **Add Item to Cart**
- **Endpoint**: `POST /cart`
- **Description**: Adds an item to the shopping cart.
- **Request Body**:
  - `item`: The name of the item.
  - `price`: The price of the item (must be a positive number).
  - `quantity`: The number of items to be added.

- **Response**: 
  - Message indicating that the item was successfully added to the cart.

### 2. **Get Cart Summary**
- **Endpoint**: `GET /cart/summary`
- **Description**: Retrieves the total price and quantity of items in the cart.
- **Response**: 
  - Total price of all items in the cart.
  - Total quantity of items in the cart.

---

## Testing

The project includes automated tests to verify its functionality. You can run the tests using **pytest**:

1. Install test dependencies.
2. Run the tests.

---
