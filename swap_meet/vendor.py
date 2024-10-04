class Vendor:
    ''' 
    Represents a Vendor with an invetory of items. 
    Attributes: inventory with list of items.
    Methods: add(item): Adds item to inventory, and returns item.
            remove(item): Removes and returns item, or False if not found.
    '''
    
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory
  
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
        ''' Retrieves an item from the inventory by its ID.
            Returns None if no matching item is found.
        '''
        
        for object in self.inventory:
            if vendor_id == object.id:
                return object
        return None   
        
    def swap_items(self, other_vendor, my_item, their_item):
        '''
        Swaps items between this Vendor and other Vendor.
        Args: other_vendor(Vendor): the Vendor to swap with.
              my_item(Item): the item the other Vendor is giving.
              their_item(Item): the item the other Vendor is giving.
        Returns: bool: True if the swap was successful, False otherwise.
        '''

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        other_vendor.add(my_item)
        return True

    def swap_first_item(self,other_vendor=None):
        ''' 
        Swap the first item in this Vendor's inventory with other Vendor.
        Arg: other_vendor(Vendor): the Vendor to swap with.
        Returns: bool: True if swap successful, False if either inventory is empty.
        '''
        
        first_item = self.inventory[0]
        other_item = other_vendor.inventory[0]
        return self.swap_items(other_vendor, first_item, other_item)
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        '''
        Swaps the best items of specified categories with another value.
        '''

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        return self.swap_items(other_vendor, my_best_item, their_best_item)

    def get_by_category(self, category):
        '''
        Returns a list of items in the inventory matching the given category.
        '''
        
        category_objects = [object for object in self.inventory if category == object.get_category()]
        return category_objects

    def get_best_by_category(self, category_best):
        '''
        Returns the item with the highest condition in the given category.
        '''
        
        category_inventory = self.get_by_category(category_best)
        
        if not category_inventory:
            return None
        
        best_condition_object = category_inventory[0]
        
        for object in category_inventory:
            if object.condition > best_condition_object.condition:
                best_condition_object = object
        return best_condition_object
        
        
        
            
        


        
