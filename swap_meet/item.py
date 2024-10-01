import uuid

class Item:

    def __init__(self, id = None):
        # Generate a random UUID
        random_uuid = uuid.uuid4()

        # Convert UUID to a random integer
        random_int = random_uuid.int

        id = random_int if id is None else id
        self.id = id

    def get_category(self):
        return self.__class__.__name__
