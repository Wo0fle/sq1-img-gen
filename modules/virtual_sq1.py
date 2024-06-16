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
        """
        If `for_case = False` (default): Applies an input algorithm `alg` to the Square1, starting from a solved state.

        If `for_case = True`: Changes the Square1's state so that the input algorithm `alg` solves it (by inverting the input algorithm and then applying it).
        """

        self.__init__()

        simplfied_alg = list(alg)

        for char in alg:
            if not char.isnumeric() and ((char != '/') and (char != ',') and (char != '-')):
                simplfied_alg.remove(char)

        simplfied_alg = [slash.split(',') for slash in (''.join(simplfied_alg)).split('/')]

        if for_case:
            simplfied_alg = self.invert_alg(simplfied_alg)

        legal = True

        for i in range(len(simplfied_alg)):
            try:
                turn_amount = int(simplfied_alg[i][0])

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
                if simplfied_alg[i][0] != '':
                    print('SYNTAX ERROR involving "-" detected!')
                    self.__init__()
                    legal = False
                    break
            
            try:
                turn_amount = int(simplfied_alg[i][1])

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
                if simplfied_alg[i][1] != '':
                    print('SYNTAX ERROR involving "-" detected!')
                    self.__init__()
                    legal = False
                    break
            except:
                pass # assume 0 for bottom turn if there's only one input
            
            if len(simplfied_alg[i]) > 2:
                print('SYNTAX ERROR involving "," detected!')
                self.__init__()
                legal = False
                break

            self.slash()

        if legal:
            self.slash()
        else:
            if for_case:
                self.error_detected(0, simplfied_alg[i], i, simplfied_alg)
            else:
                self.error_detected(1, simplfied_alg[i], i, simplfied_alg)
    
    def invert_alg(self, simplified_alg:list) -> list:
        """Inverts the input simplified algorithm `simplified_alg`."""
        
        simplified_alg = simplified_alg[::-1]

        for i in range(len(simplified_alg)):
            for j in range(len(simplified_alg[i])):
                if "-" in simplified_alg[i][j]:
                    simplified_alg[i][j] = simplified_alg[i][j].replace('-', '', 1)
                else:
                    if simplified_alg[i][j] != '0' and simplified_alg[i][j] != '':
                        simplified_alg[i][j] = "-" + simplified_alg[i][j]

        return simplified_alg

    def apply_state(self, state:str) -> None:
        """Changes the Square1's state to match the input state `state`."""

        req_pieces = "ABCDEFGH12345678"
        state = state.upper()
        state_list = list(state)

        self.__init__()
        
        for piece in req_pieces:
            if piece in state_list:
                state_list.remove(piece)
        
        if len(state_list) > 1:
            print('SYNTAX ERROR involving extra/nonexistent pieces detected!')
            self.__init__()
            #self.error_detected(2, )
        else:
            value = 0

            if len(state_list) == 1:
                state_list = list(state)

                if "/" in state:
                    self.flip_equator()
                    state_list = list(state)
                    state_list.remove("/")
                elif "|" in state:
                    state_list = list(state)
                    state_list.remove("|")
            else:
                state_list = list(state)
            
            for i in range(len(state)):
                if state[i] in "12345678":
                    value += 1
                elif state[i] in "ABCDEFGH":
                    value += 2

                if value == 12:
                    new_top = ''.join(state_list[:i+1])
                    new_bottom = ''.join(state_list[i+1:])

                    self.top = Layer(new_top)
                    self.bottom = Layer(new_bottom)

                    break
                elif value > 12:
                    print('SYNTAX ERROR involving impossible layer state detected!')
                    self.__init__()
                    #self.error_detected(2, )
                    break
        
    def error_detected(self, input_type:int, error_turns:list, error_turns_index:int, error_simplfied_alg:list) -> None:
        """
        Prints an error message depending on the input type `input_type` (where 0 is "Case", 1 is "Algorithm", and 2 is "State").
        
        All other parameters (`error_turns`, `error_turns_index`, `error_simplfied_alg`) are the specifics of where the error occurred, and depend on the `input_type`.
        """
        if input_type == 0: # case
            self.invert_alg(error_simplfied_alg)

            print(f'Error at "{','.join(error_turns)}" (move #{len(error_simplfied_alg) - error_turns_index}).\nSquare-1 reset.')
        elif input_type == 1: # alg
            print(f'Error at "{','.join(error_turns)}" (move #{error_turns_index + 1}).\nSquare-1 reset.')
        elif input_type == 2: # state
            ...

#########################################################

class Layer:
    """An arbitrary layer of the Square1."""

    def __init__(self, initial_state:str) -> None:
        """Initializes the Layer. Initial state `initial_state` is input."""

        self.current_state = initial_state
    
    def __str__(self) -> str:
        """Converts the Layer to a string."""

        return str(self.current_state)
    
    def is_sliceable(self):
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

    def turn(self, amount:int):
        """Rotates the Layer by an input amount `amount`."""

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
sq1.apply_state("4h675dae|21gbc3f8")
print(f"\nAfter: {sq1}\n")