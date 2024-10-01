from item import Item

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
        
    def get_by_id(self, id_num):
        if not self.id_num:
            return None
        self.id_num = self.id
        return self.id_num