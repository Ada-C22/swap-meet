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
        else:
            return False
  
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        my_first_item = self.inventory.pop(0)
        their_first_item = other_vendor.inventory.pop(0)
        self.inventory.append(their_first_item)
        other_vendor.inventory.append(my_first_item)

        return True

    def get_by_category(self,category):
        list_by_category = []
        for item in self.inventory:
            if category == item.get_category():
                list_by_category.append(item)
        return list_by_category
    
    def get_best_by_category(self,category):
        item_by_best_condition = None
        max_condition = -1
        for item in self.inventory:
            if category == item.get_category():
                if item.condition > max_condition:
                    max_condition = item.condition 
                    item_by_best_condition = item
        return item_by_best_condition
    
    def swap_best_by_category(self,other_vendor,my_priority,their_priority):
        my_best_item = self.get_best_by_category(my_priority) 
        their_best_item = other_vendor.get_best_by_category(their_priority)
        if my_best_item is None or their_best_item is None:
            return False
        if their_priority == my_best_item.get_category() and their_best_item.get_category() == my_priority:
            self.swap_items(other_vendor,my_best_item,their_best_item)
            return True

        return False
