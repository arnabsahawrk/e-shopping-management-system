class List:
    def __init__(self) -> None:
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def find_product(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                return product
        return None

    def remove_product(self, product_name):
        product = self.find_product(product_name)

        if product:
            self.products.remove(product)
            print("product deleted.")
        else:
            print("product no found.")

    def view_products(self):
        if len(self.products):
            print("\t**********************")
            print("\tALL LISTED PRODUCTS")
            print("\t**********************")
            for product in self.products:
                print(
                    f"Name: {product.name}\tPrice: {product.price}\t",
                    f"Quantity: {product.quantity}",
                )
        else:
            print("No listed products available yet.")
