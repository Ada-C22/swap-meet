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
            # figure out what index each item is within their list
            my_index = self.inventory.index(my_item)
            their_index = other_vendor.inventory.index(their_item)

            # reassign that element with the other item 
            self.inventory[my_index] = their_item
            other_vendor.inventory[their_index] = my_item
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
    
    