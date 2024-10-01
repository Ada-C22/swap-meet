import uuid

class Item:
    def __init__(self, id=None):
        user_uuid = uuid.uuid4()
        self.id = user_uuid.int if id is None else id
    
    def get_category(self):
        return str(self.__class__.__name__)