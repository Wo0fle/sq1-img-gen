import reflex as rx

config = rx.Config(
    app_name="sq1_img_gen",
    plugins=[
        rx.plugins.RadixThemesPlugin(theme=rx.theme(accent_color='blue'))
    ]
)