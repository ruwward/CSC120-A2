from computer import Computer

class ResaleShop:

    # What attributes will it need?
    inventory = []
    comp = Computer.create()
    id = comp[id]
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory

    # What methods will you need?
    def buy(self):
        self.inventory.append(self.comp)
   
    def sell(self):
        self.inventory.remove(self.comp)
   
    def refurbish(self):
        if int(self.comp.year_made) < 2000:
            self.comp.price = 0
        elif int(self.comp.year_made) < 2012:
            self.comp.price = 250
        elif int(self.comp.year_made) < 2018:
            self.comp.price = 550
        else:
            self.comp.price = 1000
    
    def update_price(self):
        newprice = self.comp.price
        self.inventory.comp.price = newprice

    def print_inventory(self):
        print(self.comp)
