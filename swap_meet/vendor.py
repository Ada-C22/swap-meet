class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
        
    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id is item_id:
                return item
        return None

    #Wave 3

    def swap_items(self, other_vendor, my_item, their_item):
        if their_item not in other_vendor.inventory or my_item not in self.inventory:
            return False
        other_vendor.add(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)
        self.remove(my_item)
        return True

    #Wave 4

    def swap_first_item(self, other_vender):
        if not self.inventory or not other_vender.inventory:
            return False
        my_first = self.inventory[0]
        their_first = other_vender.inventory[0]
        self.inventory[0]= their_first
        other_vender.inventory[0] = my_first
        return True

    #Wave 5
    