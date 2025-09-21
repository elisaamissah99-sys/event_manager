from nicegui import ui
def show_footer():
    """Pixel-perfect, responsive Figma-style footer with balanced layout"""

    # Load FontAwesome for social icons
    ui.add_head_html(
        '<script src="https://kit.fontawesome.com/ccba89e5d4.js" crossorigin="anonymous"></script>'
    )

    with ui.element('footer').classes(
        'bg-[#10107B] text-white w-screen px-6 md:px-10 py-10 flex flex-auto flex-wrap justify-items-stretch flex-col gap-5'
    ):
        #Logo Section 
        with ui.column().classes('items-center gap-2'):
            with ui.row().classes("items-center justify-center text-4xl font-bold"):
                ui.icon("hub").classes("text-[#ffffff] text-3xl")
                ui.label("Event").classes("text-white")
                ui.label("Hive").classes("text-[#7848F4]")

        # Newsletter Section 
        with ui.row().classes('justify-center items-center gap-3'):
            ui.input(placeholder="Enter your mail").classes(
                "w-[250px] h-[40px] px-3 rounded-sm bg-white text-gray-700"
            )
            ui.button(
                "Subscribe",
                on_click=lambda: ui.notify("You have successfully subscribed"),
            ).classes("bg-[#7848F4] text-white px-6 py-2 rounded-sm")

        # Navigation Links
        with ui.row().classes('justify-center gap-8 flex-wrap'):
            for link in ["Home", "About", "Services", "Get in touch", "FAQs"]:
                ui.label(link).classes(
                    "cursor-pointer text-[16px] hover:text-gray-300"
                )

        #Divider 
        ui.separator().classes("opacity-40")

        # Bottom Row
        with ui.row().classes(
            "w-full justify-between items-center flex-wrap gap-6"
        ):
            
            with ui.row().classes('gap-3 items-center'):
                ui.html(
                    '<a href="#" class="px-2 py-1 rounded-sm bg-purple-700 text-white text-[12px]">English</a>'
                )
                ui.html('<a href="#" class="text-white text-[12px] hover:text-gray-300">French</a>')
                ui.html('<a href="#" class="text-white text-[12px] hover:text-gray-300">Twi</a>')

            # Center: Social icons
            with ui.row().classes("gap-4 justify-center text-xl"):
                ui.html('<a href="https://facebook.com" target="_blank"><i class="fa-brands fa-facebook"></i></a>')
                ui.html('<a href="https://instagram.com" target="_blank"><i class="fa-brands fa-instagram"></i></a>')
                ui.html('<a href="https://twitter.com" target="_blank"><i class="fa-brands fa-twitter"></i></a>')
                ui.html('<a href="https://linkedin.com" target="_blank"><i class="fa-brands fa-linkedin"></i></a>')

           
            