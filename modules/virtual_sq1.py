class Square1:
    """A virtual Square-1 object."""

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

    def slash(self): # lol "slice" is taken by Python already
        if self.top.is_sliceable() and self.bottom.is_sliceable():
            value = 0

            for i in range(len(self.top.current_state)):
                if self.top.current_state[i] in "12345678":
                    value += 1
                elif self.top.current_state[i] in "ABCDEFGH":
                    value += 2

                if value == 6:
                    left_side_U = self.top.current_state[:i+1]
                    right_side_U = self.top.current_state[i+1:]
            
            value = 0

            for i in range(len(self.bottom.current_state)):
                if self.bottom.current_state[i] in "12345678":
                    value += 1
                elif self.bottom.current_state[i] in "ABCDEFGH":
                    value += 2

                if value == 6:
                    right_side_D = self.bottom.current_state[:i+1]
                    left_side_D = self.bottom.current_state[i+1:]
            
            self.top.current_state = left_side_U + right_side_D
            self.bottom.current_state =  right_side_U + left_side_D
            self.flip_equator()
        else:
            print("uhoh")

#########################################################

class Layer:
    """An arbitrary layer of the Square-1."""

    def __init__(self, initial_state:str) -> None:
        self.current_state = initial_state
    
    def __str__(self) -> str:
        return str(self.current_state)
    
    def is_sliceable(self):
        value = 0

        for piece in self.current_state:
            #print("piece: " + str(piece))

            if piece in "12345678":
                value += 1
            elif piece in "ABCDEFGH":
                value += 2

            #print("value: " + str(value))

            if value == 6:
                return True
            elif value > 6:
                return False
        

    def turn(self, amount:int):
        if amount > 0:
            initial_state = self.current_state[::-1]

            for piece in initial_state:
                if piece in "12345678":
                    value = 1
                elif piece in "ABCDEFGH":
                    value = 2
                
                if amount >= value:
                    amount -= value
                    self.current_state = piece + self.current_state[:-1]
                elif value > amount:
                    if amount != 0 or not self.is_sliceable():
                        print("Incomplete turn: layer attempted to rotate to an unsliceable position. Layer reset to initial position.")
                        self.current_state = initial_state[::-1]

                    break
        elif amount < 0:
            amount *= -1
            initial_state = self.current_state

            for piece in initial_state:
                if piece in "12345678":
                    value = 1
                elif piece in "ABCDEFGH":
                    value = 2
                
                if amount >= value:
                    amount -= value
                    self.current_state = self.current_state[1:] + piece
                elif value > amount:
                    if amount != 0 or not self.is_sliceable():
                        print("Incomplete turn: layer attempted to rotate to an unsliceable position. Layer reset to initial position.")
                        self.current_state = initial_state

                    break

#########################################################

sq1 = Square1()
print(f"Before: top-{sq1.top}, equator flipped?-{sq1.equator_flipped}, bottom-{sq1.bottom}")

sq1.top.turn(1)
sq1.bottom.turn(-1)
sq1.slash()
sq1.top.turn(6)
sq1.bottom.turn(6)
sq1.slash()

print(f"Before: top-{sq1.top}, equator flipped?-{sq1.equator_flipped}, bottom-{sq1.bottom}")