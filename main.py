from product import Product
from store import Store
from users import Customer, Seller


def main():
    # Initialize a store
    my_store = Store("PhiMart")

    # Create a seller
    seller = Seller("John Doe", "john@example.com", "password123")

    # Add some products
    product1 = Product("Laptop", 50000, 10)
    product2 = Product("Phone", 20000, 15)
    seller.add_new_product(my_store, product1)
    seller.add_new_product(my_store, product2)

    # Create a customer
    customer = Customer("Alice Smith", "alice@example.com", "pass456", 100000)

    # View all products
    print("Seller viewing products:")
    seller.view_all_products(my_store)

    # Customer adds items to cart
    customer.add_to_cart(my_store, "Laptop", 2)
    customer.add_to_cart(my_store, "Phone", 1)

    # View cart
    print("\nCustomer viewing cart:")
    customer.view_cart()

    # Customer pays the bill
    print("\nCustomer paying bill:")
    customer.pay_bill()

    # Seller checks updated products
    print("\nSeller viewing products after purchase:")
    seller.view_all_products(my_store)

    # Add deposit to customer
    customer.add_deposit = 50000
    print(f"\nCustomer new deposit: {customer.deposit}")


if __name__ == "__main__":
    main()
