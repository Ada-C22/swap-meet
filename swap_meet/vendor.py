class Vendor:
    def __init__(self,inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_id(self,id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        return False
  
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]
        self.inventory[0] = their_first_item
        other_vendor.inventory[0] = my_first_item
        return True

    def get_by_category(self,category):
        list_by_category = []
        for item in self.inventory:
            if item.get_category() == category:
                list_by_category.append(item)
        return list_by_category
    
    def get_best_by_category(self,category):
        best_item = None
        for item in self.inventory:
            if item.get_category() == category:
                if best_item is None or item.condition > best_item.condition:
                    best_item = item
        return best_item
    
    def swap_best_by_category(self,other_vendor,my_priority,their_priority):
        my_best_item = self.get_best_by_category(their_priority) 
        their_best_item = other_vendor.get_best_by_category(my_priority)
        if my_best_item is None or their_best_item is None:
            return False
        return self.swap_items(other_vendor, my_best_item, their_best_item)

