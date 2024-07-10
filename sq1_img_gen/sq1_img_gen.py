import reflex as rx
from modules.img_genner import generate_image


class FormState(rx.State):
    bordercolor: str = "0, 0, 0"
    topcolor: str = "40, 40, 40"
    bottomcolor: str = "255, 255, 255"
    frontcolor: str = "255, 0, 0"
    backcolor: str = "255, 165, 0"
    leftcolor: str = "0, 73, 255"
    rightcolor: str = "0, 255, 0"
    shapecolor: str = "100, 100, 100"
    extensionfactor: str = "1.2"
    form_data: dict = {
        "text_input": "",
        "input_type": "Case",
        "scheme": "Normal",
        "include_U": True,
        "include_E": True,
        "include_D": True,
        "img_orientation": "Vertical",
        "bordercolor": bordercolor,
        "topcolor": topcolor,
        "bottomcolor": bottomcolor,
        "frontcolor": frontcolor,
        "backcolor": backcolor,
        "leftcolor": leftcolor,
        "rightcolor": rightcolor,
        "shapecolor": shapecolor,
        "extensionfactor": extensionfactor,
    }
    img: str = ""
    

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        self.img = generate_image(form_data, 100)
    
    def handle_change(self, field_id: str, value: str):
        self.form_data[field_id] = value
        self.handle_submit(self.form_data)


@rx.page(title="Seby's Square-1 Image Generator")
def index():
    return rx.container(
        rx.center(rx.heading("Seby's Square-1 Image Generator"), margin_bottom="10px"),

        rx.center(rx.link(rx.hstack("Need help?", rx.icon("circle-help")), href="https://github.com/Wo0fle/sq1-img-gen/blob/main/README.md", target="_blank"), margin_bottom="40px"),

        rx.hstack(
            rx.center(
                rx.vstack(
                    rx.heading("Input", margin_bottom="30px"),
                    rx.form.root(
                        rx.center(
                            rx.vstack(
                                rx.hstack(
                                    rx.text_area(
                                        placeholder="Type your Case/Alg/State into here!",
                                        name="text_input",
                                        variant="surface",
                                        size="2",
                                        rows="6",
                                        on_change=lambda value: FormState.handle_change("text_input", value),
                                    ),
                                    rx.radio(
                                        ["Case", "Algorithm", "State"],
                                        default_value="Case",
                                        name="input_type",
                                        spacing="3",
                                        on_change=lambda value: FormState.handle_change("input_type", value),
                                    ),
                                    rx.dialog.root(
                                        rx.dialog.trigger(rx.link(rx.icon("circle-help"), href="#")),
                                        rx.dialog.content(
                                            rx.vstack(
                                                rx.text(rx.text.strong("Case: "), "Your input will solve the Square-1 in the generated image."),
                                                rx.text(rx.text.strong("Algorithm: "), "Your input will be applied to a solved Square-1 to generate the image."),
                                                rx.text(rx.text.strong("State: "), "Your inputted ", rx.link("sq1optim", href="https://www.jaapsch.net/puzzles/square1.htm#progs", is_external=True), " state will be the Square-1's state in the generated image."),
                                                rx.link(rx.hstack("Need help?", rx.icon("circle-help")), href="https://github.com/Wo0fle/sq1-img-gen/blob/main/README.md", target="_blank"),
                                            ),
                                        ),
                                    ),
                                ),
                                rx.radio(
                                    ["Normal", "Orientation", "Shape"],
                                    default_value="Normal",
                                    name="scheme",
                                    direction="row",
                                    spacing="5",
                                    margin_bottom="10px",
                                    on_change=lambda value: FormState.handle_change("scheme", value),
                                ),
                                rx.hstack(
                                    rx.checkbox(
                                        name="include_U",
                                        default_checked=True,
                                        on_change=lambda value: FormState.handle_change("include_U", value),
                                    ),
                                    rx.text("Include top layer")
                                ),
                                rx.hstack(
                                    rx.checkbox(
                                        name="include_E",
                                        default_checked=True,
                                        on_change=lambda value: FormState.handle_change("include_E", value),
                                    ),
                                    rx.text("Include equator")
                                ),
                                rx.hstack(
                                    rx.checkbox(
                                        name="include_D",
                                        default_checked=True,
                                        on_change=lambda value: FormState.handle_change("include_D", value),
                                    ),
                                    rx.text("Include bottom layer")
                                ),
                                rx.radio(
                                    ["Vertical", "Horizontal"],
                                    default_value="Vertical",
                                    name="img_orientation",
                                    direction="row",
                                    spacing="2",
                                    margin_top="10px",
                                    margin_bottom="10px",
                                    on_change=lambda value: FormState.handle_change("img_orientation", value),
                                ),
                                rx.divider(),
                                rx.vstack(
                                    rx.hstack(
                                        rx.text("Border color:"),
                                        rx.input(
                                            name="bordercolor",
                                            placeholder="Default: 0, 0, 0",
                                            value=FormState.bordercolor,
                                            on_change=lambda value: FormState.handle_change("bordercolor", value),
                                        ),
                                        rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=f"rgb({FormState.bordercolor})"),

                                        margin_top="10px",
                                    ),
                                    rx.html("<br>"),
                                    rx.hstack(rx.text("Top side color:"), rx.input(name="topcolor", placeholder="Default: 40, 40, 40", value=FormState.topcolor, on_change=lambda value: FormState.handle_change("topcolor", value)), rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=f"rgb({FormState.topcolor})")),
                                    rx.hstack(rx.text("Bottom side color:"), rx.input(name="bottomcolor", placeholder="Default: 255, 255, 255", value=FormState.bottomcolor, on_change=lambda value: FormState.handle_change("bottomcolor", value)), rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=f"rgb({FormState.bottomcolor})")),
                                    rx.hstack(rx.text("Front side color:"), rx.input(name="frontcolor", placeholder="Default: 255, 0, 0", value=FormState.frontcolor, on_change=lambda value: FormState.handle_change("frontcolor", value)), rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=f"rgb({FormState.frontcolor})")),
                                    rx.hstack(rx.text("Back side color:"), rx.input(name="backcolor", placeholder="Default: 255, 165, 0", value=FormState.backcolor, on_change=lambda value: FormState.handle_change("backcolor", value)), rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=f"rgb({FormState.backcolor})")),
                                    rx.hstack(rx.text("Left side color:"), rx.input(name="leftcolor", placeholder="Default: 0, 73, 255", value=FormState.leftcolor, on_change=lambda value: FormState.handle_change("leftcolor", value)), rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=f"rgb({FormState.leftcolor})")),
                                    rx.hstack(rx.text("Right side color:"), rx.input(name="rightcolor", placeholder="Default: 0, 255, 0", value=FormState.rightcolor, on_change=lambda value: FormState.handle_change("rightcolor", value)), rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=f"rgb({FormState.rightcolor})")),
                                    rx.html("<br>"),
                                    rx.hstack(rx.text("Shape color:"), rx.input(name="shapecolor", placeholder="Default: 100, 100, 100", value=FormState.shapecolor, on_change=lambda value: FormState.handle_change("shapecolor", value)), rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=f"rgb({FormState.shapecolor})")),
                                    rx.html("<br>"),
                                    rx.hstack(
                                        rx.text("Extension factor: "),
                                        rx.input(name="extensionfactor", placeholder="Default: 1.2", value=FormState.extensionfactor, on_change=lambda value: FormState.handle_change("extensionfactor", value)),
                                        rx.dialog.root(
                                            rx.dialog.trigger(rx.link(rx.icon("circle-help"), href="#")),
                                            rx.dialog.content(
                                                rx.vstack(
                                                    rx.text(rx.text.strong("Extension factor"), " refers to how far the front/back/left/right sides of pieces extend from the top/bottom sides."),
                                                    rx.text(rx.text.strong("Values above 1"), " lead to the sides sticking out of the top/bottom."),
                                                    rx.text(rx.text.strong("Values below 1"), " lead to the sides sticking into the top/bottom."),
                                                    rx.text(rx.text.strong("A value of 1"), " leads to no visible side colors on the top/bottom layers."),
                                                    rx.link(rx.hstack("Need help?", rx.icon("circle-help")), href="https://github.com/Wo0fle/sq1-img-gen/blob/main/README.md", target="_blank"),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),

                margin_bottom="30px",
                ),
            
            margin_top=0
            ),

            rx.vstack(
                rx.heading("Output", margin_top=0),
                rx.image(src=rx.get_upload_url(FormState.img)),
                rx.button(rx.icon("refresh-ccw"), "Reload Image", on_click=FormState.handle_submit(FormState.form_data), margin_top="20px", size="3"),

                margin_top=0
            ),
        
        margin_top=0,
        ),

        rx.logo(), rx.color_mode.button(position="bottom-right"),

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
