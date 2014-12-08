class Effect():
    def __init__(self, counter = 0, max_counter = 1):
        self.counter = counter
        self.max_counter = max_counter
        
    def update(self):
        self.counter += 1
