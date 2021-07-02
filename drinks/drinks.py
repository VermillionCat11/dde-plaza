class Drink:
    def __init__(self, ice, flavor, sweetness, straw=False):
        self.ice = ice
        self.flavor = flavor
        self.sweetness = sweetness
        self.straw = straw

class Smoothie(Drink):
    def __init__(self):
        super().__init__(flavor, sweetness, straw=False)
        
class Juice(Drink):
    def __init__(self):
        super().__init__(ice, flavor, sweetness, straw=False)
        
class Tea(Drink):
    def __init__(self, leaf):
        self.leaf = leaf
        super().__init__(ice, sweetness, straw=False)

class Milk(Drink):
    def __init__(self, milk_type):
        self.milk_type = milk_type
        super().__init__(sweetness, straw=False)