class Vendor:
    def __init__(self, inventory=None):

        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, new_item_added):
        self.inventory.append(new_item_added)
        return new_item_added
    
    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return False
        else:
            self.inventory.remove(item_to_remove)
            return item_to_remove