class Square1:
    """A virtual Square-1 object."""

    def __init__(self) -> None:
        """Initializes the Square1. Solved by default."""

        self.top = Layer("A1B2C3D4")
        self.equator_flipped = False
        self.bottom = Layer("5E6F7G8H")

    def __str__(self) -> str:
        """Converts the Square1 to a string."""
        
        if self.equator_flipped:
            return f"{self.top}/{self.bottom}"
        else:
            return f"{self.top}|{self.bottom}"
    
    def flip_equator(self) -> None:
        """Directly changes the equator state of the Square1 from flipped to not flipped (and vice-versa) without affecting other pieces."""

        self.equator_flipped = not self.equator_flipped

    def slash(self) -> None: # lol "slice" is taken by Python already
        """Does a slice/slash move to the Square1."""

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
    
    def apply_alg(self, alg:str, for_case:bool=False) -> None:
        """Applies an input algorithm to the Square1, starting from a solved state."""

        self.__init__()

        simplfied_alg = list(alg)

        for char in alg:
            if not char.isnumeric() and ((char != '/') and (char != ',') and (char != '-')):
                simplfied_alg.remove(char)

        simplfied_alg = [slash.split(',') for slash in (''.join(simplfied_alg)).split('/')]

        legal = True

        for turns in simplfied_alg:
            try:
                turn_amount = int(turns[0])

                while abs(turn_amount) > 6:
                    if turn_amount > 0:
                        turn_amount -= 6
                    else:
                        turn_amount += 6

                if not self.top.turn(turn_amount):
                    self.__init__()
                    legal = False
                    break
            except:
                if turns[0] != '':
                    print('SYNTAX ERROR involving "-" detected!')
                    self.__init__()
                    legal = False
                    break
            
            try:
                turn_amount = int(turns[1])

                while abs(turn_amount) > 6:
                    if turn_amount > 0:
                        turn_amount -= 6
                    else:
                        turn_amount += 6

                if not self.bottom.turn(turn_amount):
                    self.__init__()
                    legal = False
                    break
            except ValueError:
                if turns[1] != '':
                    print('SYNTAX ERROR involving "-" detected!')
                    self.__init__()
                    legal = False
                    break
            except:
                pass # assume 0 for bottom turn if there's only one input
            
            if len(turns) > 2:
                print('SYNTAX ERROR involving "," detected!')
                self.__init__()
                legal = False
                break

            self.slash()

        if legal:
            self.slash()
        else:
            if for_case:
                self.error_detected(turns, simplfied_alg, 0)
            else:
                self.error_detected(turns, simplfied_alg, 1)
    
    def apply_case(self, case:str) -> None:
        """Changes the Square1's state so that the input algorithm solves it (by reversing the input algorithm and using the "apply_alg" method)."""

        ...

    def apply_state(self, state:str) -> None:
        """Changes the Square1's state to match the input state."""

        # should i even do this?? or should i just take the input state from the site and directly send it to img_genner? im thinking leave it here for error handling

        ...

    def error_detected(self, error_turns:list, error_simplfied_alg:list, input_type:int) -> None:
        if input_type == 0: # case
            ...
        elif input_type == 1: # alg
            print(f'Error at "{','.join(error_turns)}" (move #{error_simplfied_alg.index(error_turns) + 1}).\nSquare-1 reset.')
        elif input_type == 2: # state
            ...

#########################################################

class Layer:
    """An arbitrary layer of the Square1."""

    def __init__(self, initial_state:str) -> None:
        """Initializes the Layer. Initial state is input."""

        self.current_state = initial_state
    
    def __str__(self) -> str:
        """Converts the Layer to a string."""

        return str(self.current_state)
    
    def is_sliceable(self) -> bool:
        """Determines whether or not the Layer can slice/slash at the current position."""

        value = 0

        for piece in self.current_state:
            if piece in "12345678":
                value += 1
            elif piece in "ABCDEFGH":
                value += 2

            if value == 6:
                return True
            elif value > 6:
                return False

    def turn(self, amount:int) -> bool:
        """Rotates the Layer by an input amount."""

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
                else:
                    if amount != 0 or not self.is_sliceable():
                        print('LOGIC ERROR involving an incomplete turn detected!')
                        self.current_state = initial_state[::-1]
                        return False

                    return True
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
                else:
                    if amount != 0 or not self.is_sliceable():
                        print('LOGIC ERROR involving an incomplete turn detected!')
                        self.current_state = initial_state
                        return False

                    return True
        else:
            return True

#########################################################

sq1 = Square1()

print(f"\nBefore: {sq1}\n")
sq1.apply_alg("(-2,0)/ (-3,6)/ (0,-3)/ (0,-3)/ (5,-1)/ (-3,0)/ (0,-5)/ (0,-3)/ (0,-1)/ (0,-4)/ (4,0)/ (4,0)/ (0,-4)/ (6,0)")
print(f"\nAfter: {sq1}\n")