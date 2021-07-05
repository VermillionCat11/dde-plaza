class Drink:
    def __init__(self, flavor, sweetness, straw=False, ice=False):
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
    def __init__(self, leaf, boba=False):
        self.leaf = leaf
        super().__init__(ice, sweetness, straw=False)
        
class Milk_Tea(Tea):
    def __init__(self, flavor):
        self.flavor = flavor
        super().__init__(boba=False)
        
class Fruit_Tea(Tea):
    def __init__(self, flavor):
        self.flavor = flavor
        super().__init__()

class Milk(Drink):
    def __init__(self, milk_type):
        self.milk_type = milk_type
        super().__init__(sweetness, straw=False)