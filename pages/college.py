from nicegui import ui 
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page("/college")
def show_college_page():
    show_navbar()
    with ui.element("main").classes("relative w-full max-w-[1440px] mx-auto min-h-[2428px] bg-[#F8F8FA] rounded-[20px] pb-12"):
        pass
        
        # Hero Image with navigation arrows
        with ui.element("section").classes("relative mx-[60px] mt-[129px] h-[570px] rounded-[10px] overflow-hidden"):
            ui.image("assets/audi.jpg").classes("w-full h-full object-cover rounded-[10px]")
      
            # Left arrow
            ui.button(icon="chevron_left").classes(
                "absolute left-[35px] top-1/2 -translate-y-1/2 w-[50px] h-[50px] flex items-center justify-center bg-[rgba(242,242,242,0.2)] rounded-full text-white hover:bg-white/30 transition-colors"
            )
            # Right arrow
            ui.button(icon="chevron_right").classes(
                "absolute right-[35px] top-1/2 -translate-y-1/2 w-[50px] h-[50px] flex items-center justify-center bg-[rgba(242,242,242,0.2)] rounded-full text-white hover:bg-white/30 transition-colors"
            )

        # College Title
        ui.label("IIT Roorke").classes("absolute left-[120px] top-[755px] text-[36px] font-bold leading-[42px] text-black")
        # College Description
        ui.label("DesignHub organized a 3D Modeling Workshop using Blender on 16th February at 5 PM. The workshop taught participants the magic of creating stunning 3D models and animations using Blender. It was suitable for both beginners and experienced users. The event was followed by a blender-render competition, which added to the excitement. DesignHub organized a 3D Modeling Workshop using Blender on 16th February at 5 PM. The workshop taught participants the magic of creating stunning 3D models and animations using Blender. It was suitable for both beginners and experienced users. The event was followed by a blender-render competition, which added to the excitement. DesignHub organized a 3D Modeling Workshop using Blender on 16th February at 5 PM. The workshop taught participants the magic of creating stunning 3D models and animations using Blender. It was suitable for both beginners and experienced users. The event was followed by a blender-render competition, which added to the excitement. DesignHub organized a 3D Modeling Workshop using Blender on 16th February at 5 PM. The workshop taught participants the magic of creating stunning 3D models and animations using Blender. It was suitable for both beginners and experienced users. The event was followed by a blender-render competition, which added to the excitement.").classes("absolute left-[120px] right-[120px] top-[790px] h-[285px] text-[16px] leading-[19px] text-[#7E7E7E] font-roboto")

        # College Events Title
        ui.label("College Events").classes("absolute left-[120px] top-[1095px] text-[36px] font-bold leading-[42px] text-black")

        # College Events Cards (3 in a row)
        with ui.row().classes("mx-[120px] mt-8 gap-6 flex-wrap justify-center"):
            event_images = [
                "assets/audi.jpg",
                "assets/audi.jpg",
                "assets/audi.jpg"
            ]
        with ui.row().classes("absolute left-[120px] right-[120px] top-[1178px] gap-[20px] h-[400px]"):
            for i in range(3):
                with ui.card().classes("w-[320.67px] h-[330px] bg-white rounded-[10px] flex flex-col justify-between shadow-[0px_-8px_80px_rgba(0,0,0,0.07),0px_-2.92013px_29.2013px_rgba(0,0,0,0.0482987)]"):
                    # Event Image
                   
                    with ui.element("div").classes("relative  w-full rounded-md overflow-hidden"):
                        ui.image("assets/audi.jpg").classes("w-full h-full object-cover rounded-md")
                        # FREE Tag
                        with ui.element("div").classes("absolute top-[10px] left-[10px] bg-white rounded-md px-[10px] py-[5px] flex items-center justify-center"):
                            ui.label("FREE").classes("text-[10px] text-[#7848F4]")
                    # Event Title
                    ui.label("BestSeller Book Bootcamp - Lucknow").classes("px-4 mt-[6px] text-base leading-[20px] text-black font-bold")
                    # Event Time
                    ui.label("Sat, Mar 18, 9:30PM").classes("px-4 mt-[6px] text-sm leading-[16px] text-[#7848F4]")
                    # Event Location
                    ui.label("ONLINE EVENT - Attend anywhere").classes("px-4 mt-[6px] text-sm leading-[16px] text-[#7E7E7E]")

        # More College Events Cards (3 in a row)
            with ui.row().classes("mx-[120px] mt-8 gap-6 flex-wrap justify-center"):
                more_event_images = [
                "assets/party1.jpg",
                "assets/party1.jpg",
                "assets/party1.jpg"
            ]
        with ui.row().classes("absolute left-[120px] right-[120px] top-[1608px] gap-[20px] h-[400px]"):
            for i in range(3):
                with ui.card().classes("w-[320.67px] h-[330px] bg-white rounded-[10px] flex flex-col justify-between shadow-[0px_-8px_80px_rgba(0,0,0,0.07),0px_-2.92013px_29.2013px_rgba(0,0,0,0.0482987)]"):
                    # Event Image
                    
                    with ui.element("div").classes("relative h-[140px] w-full rounded-md overflow-hidden"):
                        ui.image(more_event_images[i]).classes("w-full h-full object-cover rounded-md")
                        # FREE Tag
                        with ui.element("div").classes("absolute top-[10px] left-[10px] bg-white rounded-md px-[10px] py-[5px] flex items-center justify-center"):
                            ui.label("FREE").classes("text-[10px] text-[#7848F4]")
                    # Event Title
                    ui.label("BestSeller Book Bootcamp - Lucknow").classes("px-4 mt-[6px] text-base leading-[20px] text-black font-bold")
                    # Event Time
                    ui.label("Sat, Mar 18, 9:30PM").classes("px-4 mt-[6px] text-sm leading-[16px] text-[#7848F4]")
                    # Event Location
                    ui.label("ONLINE EVENT - Attend anywhere").classes("px-4 mt-[6px] text-sm leading-[16px] text-[#7E7E7E]")

    show_footer()