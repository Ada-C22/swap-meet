class Vendor:
    def __init__(self, inventory=None):
        inventory = [] if inventory is None else inventory
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
        
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
            
        return None

    def swap_items(self,):
        pass

    def swap_first_item(self,):
        pass

    def get_by_category(self,):
        pass

    def get_best_by_category(self, ):
        pass

    def swap_best_by_categorty(self, ):
        pass