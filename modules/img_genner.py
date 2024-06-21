import pygame as pg
import math


def generate_image(state, scheme, include_U, include_E, include_D):
    """Generate Square-1 image using all those thingies"""
    ...

img_side_length = 600
padding = img_side_length // 10
internal_side_length = img_side_length - 2*padding

img_size = img_side_length, img_side_length
center_coord = [i//2 for i in img_size]

black = (0, 0, 0)
thickness = 5
half_edge_length = (internal_side_length/2)*(math.tan(15*(math.pi/180)))
piece_height = (internal_side_length/2)

edge_vector = pg.math.Vector2(-half_edge_length, piece_height)
half_diag_vector = pg.math.Vector2(-internal_side_length/2, internal_side_length/2)


def center(vector, new_center):
    return [new_center[0]+vector[0], new_center[1]+vector[1]]


# initialize
pg.init()
window = pg.display.set_mode(img_size)
window.fill((255, 255, 255))

# draw cube
test_state = "AB12345678"
rotate_by = 0

for piece in test_state:
    if piece in "ABCDEFGH":
        pg.draw.polygon(
            window,
            black,
            [
                center_coord,
                center(edge_vector.rotate(rotate_by), center_coord),
                center(half_diag_vector.rotate(rotate_by), center_coord),
                center(edge_vector.rotate(rotate_by+60),center_coord),
            ],
            thickness
        )
        rotate_by += 60
    else:
        pg.draw.polygon(
            window,
            black,
            [
                center_coord,
                center(edge_vector.rotate(rotate_by), center_coord),
                center(edge_vector.rotate(rotate_by+30),center_coord),
            ],
            thickness
        )
        rotate_by += 30

# finalize
pg.display.update()
pg.image.save(window, "assets/image.png")
pg.quit()
