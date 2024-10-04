class Vendor:
    def __init__(self, inventory=None):
        inventory = [] if not inventory else inventory
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

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        self.inventory += [their_item]
        other_vendor.inventory.remove(their_item)
        other_vendor.inventory += [my_item]
        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]
        return self.swap_items(other_vendor, my_item, their_item)
    
    def get_by_category(self, category):
        list_of_category = [item for item in self.inventory if item.get_category() == category]
        return list_of_category
    
    def get_best_by_category(self, category):
        list_of_category = self.get_by_category(category)
        if not list_of_category:
            return None
        
        best_item = list_of_category[0]
        for item in list_of_category:
            if item.condition > best_item.condition:
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_priority_item = other_vendor.get_best_by_category(my_priority) 
        their_priority_item = self.get_best_by_category(their_priority)

        return self.swap_items(other_vendor, their_priority_item, my_priority_item)


        

    
       

