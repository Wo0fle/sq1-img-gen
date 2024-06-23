import drawsvg as draw
import math
from virtual_sq1 import Square1
from modules.color_scheme import get_color


def darken(color):
    darkening_attempt = [i-100 for i in color]
    actually_darkened_color = []

    for value in darkening_attempt:
        if value < 0:
            actually_darkened_color.append(0)
        else:
            actually_darkened_color.append(value)

    return tuple(actually_darkened_color)


def generate_image(form_data, img_width, path_to_save_to):
    """
    Generate Square-1 image of width `img_width` (in pixels)
    using `form_data` and save to "assets" + `path_to_save_to`.
    """

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
    padding = img_width // 9

    cube_side_length = img_width - 4*padding
    half_edge_length = (cube_side_length/2)*(math.tan(15*(math.pi/180)))
    edge_height = (cube_side_length/2)
    half_diag_length = cube_side_length*math.sqrt(2)*0.5
    corner_side_length = edge_height - half_edge_length

    border_thickness = int((1/175)*img_width)

    edge_vector = [-half_edge_length, edge_height]
    half_diag_vector = [-cube_side_length/2, cube_side_length/2]


    # init
    d = draw.Drawing(img_width, img_height, origin='center')

    # draw top
    rotate_by = 0

    if form_data.get("include_U") == "on":
        for piece in squan.top.__str__():
            translate = f"translate(0,{-cube_side_length})"
            rotation= f"rotate({rotate_by})"

            if piece in "ABCDEFGH":
                if form_data["scheme"] != "Shape":
                    if piece in "ABCD":
                        current_color = top_color
                    else:
                        current_color = bottom_color
                else:
                    current_color = shape_color

                d.append(draw.Lines(0, 0,
                                    edge_vector[0], edge_vector[1],
                                    half_diag_vector[0], half_diag_vector[1],
                                    half_diag_vector[0], -edge_vector[0],
                                    close=True,
                                    fill=f"rgb{current_color}",
                                    stroke=f"rgb{border_color}", stroke_width=border_thickness,
                                    transform=f"{translate} {rotation}"))

                if form_data["scheme"] == "Normal":
                    d.append(draw.Line(
                                    edge_vector[0], edge_vector[1],
                                    half_diag_vector[0], half_diag_vector[1],
                                    stroke=f"rgb{get_color(color_list, piece)}", stroke_width=3*border_thickness,
                                    transform=f"{translate} {rotation}"
                                ))
                    d.append(draw.Line(
                                    half_diag_vector[0], half_diag_vector[1],
                                    half_diag_vector[0], -edge_vector[0],
                                    stroke=f"rgb{get_color(color_list, piece, 1)}", stroke_width=3*border_thickness,
                                    transform=f"{translate} {rotation}"
                                ))

                rotate_by += 60
            else:
                if form_data["scheme"] != "Shape":
                    if piece in "1234":
                        current_color = top_color
                    else:
                        current_color = bottom_color
                else:
                    current_color = shape_color

                d.append(draw.Lines(0, 0,
                                    edge_vector[0], edge_vector[1],
                                    edge_vector[0]-(2*half_edge_length*math.cos(30*math.pi/180)), edge_vector[1]-(2*half_edge_length*math.sin(30*math.pi/180)),
                                    close=True,
                                    fill=f"rgb{current_color}",
                                    stroke=f"rgb{border_color}", stroke_width=border_thickness,
                                    transform=f"{translate} {rotation}"))

                if form_data["scheme"] == "Normal":
                    d.append(draw.Line(
                                        edge_vector[0], edge_vector[1],
                                        edge_vector[0]-(2*half_edge_length*math.cos(30*math.pi/180)), edge_vector[1]-(2*half_edge_length*math.sin(30*math.pi/180)),
                                        stroke=f"rgb{get_color(color_list, piece)}", stroke_width=3*border_thickness,
                                        transform=f"{translate} {rotation}"))

                rotate_by += 30

    # draw equator
    if form_data.get("include_E") == "on":
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

        d.append(draw.Rectangle(-cube_side_length/2, -half_edge_length,
                                corner_side_length, (2*half_edge_length),
                                fill=f"rgb{left_eq_color}",
                                stroke=f"rgb{darken(left_border_color)}", stroke_width=border_thickness))

        if not squan.equator_flipped:
            d.append(draw.Rectangle(-half_edge_length, -half_edge_length,
                                corner_side_length+(2*half_edge_length), (2*half_edge_length),
                                fill=f"rgb{right_eq_color}",
                                stroke=f"rgb{darken(right_border_color)}", stroke_width=border_thickness))
        else:
            d.append(draw.Rectangle(-half_edge_length, -half_edge_length,
                                corner_side_length, (2*half_edge_length),
                                fill=f"rgb{right_eq_color}",
                                stroke=f"rgb{darken(right_border_color)}", stroke_width=border_thickness))

    # draw top
    rotate_by = 150

    if form_data.get("include_D") == "on":
        for piece in squan.bottom.__str__():
            translate = f"translate(0,{cube_side_length})"
            rotation= f"rotate({rotate_by})"

            if piece in "ABCDEFGH":
                if form_data["scheme"] != "Shape":
                    if piece in "ABCD":
                        current_color = top_color
                    else:
                        current_color = bottom_color
                else:
                    current_color = shape_color

                d.append(draw.Lines(0, 0,
                                    edge_vector[0], edge_vector[1],
                                    half_diag_vector[0], half_diag_vector[1],
                                    half_diag_vector[0], -edge_vector[0],
                                    close=True,
                                    fill=f"rgb{current_color}",
                                    stroke=f"rgb{border_color}", stroke_width=border_thickness,
                                    transform=f"{translate} {rotation}"))

                if form_data["scheme"] == "Normal":
                    d.append(draw.Line(
                                    edge_vector[0], edge_vector[1],
                                    half_diag_vector[0], half_diag_vector[1],
                                    stroke=f"rgb{get_color(color_list, piece)}", stroke_width=3*border_thickness,
                                    transform=f"{translate} {rotation}"
                                ))
                    d.append(draw.Line(
                                    half_diag_vector[0], half_diag_vector[1],
                                    half_diag_vector[0], -edge_vector[0],
                                    stroke=f"rgb{get_color(color_list, piece, 1)}", stroke_width=3*border_thickness,
                                    transform=f"{translate} {rotation}"
                                ))

                rotate_by += 60
            else:
                if form_data["scheme"] != "Shape":
                    if piece in "1234":
                        current_color = top_color
                    else:
                        current_color = bottom_color
                else:
                    current_color = shape_color

                d.append(draw.Lines(0, 0,
                                    edge_vector[0], edge_vector[1],
                                    edge_vector[0]-(2*half_edge_length*math.cos(30*math.pi/180)), edge_vector[1]-(2*half_edge_length*math.sin(30*math.pi/180)),
                                    close=True,
                                    fill=f"rgb{current_color}",
                                    stroke=f"rgb{border_color}", stroke_width=border_thickness,
                                    transform=f"{translate} {rotation}"))

                if form_data["scheme"] == "Normal":
                    d.append(draw.Line(
                                        edge_vector[0], edge_vector[1],
                                        edge_vector[0]-(2*half_edge_length*math.cos(30*math.pi/180)), edge_vector[1]-(2*half_edge_length*math.sin(30*math.pi/180)),
                                        stroke=f"rgb{get_color(color_list, piece)}", stroke_width=3*border_thickness,
                                        transform=f"{translate} {rotation}"))

                rotate_by += 30

    d.save_svg("assets"+path_to_save_to)
