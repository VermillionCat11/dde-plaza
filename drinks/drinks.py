class Drink:
    def __init__(self, flavor, sweetness, straw=False):
        self.flavor = flavor
        self.sweetness = sweetness
        self.straw = straw

class Smoothie(Drink):
    def __init__(self):
        super().__init__(flavor, sweetness, straw=False)
        
class Juice(Drink):
    def __init__(self):
        super().__init__(flavor, sweetness, straw=False)