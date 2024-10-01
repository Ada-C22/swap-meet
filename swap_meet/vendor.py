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
        self.other_vendor = other_vendor
        self.my_item = my_item
        self.their_item = their_item

        if their_item in self.other_vendor and my_item in self.inteventory:
            self.other_vender.remove(their_item)
            self.inventory.append(their_item)
            self.inventory.remove(my_item)
            self.other_vender.append(my_item)
        