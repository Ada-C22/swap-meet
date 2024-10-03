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
    def swap_items(self,other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.remove(my_item)
        other_vendor.remove(their_item)

        self.add(their_item)
        other_vendor.add(my_item)
        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False 
        
        first_vendor_item = self.inventory[0] 
        first_othervendor_item = other_vendor.inventory[0]

        self.inventory[0]= first_othervendor_item
        other_vendor.inventory[0] = first_vendor_item

        return True 
    
    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.get_category() == category:
                items_in_category.append(item)
        return items_in_category
        







