class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item

    def get_by_id(self,id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        vendor_item = other_vendor.get_by_id(their_item.id)
        an_item = self.get_by_id(my_item.id)

        if an_item is not None and vendor_item is not None:
            other_vendor.add(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            self.remove(my_item)
            return True
        else:
            return False
#



    

    def swap_first_item(self, other_vendor): 
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        else:
            first_item_v = self.inventory[0]
            first_item_friend = other_vendor.inventory[0]
            self.remove(first_item_v)
            other_vendor.remove(first_item_friend)
            self.add(first_item_friend)
            other_vendor.add(first_item_v)
            return True



