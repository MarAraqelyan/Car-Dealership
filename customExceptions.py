class NotInInventory(Exception):
    def __init__(self):
        super().__init__(self, "Not present in the inventory")