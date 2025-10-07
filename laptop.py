class Laptop():
    def __init__(self,p,d):
        self.price=p
        self.discount=d
    def discountprice(self):
        discount_amount=(self.price*self.discount)/100
        final_amt=self.price-discount_amount
        print(f"Price:{self.price}")
        print(f"Discount:{self.discount}%.")
        print(f"Final Price:{final_amt}")
hp=Laptop(20000,10)
hp.discountprice()
