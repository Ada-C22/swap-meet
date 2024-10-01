class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
     
        return True