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
        for item in self.inventory:
            if item.id == item_id:
                return item

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        return False
