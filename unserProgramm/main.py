#importiert die Klasse 
from Stock import Stock
from Product import Product
from productInstock import ProductInStock
from ShoppingCart import ShoppingCart
from ProductInCart import ProductInCart

stock = Stock()

product = Product()
product.productname ="Tshirt"
product.price = 20
product.number = 1

inStock = ProductInStock()
inStock.product = product
inStock.amount = 10

stock.add(inStock)



product2 = Product()
product2.productname ="Tshirt"
product2.price = 25
product2.number = 1

inStock2 = ProductInStock()
inStock2.product = product2
inStock.amount = 20

stock.add(inStock)


liste = stock.getProducts()
for l in liste:
    print(l.product.productname)



Cart = ShoppingCart()
inCart = ProductInCart()
inCart.product = product
inCart.amount = 2

Cart.add(inCart)
Cart.add(inCart)

productsInCart = Cart.getProducts()
for s in productsInCart:
    print(s.amount)

print("ende")
