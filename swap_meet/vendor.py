#

class Vendor:
    def __init__(self, inventory):
        self.inventory = inventory
    
    def __contains__(self, item):
        return self.inventory[0] <= item <= self.inventory[len(self.inventory-1)]
        
    
    def add(self, inventory, item):
        inventory.append(item)
        return item
        
    
    def remove(self, item, inventory):
        
        if self.item in self.inventory:
            inventory.remove(self.item)

        return self.item if self.item in self.inventory else False  

