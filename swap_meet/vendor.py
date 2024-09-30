#

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
    
    def __contains__(self, item):
        # return self.inventory[0] <= item <= self.inventory[len(self.inventory-1)]
        return item in self.inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item

    
        
    
    def remove(self, item, inventory):
        new_inventory = list(inventory)

        # Note: Is it okay to remove 
        
        if self.item in self.inventory:
            inventory.remove(self.item)

        return self.item if self.item in self.inventory else False  

