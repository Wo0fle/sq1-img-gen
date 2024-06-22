import pygame as pg
import math
from virtual_sq1 import Square1
from modules.color_scheme import get_color


def center(vector, new_center):
    "Returns a new vector centered at `new_center`."
    return [new_center[0]+vector[0], new_center[1]+vector[1]]


def darken(color):
    darkening_attempt = [i-100 for i in color]
    actually_darkened_color = []

    for value in darkening_attempt:
        if value < 0:
            actually_darkened_color.append(0)
        else:
            actually_darkened_color.append(value)

    return actually_darkened_color

def generate_image(form_data, img_width, path_to_save_to):
    """Generate Square-1 image using `form_data`."""
    squan = Square1()

    if form_data["input_type"] == "Case":
        squan.apply_alg(form_data["text_input"], True)
    elif form_data["input_type"] == "Algorithm":
        squan.apply_alg(form_data["text_input"])
    else:
        squan.apply_state(form_data["text_input"])

    border_color = (0, 0, 0)

    top_color = (20, 20, 20)
    bottom_color = (255, 255, 255)
    front_color = (255, 0, 0)
    back_color = (255, 165, 0)
    left_color = (0, 73, 255)
    right_color = (0, 255, 0)

    shape_color = (90, 90, 90)

    color_list = [front_color, left_color, back_color, right_color]

    img_height = img_width * 2
    img_size = img_width, img_height
    padding = img_width // 9

    cube_side_length = img_width - 4*padding
    half_edge_length = (cube_side_length/2)*(math.tan(15*(math.pi/180)))
    piece_height = (cube_side_length/2)
    half_diag_length = cube_side_length*math.sqrt(2)*0.5
    corner_side_length = piece_height - half_edge_length

    center_coord = [i/2 for i in img_size]
    top_center_coord = [center_coord[0], padding+half_diag_length]
    bottom_center_coord = [center_coord[0], img_height-(padding+half_diag_length)]

    border_thickness = int((1/100)*img_width)

    edge_vector = pg.math.Vector2(-half_edge_length, piece_height)
    half_diag_vector = pg.math.Vector2(-cube_side_length/2, cube_side_length/2)

    # initialize
    pg.init()
    window = pg.Surface(img_size). # check if it works, otherwise use pg.display.set_mode(img_size)
    window.fill((255, 255, 255))

    # draw top
    rotate_by = 0

    for piece in squan.top.__str__():
        if piece in "ABCDEFGH":
            if form_data["scheme"] != "Shape":
                if piece in "ABCD":
                    current_color = top_color
                else:
                    current_color = bottom_color
            else:
                current_color = shape_color

            pg.draw.polygon(
                window,
                current_color,
                [
                    top_center_coord,
                    center(edge_vector.rotate(rotate_by), top_center_coord),
                    center(half_diag_vector.rotate(rotate_by), top_center_coord),
                    center(edge_vector.rotate(rotate_by+60), top_center_coord),
                ]
            )
            pg.draw.polygon(
                window,
                border_color,
                [
                    top_center_coord,
                    center(edge_vector.rotate(rotate_by), top_center_coord),
                    center(half_diag_vector.rotate(rotate_by), top_center_coord),
                    center(edge_vector.rotate(rotate_by+60), top_center_coord),
                ],
                border_thickness
            )

            if form_data["scheme"] == "Normal":
                pg.draw.line(
                    window,
                    get_color(color_list, piece),
                    center(edge_vector.rotate(rotate_by), top_center_coord),
                    center(half_diag_vector.rotate(rotate_by), top_center_coord),
                    2*border_thickness,
                )
                pg.draw.line(
                    window,
                    get_color(color_list, piece, 1),
                    center(half_diag_vector.rotate(rotate_by), top_center_coord),
                    center(edge_vector.rotate(rotate_by+60), top_center_coord),
                    2*border_thickness,
                )

            rotate_by += 60
        else:
            if form_data["scheme"] != "Shape":
                if piece in "1234":
                    current_color = top_color
                else:
                    current_color = bottom_color
            else:
                current_color = shape_color

            pg.draw.polygon(
                window,
                current_color,
                [
                    top_center_coord,
                    center(edge_vector.rotate(rotate_by), top_center_coord),
                    center(edge_vector.rotate(rotate_by+30), top_center_coord),
                ]
            )
            pg.draw.polygon(
                window,
                border_color,
                [
                    top_center_coord,
                    center(edge_vector.rotate(rotate_by), top_center_coord),
                    center(edge_vector.rotate(rotate_by+30), top_center_coord),
                ],
                border_thickness
            )

            if form_data["scheme"] == "Normal":
                pg.draw.line(
                    window,
                    get_color(color_list, piece),
                    center(edge_vector.rotate(rotate_by), top_center_coord),
                    center(edge_vector.rotate(rotate_by+30), top_center_coord),
                    2*border_thickness,
                )

            rotate_by += 30

    # draw equator
    if form_data["scheme"] != "Normal":
        left_eq_color = shape_color
        right_eq_color = shape_color
        left_border_color = border_color
        right_border_color = border_color
    else:
        left_eq_color = front_color
        left_border_color = front_color
        right_eq_color = front_color
        right_border_color = front_color

        if squan.equator_flipped:
            right_eq_color = back_color
            right_border_color = back_color

    pg.draw.polygon(
        window,
        left_eq_color,
        [
            (center_coord[0]-half_edge_length, center_coord[1]-half_edge_length),
            (center_coord[0]-half_edge_length, center_coord[1]+half_edge_length),
            (center_coord[0]-piece_height, center_coord[1]+half_edge_length),
            (center_coord[0]-piece_height, center_coord[1]-half_edge_length),
        ],
    )
    pg.draw.polygon(
        window,
        darken(left_border_color),
        [
            (center_coord[0]-half_edge_length, center_coord[1]-half_edge_length),
            (center_coord[0]-half_edge_length, center_coord[1]+half_edge_length),
            (center_coord[0]-piece_height, center_coord[1]+half_edge_length),
            (center_coord[0]-piece_height, center_coord[1]-half_edge_length),
        ],
        border_thickness,
    )

    if not squan.equator_flipped:
        pg.draw.polygon(
            window,
            right_eq_color,
            [
                (center_coord[0]-half_edge_length, center_coord[1]-half_edge_length),
                (center_coord[0]-half_edge_length, center_coord[1]+half_edge_length),
                (center_coord[0]+piece_height, center_coord[1]+half_edge_length),
                (center_coord[0]+piece_height, center_coord[1]-half_edge_length),
            ],
        )
        pg.draw.polygon(
            window,
            darken(right_border_color),
            [
                (center_coord[0]-half_edge_length, center_coord[1]-half_edge_length),
                (center_coord[0]-half_edge_length, center_coord[1]+half_edge_length),
                (center_coord[0]+piece_height, center_coord[1]+half_edge_length),
                (center_coord[0]+piece_height, center_coord[1]-half_edge_length),
            ],
            border_thickness,
        )
    else:
        pg.draw.polygon(
            window,
            right_eq_color,
            [
                (center_coord[0]-half_edge_length, center_coord[1]-half_edge_length),
                (center_coord[0]-half_edge_length, center_coord[1]+half_edge_length),
                (center_coord[0]-half_edge_length+corner_side_length, center_coord[1]+half_edge_length),
                (center_coord[0]-half_edge_length+corner_side_length, center_coord[1]-half_edge_length),
            ],
        )
        pg.draw.polygon(
            window,
            darken(right_border_color),
            [
                (center_coord[0]-half_edge_length, center_coord[1]-half_edge_length),
                (center_coord[0]-half_edge_length, center_coord[1]+half_edge_length),
                (center_coord[0]-half_edge_length+corner_side_length, center_coord[1]+half_edge_length),
                (center_coord[0]-half_edge_length+corner_side_length, center_coord[1]-half_edge_length),
            ],
            border_thickness,
        )

    # draw bottom
    rotate_by = 150

    for piece in squan.bottom.__str__():
        if piece in "ABCDEFGH":
            if form_data["scheme"] != "Shape":
                if piece in "ABCD":
                    current_color = top_color
                else:
                    current_color = bottom_color
            else:
                current_color = shape_color

            pg.draw.polygon(
                window,
                current_color,
                [
                    bottom_center_coord,
                    center(edge_vector.rotate(rotate_by), bottom_center_coord),
                    center(half_diag_vector.rotate(rotate_by), bottom_center_coord),
                    center(edge_vector.rotate(rotate_by+60), bottom_center_coord),
                ]
            )
            pg.draw.polygon(
                window,
                border_color,
                [
                    bottom_center_coord,
                    center(edge_vector.rotate(rotate_by), bottom_center_coord),
                    center(half_diag_vector.rotate(rotate_by), bottom_center_coord),
                    center(edge_vector.rotate(rotate_by+60), bottom_center_coord),
                ],
                border_thickness
            )

            if form_data["scheme"] == "Normal":
                pg.draw.line(
                    window,
                    get_color(color_list, piece),
                    center(edge_vector.rotate(rotate_by), bottom_center_coord),
                    center(half_diag_vector.rotate(rotate_by), bottom_center_coord),
                    2*border_thickness,
                )
                pg.draw.line(
                    window,
                    get_color(color_list, piece, 1),
                    center(half_diag_vector.rotate(rotate_by), bottom_center_coord),
                    center(edge_vector.rotate(rotate_by+60), bottom_center_coord),
                    2*border_thickness,
                )

            rotate_by += 60
        else:
            if form_data["scheme"] != "Shape":
                if piece in "1234":
                    current_color = top_color
                else:
                    current_color = bottom_color
            else:
                current_color = shape_color

            pg.draw.polygon(
                window,
                current_color,
                [
                    bottom_center_coord,
                    center(edge_vector.rotate(rotate_by), bottom_center_coord),
                    center(edge_vector.rotate(rotate_by+30), bottom_center_coord),
                ]
            )
            pg.draw.polygon(
                window,
                border_color,
                [
                    bottom_center_coord,
                    center(edge_vector.rotate(rotate_by), bottom_center_coord),
                    center(edge_vector.rotate(rotate_by+30), bottom_center_coord),
                ],
                border_thickness
            )

            if form_data["scheme"] == "Normal":
                pg.draw.line(
                    window,
                    get_color(color_list, piece),
                    center(edge_vector.rotate(rotate_by), bottom_center_coord),
                    center(edge_vector.rotate(rotate_by+30), bottom_center_coord),
                    2*border_thickness,
                )

            rotate_by += 30

    # finalize
    pg.display.update()
    pg.image.save(window, "assets"+path_to_save_to)
    pg.quit()
