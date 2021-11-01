from Stock import Stock
from Product import Product
from productInstock import ProductInStock

stock = Stock()

product = Product()
product.productname ="Tshirt"
product.price = 20
product.number = 1

inStock = ProductInStock()
inStock.product = product
inStock.amount = 10

stock.add(inStock)

liste = stock.getProducts()
for l in liste:
    print(l.product.productname)

print("ende")