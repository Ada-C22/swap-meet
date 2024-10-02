class Vendor:
    # wave 1
    def __init__(self, inventory=None):
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
        else:
            return False
    # wave 2      
    def get_by_id(self, id):
        '''
        iventory = [ Item(), Item()]
        where Item has id
        '''
        for item in self.inventory:
            if id == item.id:
                return item
        return None
    
    # wave 3
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            #look through Vendor's inventory and find where my_item is located and return its index
            my_item_index = self.inventory.index(my_item)
            self.inventory[my_item_index] = their_item
            
            their_item_index = other_vendor.inventory.index(their_item)
            other_vendor.inventory[their_item_index] = my_item
            return True
        else:
            return False

    # wave 4
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]
        
        self.swap_items(other_vendor, my_first_item, their_first_item)

        return True
    
    # wave 6
    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.get_category() == category:
                result.append(item)
        return result        
        
    def get_best_by_category(self, category):
        best_item, best_condition = None, -1
        
        for item in self.inventory:
            if item.get_category() == category and item.condition > best_condition:
                best_item = item    
        
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)
        
        if not my_item or not their_item:
            return False
        
        self.swap_items(other_vendor, my_item, their_item)
        return True
    
    # Optional Enhancements
    def get_newest(self):
        pass
    
    def swap_by_newest(self):
        pass
    