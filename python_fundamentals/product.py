class product:
    def __init__(self,price,item_name,weigth,brand):
        self.price=price
        self.item_name=item_name
        self.weigth=weigth
        self.brand=brand
        self.status="for sale"
        
    def Sell(self):
        self.status="sold"
        return self

    def AddTax(self, tax):
        return self.price+self.price*tax/100

    def Return_Item(self,reason_for_return):
        if reason_for_return=="defective":
            self.status=reason_for_return 
            self.price=0
        elif reason_for_return=="like_new":
            self.status="for sale"             
        elif reason_for_return=="opened":
            self.status="used" 
            self.price=self.price - self.price/5
        return self

    def Display_Info(self):
        print("\nPrice: " ,self.price,"\nItem Name: ",self.item_name,"\nWeigth: ",self.weigth,"\nBrand: ",self.brand,"\nStatus: ",self.status)

product1=product(2000.0,"A",20,"Abrand")
product1.Sell().Display_Info()

product2=product(2000.0,"B",33.5,"Bbrand")
product2.price=product2.AddTax(10)
product2.Return_Item("like_new").Display_Info()

product3=product(2000.0,"C",10.9,"Cbrand")
product3.price=product3.AddTax(10)
product3.Return_Item("opened").Display_Info()

product4=product(2000.0,"D",40,"Abrand")
product4.price=product4.AddTax(10)
product4.Sell().Display_Info()

product5=product(2000.0,"E",78.5,"Bbrand")
product5.price=product5.AddTax(10)
product5.Sell().Display_Info()

product6=product(20000000.0,"F",12,"Cbrand")
product6.price=product6.AddTax(10)
product6.Return_Item("defective").Display_Info()        