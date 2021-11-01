from productInstock import ProductInStock

class Stock:
    products = []

    def add(self, product:ProductInStock):
        self.products.append(product)
        #ProductInStock = self.addProductInStock
        #newstock = ProductInStock.addProductInStock + addother
        #ProductInStock.setProductInStock(newstock)

    def getProducts(self):
        return self.products


