from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = []
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory

    # What methods will you need?
    def buy(self):
        computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
        self.inventory.append(computer)
    def sell(self):
        self.inventory.remove()
    def refurbish(self):
        
    def update_price(self):
    def print_inventory(self):
