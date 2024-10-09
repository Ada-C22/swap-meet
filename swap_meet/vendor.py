class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        my_item_index = self.inventory.index(my_item)
        their_item_index = other_vendor.inventory.index(their_item)
        other_vendor.inventory[their_item_index], self.inventory[my_item_index] = my_item, their_item

        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        first_item = self.inventory[0]
        first_item_other = other_vendor.inventory[0]
        if  first_item  and first_item_other:

            my_item_index = self.inventory.index(first_item)
            their_item_index = other_vendor.inventory.index(first_item_other)
            other_vendor.inventory[their_item_index], self.inventory[my_item_index] = first_item, first_item_other
            
            return True
 
    def get_by_category(self, category="Unknown"):
        return [item for item in self.inventory if item.get_category() == category]
    
    def get_highest_item(self, list_items, key):     
        highest = list_items[0]
        for item in list_items:
            if key(item) > key(highest):
                highest = item
        return highest
    
    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)

        if not items_in_category:
            return None

        best_item = self.get_highest_item(items_in_category, key=lambda item: item.condition)
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        personal_priority = other_vendor.get_best_by_category(my_priority)
        other_vendor_priority = self.get_best_by_category(their_priority)
        
        swap = self.swap_items(other_vendor, other_vendor_priority, personal_priority)
        return swap
    
    def get_newest_item(self, list_items, key):
        newest = list_items[0]
        for item in list_items:
            if key(item) < key(newest):
                newest = item
        return newest

    def swap_by_newest(self, other_vendor):   
        if not self.inventory or not other_vendor.inventory:
            return False
        my_newest_item = self.get_newest_item(self.inventory, key=lambda item: item.age)     
        other_vendors_newest_item = other_vendor.get_newest_item(
                other_vendor.inventory, key=lambda item: item.age
                )

        return self.swap_items(other_vendor, my_newest_item, other_vendors_newest_item)