class Vendor:
    #create attributes name inventory which is empty list []
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)  
            return item
        else:
            return False
          
    def get_by_id(self, id):
        '''
        iventory = [ Item(), Item()]
        where Item has id
        '''
        for item in self.inventory:
            if id == item.id:
                return item
        return None
