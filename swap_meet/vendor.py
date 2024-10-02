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



