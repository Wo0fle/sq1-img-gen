class Square1:
    def __init__(self) -> None:
        top = Layer("A1B2C3D4")
        bottom = Layer("5E6F7G8H")
        equator_flipped = False

        self.top = top
        self.equator_flipped = equator_flipped
        self.bottom = bottom

    def __str__(self) -> str:
        return str(self.top) + ", " + str(self.equator_flipped) + ", " + str(self.bottom)

    def reset(self):
        top = Layer("A1B2C3D4")
        bottom = Layer("5E6F7G8H")
        equator_flipped = False

        self.top = top
        self.equator_flipped = equator_flipped
        self.bottom = bottom
    
    def flip_equator(self):
        self.equator_flipped = not self.equator_flipped

    def slash(self): # lol slice is taken by Python already
        pass

#########################################################

class Layer:
    current_state = ""
    solved_state = ""
    sliceable = True

    def __init__(self, solved_state) -> None:
        self.current_state = solved_state
        self.solved_state = solved_state
    
    def __str__(self) -> str:
        return str(self.current_state)

    def turn(self):
        pass

# doesnt seem too bad, the square-1 is a fundamentally simple puzzle... hopefully the way im doing this isn't wildly inefficient lol (it probably is)