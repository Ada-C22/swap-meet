class Vendor:
    def __init__(self, inventory= None):
        if inventory is None:
            self.inventory = []
        else: 
            self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False 
    
    def get_by_id(self,item_id):
        for item in self.inventory: 
            if item.id == item_id:
                return item 
        return None 
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False 
        
        first_vendor_item = self.inventory[0] 
        first_othervendor_item = other_vendor.inventory[0]

        self.inventory[0]= first_othervendor_item
        other_vendor.inventory[0] = first_vendor_item

        return True 
        
