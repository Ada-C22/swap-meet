class Vendor:
    def __init__(self, inventory=None):

        self.inventory = [] if inventory is None else inventory

    def add(self, new_item_added):
        self.inventory.append(new_item_added)
        return new_item_added

    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return False
        else:
            self.inventory.remove(item_to_remove)
            return item_to_remove

    def get_by_id(self, item_id):
        #from inventory list retreive item that is same as item_id provided
        for item in self.inventory:
            if item.id == item_id: # Compare id from Item class with item_id
                return item
        
