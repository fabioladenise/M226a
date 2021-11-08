from productInstock import ProductInStock

class Stock:
    products = []

    def add(self, pis:ProductInStock):
        # überprüfen ob produkt bereits in liste ist
        # for .... durch alle self.products durchloopen
        # if (.........).. überprüfen, ob aktuelles loop-item übereinstimmt mit neuem item
        isAlreadyInStock = False
        for p in self.products:
            if(pis.product.number == p.product.number ):
                isAlreadyInStock = True

        if  (isAlreadyInStock == False):
            self.products.append(pis)
        else:
            print("It exist already")


    def getProducts(self):
        return self.products


