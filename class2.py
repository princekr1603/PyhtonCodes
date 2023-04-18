class item:
    def calprice(self,x,y):
        print(x*y)
        
item1=item()
item1.name="phone"
item1.price=100
item1.quantity=5
item1.calprice(item1.price,item1.quantity)

item2=item()
item2.name="laptop"
item2.price=10000
item2.quantity=8
item2.calprice(item2.price,item2.quantity)