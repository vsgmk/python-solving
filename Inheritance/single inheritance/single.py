# Single Inheritance

class Wholesale():
    def sell():
        print("The profit is minimum but the sell was maximum")

class Shopkeeper(Wholesale):
    def purchase():
        print("The profit is maximum but the sell was minimum")
    
obj=Shopkeeper
obj.purchase()
obj.sell()