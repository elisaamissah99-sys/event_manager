from nicegui import ui

def show_navbar():
    # Adjust the padding/margin to match your Figma spacing
    with ui.element("nav").classes("fixed w-full top-0 left-0 right-0 z-50 bg-white shadow"):
        with ui.row().classes("px-[120px] h-[64px] justify-between items-center"):
            # Logo/Brand name
            ui.label("Event Hive").classes("font-roboto font-bold text-3xl leading-[47px] text-black")

            # Navigation links container
            with ui.row().classes("gap-[30px] items-center"):
                # Login link
                ui.link("Login", "/login").classes(
                    "font-roboto text-base text-[#131315] hover:text-[#7848F4] "
                    "transition-colors duration-200"
                )
                
                # Signup button
                ui.button("Signup", on_click=lambda: ui.navigate("/signup")).classes(
                    "bg-white text-[#7848F4] border border-[#7848F4] px-6 py-2 rounded-md "
                    "font-roboto text-base hover:bg-[#f5f2ff] transition-colors duration-200"
                )
                
                # Create Event button (primary action)
                ui.button("Create Event", on_click=lambda: ui.navigate("/create-event")).classes(
                    "bg-[#7848F4] text-white px-6 py-3 rounded-md "
                    "font-roboto text-base font-medium hover:bg-[#6537E0] "
                    "transition-colors duration-200 shadow-md hover:shadow-lg"
                )