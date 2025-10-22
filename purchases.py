class Purchase:
    def __init__(self) -> None:
        self.products = {}

    def add_cart(self, product):
        if product in self.products:
            self.products[product] += product.quantity
        else:
            self.products[product] = product.quantity

    def remove(self, product):
        if product in self.products:
            del self.products[product]
        else:
            print("Product not found.")

    @property
    def total(self):
        return sum(pod.price * q for pod, q in self.products.items())

    def clear(self):
        self.products = {}
