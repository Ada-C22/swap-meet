class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
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


    # Wave 2

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None


    #Wave 3

    def swap_items(self, other_vendor, my_item, their_item):
        '''
        1.Check if both items are in the each inventories
        2.Remove my_item from this vendor and add it to other_vendor
        3.Remove their_item from other_vendor and add it to this vendor
        '''
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)

        return True


    #Wave 4

    def swap_first_item(self, other_vender):
        if not self.inventory or not other_vender.inventory:
            return False
        
        my_item = self.inventory[0]
        their_item = other_vender.inventory[0]

        self.remove(my_item)
        other_vender.remove(their_item)

        self.add(their_item)
        other_vender.add(my_item)

        return True


    #Wave 6

    def get_by_category(self, category):
        matching_items = []
        for item in self.inventory:
            if item.get_category() == category:  
                matching_items.append(item)  
        return matching_items

    def get_best_by_category(self, category):
        best_item = None
        max_condition = 0
        for item in self.inventory:
            if item.get_category() == category:
                if item.condition > max_condition:
                    max_condition = item.condition
                    best_item = item
        return best_item        

    def swap_best_by_category(self,other_vendor,my_priority,their_priority):
        """Exchange the best items from two suppliers in a specified category"""
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False
        
        self.inventory.remove(my_best_item)
        other_vendor.inventory.remove(their_best_item)

        self.inventory.append(their_best_item)
        other_vendor.inventory.append(my_best_item)

        return True