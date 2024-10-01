from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory=None):
<<<<<<< HEAD
        if inventory is None:
            inventory = []
        self.inventory = inventory

      

    def add(self, added_item):
        self.inventory.append(added_item)
        return added_item

    
    def remove(self, remove_item):
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        return False
=======
        self.inventory = [] if inventory is None else inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_id(self, id):
        for item in self.inventory:
            if id == item.id:
                return item
        return None


>>>>>>> 6533bc30c9a029f047be2c9fae42e4f02a97e501
