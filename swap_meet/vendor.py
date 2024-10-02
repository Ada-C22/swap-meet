
class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory
    
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
                
        
    def swap_items(self, other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        # Transactions
        self.remove(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        other_vendor.add(my_item)
        return True
    
    # DRY up code by using swap_items() inside of this method below
    # in swap_first_item()
    def swap_first_item(self,other_vendor=None ):
        # if either is empty return false
        if not self.inventory or not other_vendor.inventory:
            return False
        
        first_item = self.inventory[0]
        other_item = other_vendor.inventory[0]

         #swap remove inventory 
        self.remove(first_item)
        other_vendor.remove(other_item)
        # swap add inventory
        self.add(other_item)
        other_vendor.add(first_item)
        
        return True
        
      
        
        
            
        


        


