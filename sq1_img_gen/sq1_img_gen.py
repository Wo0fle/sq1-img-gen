import reflex as rx

############################################################

class FormState(rx.State):
    form_data:dict = {}
    U:bool = True
    E:bool = True
    D:bool = True

    def handle_submit(self, form_data:dict):
        """Handle the form submit."""
        self.form_data = form_data

    def change_U(self):
        self.U = not self.U

    def change_E(self):
        self.E = not self.E

    def change_D(self):
        self.D = not self.D

############################################################

def index():
    return rx.container(
        rx.color_mode.button(position="top-right"),

        rx.center(
            rx.vstack(
                rx.heading("Seby's Square-1 Image Generator",
                    margin_bottom="30px"
                ),

                rx.form.root(
                    rx.center(
                        rx.vstack(
                            rx.hstack(
                                rx.text_area(
                                    placeholder="/ (3,0) / (-3,-3) / (0,3) /",
                                    name="input",
                                    variant="surface",
                                    size="2",
                                    rows="6",
                                ),
                                rx.radio(
                                    ["Case", "Algorithm", "State"],
                                    default_value="Case",
                                    name="input_type",
                                    spacing="3"
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
                                        align="center"
                                    ),
                                ),
                            ),
                            rx.radio(
                                ["Normal", "Orientation", "Shape"],
                                default_value="Normal",
                                name="scheme",
                                direction="row",
                                spacing="5"
                            ),
                            rx.hstack(
                                rx.switch(
                                    name="include_U",
                                    on_change=FormState.change_U(),
                                    default_checked=True,
                                ),
                                rx.cond(
                                    FormState.U,
                                    rx.text("Include top layer"),
                                    rx.text("Do not include top layer"),
                                ),
                            ),
                            rx.hstack(
                                rx.switch(
                                    name="include_E",
                                    on_change=FormState.change_E(),
                                    default_checked=True,
                                ),
                                rx.cond(
                                    FormState.E,
                                    rx.text("Include equator"),
                                    rx.text("Do not include equator"),
                                ),
                            ),
                            rx.hstack(
                                rx.switch(
                                    name="include_D",
                                    on_change=FormState.change_D(),
                                    default_checked=True,
                                ),
                                rx.cond(
                                    FormState.D,
                                    rx.text("Include bottom layer"),
                                    rx.text("Do not include bottom layer"),
                                ),
                            ),
                            rx.accordion.root( # probably replace this with something else, i want to avoid fix_arrow.css (ideally)
                                rx.accordion.item(
                                    header="Advanced Settings",
                                    content=rx.center(
                                        rx.text("you'll eventually be able to edit color scheme, number pieces, other stuff"),

                                        color=rx.color_mode_cond(light="#000000", dark="#FFFFFF"),
                                    ),
                                ),

                                collapsible=True,
                                variant="ghost",
                            ),
                            rx.cond(
                                FormState.U | FormState.E | FormState.D,
                                rx.button(rx.icon("image"), "Generate", type="submit", margin_top="20px", size="3"),
                                rx.button(rx.icon("image"), "Generate", type="submit", margin_top="20px", size="3", disabled=True, variant="outline"),
                            )
                        ),
                    ),


                    on_submit=FormState.handle_submit,
                    reset_on_submit=False,
                ),

                rx.heading("Input"),
                rx.text(FormState.form_data.to_string()),
            ),
        ),

        padding="20px",
    )
        
############################################################

all_is_margin_auto = {
    "*": {
        "margin": "auto",
    },
}

app = rx.App(
    theme=rx.theme(appearance="dark"),
    accent_color="blue",
    style=all_is_margin_auto,
    stylesheets=["/fix_arrow.css"]
)
app.add_page(index)
