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
    extensionfactor: str = "1.25"
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
        "sliceindicator": True,
    }
    img: str = ""
    png: str = ""
    svg: str = ""
    error_message: str = ""

    @rx.event
    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        self.img, self.error_message = generate_image(form_data, 100)
        self.png = self.img  + ".png"
        self.svg = self.img  + ".svg"
    
    @rx.event
    def handle_change(self, field_id: str, value: str):
        self.form_data[field_id] = value
        self.handle_submit(self.form_data)
    
    @rx.var
    def bordercolor_rgb(self) -> str:
        return f"rgb({self.form_data["bordercolor"]})"
    
    @rx.var
    def topcolor_rgb(self) -> str:
        return f"rgb({self.form_data["topcolor"]})"
    
    @rx.var
    def bottomcolor_rgb(self) -> str:
        return f"rgb({self.form_data["bottomcolor"]})"
    
    @rx.var
    def frontcolor_rgb(self) -> str:
        return f"rgb({self.form_data["frontcolor"]})"
    
    @rx.var
    def backcolor_rgb(self) -> str:
        return f"rgb({self.form_data["backcolor"]})"
    
    @rx.var
    def leftcolor_rgb(self) -> str:
        return f"rgb({self.form_data["leftcolor"]})"
    
    @rx.var
    def rightcolor_rgb(self) -> str:
        return f"rgb({self.form_data["rightcolor"]})"
    
    @rx.var
    def shapecolor_rgb(self) -> str:
        return f"rgb({self.form_data["shapecolor"]})"
    
    @rx.var
    def whathappen(self) -> str:
        if self.error_message == "":
            return self.error_message
        else:
            return self.error_message[:-34]
            


@rx.page(title="Seby's Square-1 Image Generator")
def index():
    return rx.container(
        rx.center(rx.heading("Seby's Square-1 Image Generator"), margin_bottom="10px"),

        rx.center(rx.link(rx.hstack("Need help?", rx.icon("circle-help")), href="https://github.com/Wo0fle/sq1-img-gen/blob/main/README.md", target="_blank"), margin_bottom="40px"),

        rx.hstack(
            rx.center(
                rx.vstack(
                    rx.heading("Input", margin="auto", margin_bottom="30px"),
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
                                        direction="column",
                                        name="input_type",
                                        spacing="3",
                                        on_change=lambda value: FormState.handle_change("input_type", value),
                                        margin="auto", 
                                    ),
                                    rx.dialog.root(
                                        rx.dialog.trigger(rx.link(rx.icon("circle-help"), href="#"),margin="auto"),
                                        rx.dialog.content(
                                            rx.vstack(
                                                rx.text(rx.text.strong("Case: "), "Your input will solve the Square-1 in the generated image."),
                                                rx.text(rx.text.strong("Algorithm: "), "Your input will be applied to a solved Square-1 to generate the image."),
                                                rx.text(rx.text.strong("State: "), "Your inputted ", rx.link("sq1optim", href="https://www.jaapsch.net/puzzles/square1.htm#progs", is_external=True), " state will be the Square-1's state in the generated image."),
                                                rx.link(rx.hstack("Need help?", rx.icon("circle-help")), href="https://github.com/Wo0fle/sq1-img-gen/blob/main/README.md", target="_blank",margin="auto"),
                                            ),
                                        ),
                                    ),
                                
                                margin="auto"
                                ),
                                rx.radio(
                                    ["Normal", "Orientation", "Shape"],
                                    default_value="Normal",
                                    name="scheme",
                                    spacing="5",
                                    margin="auto", 
                                    margin_bottom="10px",
                                    on_change=lambda value: FormState.handle_change("scheme", value),
                                ),
                                rx.hstack(
                                    rx.checkbox(
                                        name="include_U",
                                        default_checked=True,
                                        on_change=lambda value: FormState.handle_change("include_U", value),
                                    ),
                                    rx.text("Include top layer"),
                                    margin="auto", 
                                ),
                                rx.hstack(
                                    rx.checkbox(
                                        name="include_E",
                                        default_checked=True,
                                        on_change=lambda value: FormState.handle_change("include_E", value),
                                    ),
                                    rx.text("Include equator"),
                                    margin="auto", 
                                ),
                                rx.hstack(
                                    rx.checkbox(
                                        name="include_D",
                                        default_checked=True,
                                        on_change=lambda value: FormState.handle_change("include_D", value),
                                    ),
                                    rx.text("Include bottom layer"),
                                    margin="auto", 
                                ),
                                rx.radio(
                                    ["Vertical", "Horizontal"],
                                    default_value="Vertical",
                                    name="img_orientation",
                                    direction="row",
                                    spacing="2",
                                    margin="auto", 
                                    margin_top="10px",
                                    margin_bottom="10px",
                                    on_change=lambda value: FormState.handle_change("img_orientation", value),
                                ),
                                rx.divider(),
                                rx.vstack(
                                    rx.hstack(
                                        rx.text("Border color:",margin="auto", ),
                                        rx.input(
                                            name="bordercolor",
                                            placeholder="Default: 0, 0, 0",
                                            value=FormState.bordercolor,
                                            on_change=lambda value: FormState.handle_change("bordercolor", value),
                                        ),
                                        rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=FormState.bordercolor_rgb, margin="auto",),

                                        margin_top="10px",
                                    ),
                                    rx.html("<br>"),
                                    rx.hstack(rx.text("Top side color:",margin="auto"), rx.input(name="topcolor", placeholder="Default: 40, 40, 40", value=FormState.topcolor, on_change=lambda value: FormState.handle_change("topcolor", value)), rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=FormState.topcolor_rgb,margin="auto")),
                                    rx.hstack(rx.text("Bottom side color:",margin="auto"), rx.input(name="bottomcolor", placeholder="Default: 255, 255, 255", value=FormState.bottomcolor, on_change=lambda value: FormState.handle_change("bottomcolor", value)), rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=FormState.bottomcolor_rgb,margin="auto")),
                                    rx.hstack(rx.text("Front side color:",margin="auto"), rx.input(name="frontcolor", placeholder="Default: 255, 0, 0", value=FormState.frontcolor, on_change=lambda value: FormState.handle_change("frontcolor", value)), rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=FormState.frontcolor_rgb,margin="auto")),
                                    rx.hstack(rx.text("Back side color:",margin="auto"), rx.input(name="backcolor", placeholder="Default: 255, 165, 0", value=FormState.backcolor, on_change=lambda value: FormState.handle_change("backcolor", value)), rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=FormState.backcolor_rgb,margin="auto")),
                                    rx.hstack(rx.text("Left side color:",margin="auto"), rx.input(name="leftcolor", placeholder="Default: 0, 73, 255", value=FormState.leftcolor, on_change=lambda value: FormState.handle_change("leftcolor", value)), rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=FormState.leftcolor_rgb,margin="auto")),
                                    rx.hstack(rx.text("Right side color:",margin="auto"), rx.input(name="rightcolor", placeholder="Default: 0, 255, 0", value=FormState.rightcolor, on_change=lambda value: FormState.handle_change("rightcolor", value)), rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=FormState.rightcolor_rgb,margin="auto")),
                                    rx.html("<br>"),
                                    rx.hstack(rx.text("Shape color:",margin="auto"), rx.input(name="shapecolor", placeholder="Default: 100, 100, 100", value=FormState.shapecolor, on_change=lambda value: FormState.handle_change("shapecolor", value)), rx.box(width="15px", height="15px", border="1px solid gray", border_radius="50%", background_color=FormState.shapecolor_rgb,margin="auto")),
                                    rx.html("<br>"),
                                    rx.hstack(
                                        rx.text("Extension factor: ",margin="auto"),
                                        rx.input(name="extensionfactor", placeholder="Default: 1.25", value=FormState.extensionfactor, on_change=lambda value: FormState.handle_change("extensionfactor", value)),
                                        rx.dialog.root(
                                            rx.dialog.trigger(rx.link(rx.icon("circle-help"), href="#"),margin="auto"),
                                            rx.dialog.content(
                                                rx.vstack(
                                                    rx.text(rx.text.strong("Extension factor"), " refers to how far the front/back/left/right sides of pieces extend from the top/bottom sides."),
                                                    rx.text(rx.text.strong("Values above 1"), " lead to the sides sticking out of the top/bottom."),
                                                    rx.text(rx.text.strong("Values below 1"), " lead to the sides sticking into the top/bottom."),
                                                    rx.text(rx.text.strong("A value of exactly 1"), " leads to no visible side colors on the top/bottom layers."),
                                                    rx.link(rx.hstack("Need help?", rx.icon("circle-help")), href="https://github.com/Wo0fle/sq1-img-gen/blob/main/README.md", target="_blank",margin="auto"),
                                                ),
                                            ),
                                        ),
                                    ),
                                    rx.html("<br>"),
                                    rx.hstack(
                                        rx.checkbox(
                                            name="sliceindicator",
                                            default_checked=True,
                                            on_change=lambda value: FormState.handle_change("sliceindicator", value),
                                        ),
                                        rx.text("Include slice indcator"),
                                        margin="auto", 
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
                rx.heading("Output",margin="auto",margin_top=0),
                rx.image(src=rx.get_upload_url(FormState.img + ".svg"),margin="auto",),
                rx.text(FormState.whathappen, margin="auto", align="center"),
                rx.button(rx.icon("refresh-ccw"), "Reload Image", on_click=FormState.handle_submit(FormState.form_data), margin="auto",margin_top="20px", size="3"),
                rx.button(rx.icon("image-down"), "Download .png", on_click=rx.download(url=rx.get_upload_url(FormState.png)), margin="auto",margin_top="20px", size="3"),
                rx.button(rx.icon("image-down"), "Download .svg", on_click=rx.download(url=rx.get_upload_url(FormState.svg)), margin="auto",margin_top="20px", size="3"),

                margin="auto",
                margin_top=0,
                width="200px"
            ),
        
        margin_top=0,
        ),

        rx.color_mode.button(position="bottom-left"),

        padding="20px",
    )


app = rx.App()
app.add_page(index)