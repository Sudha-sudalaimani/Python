class Laptop():
    def __init__(self,p,d):
        self.price=p
        self.discount=d
    def discountprice(self):
        discount=(self.price*self.discount)/100
        final_price=self.price-discount
        print(f"Amount:{self.price}")
        print(f"Discount:{self.discount}%. Discounted price:{final_price}")
        
hp=Laptop(10000,10)
hp.discountprice()
