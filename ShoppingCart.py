from ProdctInCart import ProductInCart

class ShoppingCart:
    products = []

    def add(self, product:ProductInCart):
        self.products.append(product)

    def getProducts(self):
        return self.products