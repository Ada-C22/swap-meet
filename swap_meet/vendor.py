
class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
    
    def __contains__(self, item):
        # return self.inventory[0] <= item <= self.inventory[len(self.inventory-1)]
        return item in self.inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item

    
    def remove(self, item):
         
        if item not in self.inventory:
            return False
    
        else:
            self.inventory.remove(item)

        return item

    def get_by_id(self, vendor_id):
        
        # return Item object inside the inventory list
        # whose id matches the vendor id
        for item in self.inventory:
            if vendor_id == item.id:
                return item
            
        return None
                
        
        
        #return None if item_id not in self.inventory else item_id