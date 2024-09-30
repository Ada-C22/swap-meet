class Vendor:
    #create attributes name inventory which is empty list []
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)  
            return item
        else:
            return False
        
    # def get_inventory(self):
    #     return self.inventory     
    
    def get_by_id(self, id):
        '''
        iventory = [ Item(), Item()]
        where Item has id
        '''
        for item in self.inventory:
            if id == item.id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        """
        Parameters:
            other_vendor: represent the friend that the vendor is swapping
            my_item: item this Vendor instance plans to give
            their_item: item the friend plans to give
        """
        #remove() my_item from this vendor inventory and add to friend inventory
        #remove() their_item from other's vendor inventory and add to this inventory
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            self.add(their_item)
            
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            
            return True
        return False