import reflex as rx
import random

############################################################

class State(rx.State):
    form_data:dict = {}
    checked:bool = False

    def handle_submit(self, form_data:dict):
        """Handle the form submit."""
        self.form_data = form_data

    def change(self):
        self.checked = not self.checked

############################################################

def index():
    return rx.container(
        rx.color_mode.button(position="top-right"),

        rx.center(
            rx.vstack(
                rx.heading("Seby's Square-1 Image Generator",
                    margin="auto",
                    margin_bottom="20px"
                ),

                rx.form(
                    rx.center(
                        rx.vstack(
                            rx.hstack(
                                rx.text_area(
                                    placeholder="/ (3,0) / (-3,-3) / (0,3) /",
                                    name="input",
                                    variant="surface",
                                    size="2",
                                    rows="6",
                                    margin="auto"
                                ),
                                rx.radio(
                                    ["Case", "Algorithm", "State"],
                                    default_value="Case",
                                    margin="auto",
                                    name="input_type"
                                ),
                                rx.popover.root(
                                    rx.popover.trigger(rx.icon("circle-help"), margin="auto", _hover={"cursor": "pointer"}),
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
                            rx.hstack(
                                rx.switch(
                                    name="include_equator",
                                    on_change=State.change(),
                                    default_checked=True,
                                ),
                                rx.cond(
                                    State.checked,
                                    rx.text("Do not include equator"),
                                    rx.text("Include equator"),
                                ),

                                margin="auto"
                            ),
                            rx.button("Generate", type="submit", margin="auto"),
                        ),
                    ),


                    on_submit=State.handle_submit,
                    reset_on_submit=False,
                ),

                rx.heading("Input"),
                rx.text(State.form_data.to_string())
            ),

            wrap="wrap"
        ),


        size="2"
    )
        
############################################################

app = rx.App(
    theme=rx.theme(appearance="dark"), accent_color="blue"
)
app.add_page(index)
