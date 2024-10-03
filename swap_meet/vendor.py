class Vendor:
    def __init__(self, inventory=None,):
        inventory = [] if inventory is None else inventory
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
        
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
            
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            return True
        else:
            return False
    
    def swap_first_item(self, other_vendor):
        # if not self.inventory or not other_vendor.inventory:
        #     return False
        # else:
        #     other_vendor.inventory.append(self.inventory[0])
        #     self.inventory.remove(self.inventory[0])
        #     self.inventory.append(other_vendor.inventory[0])
        #     other_vendor.inventory.remove(other_vendor.inventory[0])
        #     return True
        
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory[0]
            self.swap_items(other_vendor, my_first_item, their_first_item)
            return True

    def get_by_category(self, category):
        category_list = []
        
        for item in self.inventory:
            if category == item.get_category(): 
                category_list.append(item)
        
        return category_list
    
    def get_best_by_category(self, category):
        best_item = self.inventory[0]

        for item in self.inventory:
            if category == item.get_category() and item.condition > best_item.condition:
                best_item = item

        if best_item.get_category() == category:
            return best_item
        else:
            return None
    

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not other_vendor.inventory or not self.inventory:
            return False
        
        my_item_to_swap = self.get_best_by_category(their_priority)
        their_item_to_swap = other_vendor.get_best_by_category(my_priority)
        
        if my_item_to_swap and their_item_to_swap:
            self.swap_items(other_vendor, my_item_to_swap, their_item_to_swap)
            return True
        elif not my_item_to_swap or not their_item_to_swap:
            return False
    
    # Optional 
    # get the newest item and then swap the item
    # situation haven't consider:
    # 1. if there're more thean one item with same age? 
    # 2. if my inventory or their inventory is empty

    def get_newest_item(self):
        newest_item = self.inventory[0]
        
        for item in self.inventory:
            if item.age < newest_item.age:
                newest_item = item
        
        return newest_item 
           
    def swap_by_newest(self, other_vendor):
        my_newest_item = self.get_newest_item()
        their_newest_item = other_vendor.get_newest_item()
        
        return self.swap_items(other_vendor, my_newest_item, their_newest_item)

        
        






        