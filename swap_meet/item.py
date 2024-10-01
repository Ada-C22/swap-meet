<<<<<<< HEAD
import uuid 
class Item:
    def __init__(self, id=None):
        self.id = id if id is not None else uuid.uuid4().int
    def get_category(self):
        return type(self).__name__

=======
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
>>>>>>> 41c4f9a66446fdf5da871c2087fda1ef9a57043f
