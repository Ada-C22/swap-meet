class Vendor:
    #create attributes name inventory which is empty list []
    def __init__(self, inventory):
        inventory = [] if inventory is None else inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)  
            return item
        else:
            return False      