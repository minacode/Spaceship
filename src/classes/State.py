class State():
    def __init__(self, value = None):
        self.set_value(value)
    
    def set_value(self, value):
        self.value = value
        
    def get_value(self):
        return self.value
