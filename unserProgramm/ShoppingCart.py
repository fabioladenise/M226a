from ProductInCart import ProductInCart

class ShoppingCart:
    products = []

    def add(self, prc:ProductInCart):

        isAlreadyInCart = False
        for p in self.products:
            if(prc.product.number == p.product.number):
                p.amount = p.amount + prc.amount
                isAlreadyInCart = True


        if (isAlreadyInCart == False):
            self.products.append(prc)


    def getProducts(self):
        return self.products