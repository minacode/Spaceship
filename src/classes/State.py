class State():
    def __init__(self, value = None):
        self.set_value(value)

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __lt__(self, other):
        return self.value < other

    def __gt__(self, other):
        return self.value > other

    def __le__(self, other):
        return self.value <= other

    def __ge__(self, other):
        return self.value >= other

    def set_value(self, value):
        self.value = value
        
    def get_value(self):
        return self.value

    def increase(self, value):
        self.value += value
	
    def decrease(self, value):
        self.value -= value

