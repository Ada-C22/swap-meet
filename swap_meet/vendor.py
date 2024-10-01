class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        elif item in self.inventory:
            self.inventory.remove(item)
            return item
    
    def get_by_id(self, item_id):
        for item_obj in self.inventory:
            if item_obj.id == item_id:
                return item_obj
        return None
