from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self,other_vendor,my_item,their_item):
        if my_item not in self.inventory or \
            their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    
    # def swap_items(self, other_vendor, my_item, their_item):
    #     if my_item not in self.inventory or their_item not in other_vendor.inventory:
    #         return False
        
    #     for i in range(len(self.inventory)):
    #         if self.inventory[i] == my_item:
    #             self.inventory[i] = their_item
    #             break
        
    #     for j in range(len(other_vendor.inventory)):
    #         if other_vendor.inventory[j] == their_item:
    #             other_vendor.inventory[j] = my_item
    #             break

    #     return True

    def swap_first_item(self,other_vendor):
        my_first = self.inventory[0]
        their_first = other_vendor.inventory[0]

        result = self.swap_items(other_vendor,my_first,their_first)

