#

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
    
    def __contains__(self, item):
        # return self.inventory[0] <= item <= self.inventory[len(self.inventory-1)]
        return item in self.inventory
        pass
    def add(self, item):
        self.inventory.append(item)
        return item

    
        
    
    def remove(self, item, inventory):
        new_inventory = list(inventory)

        # Note: Is it okay to remove 
        if self.item in new_inventory:
            new_inventory.remove(item)
        
        return item in new_inventory
                
