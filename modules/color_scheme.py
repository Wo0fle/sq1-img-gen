color_scheme_dict = {
    "A": "fl",
    "B": "lb",
    "C": "br",
    "D": "rf",
    "E": "fr",
    "F": "rb",
    "G": "bl",
    "H": "lf",
    "1": "l",
    "2": "b",
    "3": "r",
    "4": "f",
    "5": "f",
    "6": "r",
    "7": "b",
    "8": "l",
}


def get_color(color_list, piece, index=0):
    face = color_scheme_dict[piece][index]

    if face == "f":
        return color_list[0]
    elif face == "l":
        return color_list[1]
    elif face == "b":
        return color_list[2]
    elif face == "r":
        return color_list[3]
