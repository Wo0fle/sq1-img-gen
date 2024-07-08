import reflex as rx
from modules.img_genner import generate_image


class FormState(rx.State):
    form_data: dict = {}
    u_layer: bool = True
    e_layer: bool = True
    d_layer: bool = True
    img: str = ""

    def handle_submit(self, form_data: dict):
        self.img = generate_image(form_data, 100)
  
    def change_U(self):
        self.u_layer = not self.u_layer

    def change_E(self):
        self.e_layer = not self.e_layer

    def change_D(self):
        self.d_layer = not self.d_layer


@rx.page(title="Seby's Square-1 Image Generator")
def index():
    return rx.container(
        rx.color_mode.button(position="top-right"),

        rx.center(rx.heading("Seby's Square-1 Image Generator"), margin_bottom="50px"),

        rx.hstack(
            rx.center(
                rx.vstack(
                    rx.heading("Input", margin_bottom="30px"),
                    rx.form.root(
                        rx.center(
                            rx.vstack(
                                rx.hstack(
                                    rx.text_area(
                                        placeholder="/ (3,0) / (-3,-3) / (0,3) /",
                                        name="text_input",
                                        variant="surface",
                                        size="2",
                                        rows="6",
                                    ),
                                    rx.radio(
                                        ["Case", "Algorithm", "State"],
                                        default_value="Case",
                                        name="input_type",
                                        spacing="3",
                                    ),
                                    rx.popover.root(
                                        rx.popover.trigger(rx.icon("circle-help"), _hover={"cursor": "pointer"}),
                                        rx.popover.content(
                                            rx.vstack(
                                                rx.text(rx.text.strong("Case: "), "Your input will solve the Square-1 in the generated image."),
                                                rx.text(rx.text.strong("Algorithm: "), "Your input will be applied to a solved Square-1 to generate the image."),
                                                rx.text(rx.text.strong("State: "), "Your inputted ", rx.link("sq1optim", href="https://www.jaapsch.net/puzzles/square1.htm#progs", is_external=True), " state will be the Square-1's state in the generated image."),
                                            ),

                                            side="right",
                                            align="center",
                                        ),
                                    ),
                                ),
                                rx.radio(
                                    ["Normal", "Orientation", "Shape"],
                                    default_value="Normal",
                                    name="scheme",
                                    direction="row",
                                    spacing="5",
                                    margin_bottom="10px"
                                ),
                                rx.hstack(
                                    rx.checkbox(
                                        name="include_U",
                                        on_change=FormState.change_U(),
                                        default_checked=True,
                                    ),
                                    rx.text("Include top layer")
                                ),
                                rx.hstack(
                                    rx.checkbox(
                                        name="include_E",
                                        on_change=FormState.change_E(),
                                        default_checked=True,
                                    ),
                                    rx.text("Include equator")
                                ),
                                rx.hstack(
                                    rx.checkbox(
                                        name="include_D",
                                        on_change=FormState.change_D(),
                                        default_checked=True,
                                    ),
                                    rx.text("Include bottom layer")
                                ),
                                rx.radio(
                                    ["Vertical", "Horizontal"],
                                    default_value="Vertical",
                                    name="img_orientation",
                                    direction="row",
                                    spacing="2",
                                    margin_top="10px"
                                ),
                                rx.cond(
                                    FormState.u_layer | FormState.e_layer | FormState.d_layer,
                                    rx.button(rx.icon("image"), "Generate", type="submit", margin_top="20px", size="3"),
                                    rx.button(rx.icon("image"), "Generate", margin_top="20px", size="3", disabled=True, variant="outline"),
                                ),
                            ),
                        ),


                        on_submit=FormState.handle_submit,
                        reset_on_submit=False,
                    ),

                margin_bottom="30px",
                ),
            
            margin_top=0
            ),

            rx.vstack(
                rx.heading("Output", margin_top=0),
                rx.image(src=rx.get_upload_url(FormState.img)),

                margin_top=0
            ),
        
        margin_top=0,
        ),

        padding="20px",
    )


all_is_margin_auto = {
    "*": {
        "margin": "auto",
    },
}

app = rx.App(
    theme=rx.theme(appearance="dark"),
    accent_color="blue",
    style=all_is_margin_auto,
)
app.add_page(index)
