from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer
from components.event_card import show_event_card
import requests
from utils.api import base_url

@ui.page("/")
def show_home_page():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    show_navbar()
    
    # Main container
    with ui.element("main").classes("relative w-full max-w-[1440px] mx-auto min-h-screen bg-[#F8F8FA] rounded-[20px] overflow-hidden"):
        # Hero Section
        with ui.element("section").classes("relative h-[400px] md:h-[596px] mx-4 md:mx-[60px] mt-8 md:mt-[129px] rounded-[10px] overflow-hidden"):
            # Background image container
            with ui.element("div").classes("absolute inset-0 bg-cover bg-center"):
                ui.image("assets/hero-image.jpg").classes("w-full h-full object-cover inset-0")
            
            # Hero content
            ui.label("Made for those who do").classes(
                "absolute left-1/2 transform -translate-x-1/2 top-1/2 -translate-y-1/2 "
                "font-roboto font-bold text-3xl md:text-[64px] leading-tight md:leading-[75px] "
                "text-center uppercase text-white w-full max-w-[90%] md:max-w-[550px] px-4"
            )
            
            # Navigation arrows
            with ui.element("div").classes("absolute inset-x-0 top-1/2 -translate-y-1/2 flex justify-between px-4 md:px-[95px]"):
                ui.button(icon="chevron_left").classes(
                    "w-10 h-10 md:w-[50px] md:h-[50px] flex items-center justify-center "
                    "bg-white/20 rounded-full text-white hover:bg-white/30 transition-colors"
                )
                ui.button(icon="chevron_right").classes(
                    "w-10 h-10 md:w-[50px] md:h-[50px] flex items-center justify-center "
                    "bg-white/20 rounded-full text-white hover:bg-white/30 transition-colors"
                )
        
        # Search Section
        with ui.element("section").classes(
            "relative mx-4 md:mx-[120px] h-auto md:h-[144px] mt-4 md:mt-[-40px] bg-[#10107B] rounded-[20px] p-4 md:p-0"
        ):
            with ui.column().classes("w-full md:flex md:flex-row md:h-[70px] gap-4 md:gap-[40px] md:px-[70px] md:py-[37px]"):
                # Looking For dropdown
                with ui.element("div").classes("flex-1 min-w-[150px]"):
                    ui.label("Looking for").classes("text-white mb-2 text-sm md:text-base")
                    with ui.row().classes("bg-[#ECECEC] rounded-md p-2 justify-between items-center min-h-[44px]"):
                        ui.label("Select Category").classes("text-[#10107B] text-sm")
                        ui.icon("expand_more").classes("text-[#10107B]")
                
                # Location dropdown
                with ui.element("div").classes("flex-1 min-w-[150px]"):
                    ui.label("Location").classes("text-white mb-2 text-sm md:text-base")
                    with ui.row().classes("bg-[#ECECEC] rounded-md p-2 justify-between items-center min-h-[44px]"):
                        ui.label("Select Location").classes("text-[#10107B] text-sm")
                        ui.icon("expand_more").classes("text-[#10107B]")
                
                # When dropdown
                with ui.element("div").classes("flex-1 min-w-[150px]"):
                    ui.label("When").classes("text-white mb-2 text-sm md:text-base")
                    with ui.row().classes("bg-[#ECECEC] rounded-md p-2 justify-between items-center min-h-[44px]"):
                        ui.label("Select Date").classes("text-[#10107B] text-sm")
                        ui.icon("expand_more").classes("text-[#10107B]")
                
                # Search button
                ui.button(icon="search").classes(
                    "w-full md:w-[70px] h-[44px] md:h-[70px] bg-[#7848F4] text-white rounded-md mt-4 md:mt-0"
                )
        
        # Upcoming Events Section header
        with ui.column().classes("mx-4 md:mx-[120px] mt-8 md:mt-[40px] gap-4"):
            ui.label("Upcoming Events").classes("text-2xl md:text-4xl font-bold")
            with ui.row().classes("gap-2 md:gap-5 flex-wrap"):
                for filter_text in ["Popular", "Newest", "Following"]:
                    with ui.element("div").classes(
                        "px-3 py-2 bg-[rgba(104,124,148,0.05)] rounded-md "
                        "flex items-center justify-between gap-2 cursor-pointer"
                    ):
                        ui.label(filter_text).classes("text-xs md:text-sm text-[#131315]")
                        ui.icon("expand_more").classes("text-[#131315] text-sm")

        # Events Cards Section
        with ui.element("div").classes("mx-4 md:mx-[120px] mt-8 flex justify-center"):
            with ui.column().classes("w-full md:flex md:flex-row md:gap-6 md:justify-between max-w-[1000px]"):
                response = requests.get(f"{base_url}/events?limit=3")
                json_data = response.json()
                for event in json_data['data']:
                    show_event_card(event)
        
        # More events section
        with ui.row().classes("mx-4 md:mx-[120px] mt-8 gap-4 md:gap-6 flex-wrap justify-center"):
            for i in range(3):
                with ui.card().classes(
                    "w-full md:w-[300px] h-auto md:h-[340px] bg-white rounded-[10px] overflow-hidden flex-shrink-0 "
                    "shadow-[0px_-8px_80px_rgba(0,0,0,0.07),0px_-2.92013px_29.2013px_rgba(0,0,0,0.0482987)] mb-4 md:mb-0"
                ):
                    # Event Image Section
                    with ui.element("div").classes("relative w-full h-[180px] md:h-[200px] rounded-md overflow-hidden"):
                        ui.image("assets/party2.jpg").classes("w-full h-full object-cover rounded-md")
                        # FREE Tag
                        with ui.element("div").classes(
                            "absolute top-[10px] left-[10px] bg-white rounded-md "
                            "px-[10px] py-[5px] flex items-center justify-center"
                        ):
                            ui.label("FREE").classes("text-[10px] text-[#7848F4]")
                    # Event Content
                    with ui.column().classes("p-4"):
                        # Event Title
                        ui.label(
                            [
                                "Music Night - Harvard",
                                "Startup Pitch - Stanford",
                                "Design Fair - Nanyang"
                            ][i]
                        ).classes("text-base leading-[20px] text-black font-bold mb-2")
                        # Event Time
                        ui.label([
                            "Sat, Jun 10, 7:00PM",
                            "Thu, Jul 13, 3:00PM",
                            "Mon, Aug 21, 11:00AM"
                        ][i]).classes("text-sm leading-[16px] text-[#7848F4] mb-2")
                        # Event Location
                        ui.label([
                            "Harvard Hall",
                            "Stanford Auditorium",
                            "Nanyang Center"
                        ][i]).classes("text-sm leading-[16px] text-[#7E7E7E]")
        
        # View More Button
        with ui.element("div").classes("flex justify-center mt-8 md:mt-10 px-4"):
            ui.button("View More").classes(
                "w-full md:w-auto px-6 py-3 md:px-10 md:py-4 bg-[#7848F4] text-white rounded-md "
                "hover:bg-[#6537E0] transition-colors text-sm md:text-base"
            )

        # Create Events Section
        with ui.element("section").classes("relative w-full h-auto md:h-[303px] mt-16 md:mt-[100px] px-4 md:px-0"):
            # Navy blue background
            with ui.element("div").classes("absolute w-full h-[200px] md:h-[252px] left-0 top-[30px] md:top-[51px] bg-[#10107B] rounded-[20px]"):
                pass
            # Content container
            with ui.row().classes("relative z-10 flex flex-col md:flex-row items-center justify-between h-full pt-8 md:pt-0 px-4 md:px-[100px]"):
                # Left image
                with ui.element("div").classes("w-full md:w-[40%] h-[200px] md:h-[303px] order-2 md:order-1 mt-4 md:mt-0"):
                    ui.image("assets/cartoon.png").classes("w-full h-full object-cover rounded-[10px]")
                # Right content
                with ui.column().classes("w-full md:w-[50%] order-1 md:order-2 text-center md:text-left"):
                    ui.label("Make your own Event").classes("text-2xl md:text-[36px] font-bold leading-tight md:leading-[42px] text-[#F8F8FA]")
                    ui.label("Lorem ipsum dolor sit amet, consectetur adipiscing elit.").classes("mt-2 md:mt-4 text-base md:text-[18px] leading-normal md:leading-[21px] text-[#F8F8FA] mt-4")
                    # CTA Button
                    ui.button("Create Events").classes(
                        "w-full md:w-[302px] h-[50px] md:h-[60px] bg-[#7848F4] text-white text-base md:text-[18px] font-bold rounded-[5px] shadow-[0px_10px_50px_rgba(61,55,241,0.25)] mt-4"
                    )

        # Brands Section
        with ui.element("section").classes("relative w-full max-w-[1200px] mx-auto py-8 md:py-[60px] mt-16 md:mt-[120px] bg-transparent px-4"):
            ui.label("Join these brands").classes("block text-2xl md:text-[36px] font-bold leading-tight md:leading-[42px] text-center text-[#131315] mb-2")
            ui.label("We've had the pleasure of working with industry-defining brands. These are just some of them.").classes("block text-base md:text-[18px] leading-normal md:leading-[21px] text-center text-[#131315] mb-8 max-w-3xl mx-auto")
            # Logo grid
            brand_logos = [
                ("assets/spotify.png", "w-[120px] md:w-[179px] h-[30px] md:h-[50px]"),
                ("assets/google.png", "w-[110px] md:w-[162px] h-[30px] md:h-[49px]"),
                ("assets/stripe.png", "w-[100px] md:w-[141px] h-[40px] md:h-[63px]"),
                ("assets/youtube.png", "w-[150px] md:w-[226px] h-[80px] md:h-[131px]"),
                ("assets/microsoft.png", "w-[130px] md:w-[182px] h-[25px] md:h-[39px]"),
                ("assets/medium.png", "w-[200px] md:w-[297px] h-[80px] md:h-[124px]"),
                ("assets/zoom.png", "w-[200px] md:w-[295px] h-[50px] md:h-[83px]"),
                ("assets/uber.png", "w-[100px] md:w-[134px] h-[30px] md:h-[44px]"),
                ("assets/grab.png", "w-[110px] md:w-[145px] h-[35px] md:h-[52px]")
            ]
            with ui.grid().classes("grid grid-cols-2 md:grid-cols-3 gap-6 md:gap-8 justify-items-center items-center mb-8"):
                for logo, size in brand_logos:
                    ui.image(logo).classes(f"object-contain bg-transparent rounded-md {size} max-w-full")

        # Trending Colleges Section
        with ui.element("section").classes("relative w-full max-w-[1200px] mx-auto py-8 md:py-[60px] mt-8 md:mt-[40px] bg-transparent px-4"):
            ui.label("Trending colleges").classes("block text-2xl md:text-[36px] font-bold leading-tight md:leading-[42px] text-left text-[#000] mb-6 md:mb-8")
            college_data = [
                {
                    "img": "assets/havard.png",
                    "name": "Harvard University",
                    "location": "Cambridge, Massachusetts, UK",
                    "rating": "4.8",
                    "tag": "EXCLUSIVE"
                },
                {
                    "img": "assets/standford.png",
                    "name": "Stanford University",
                    "location": "Stanford, California",
                    "rating": "4.8",
                    "tag": "EXCLUSIVE"
                },
                {
                    "img": "assets/nayang.png",
                    "name": "Nanyang University",
                    "location": "Nanyang Ave, Singapura",
                    "rating": "4.8",
                    "tag": "EXCLUSIVE"
                },
            ]
            with ui.column().classes("w-full md:flex md:flex-row md:gap-8 justify-between items-start"):
                for college in college_data:
                    with ui.card().classes("w-full md:w-[330px] h-auto md:h-[340px] bg-white rounded-[10px] flex flex-col justify-between shadow-[0px_-8px_80px_rgba(0,0,0,0.07),0px_-2.92013px_29.2013px_rgba(0,0,0,0.0482987)] mb-6 md:mb-0"):
                        # Card image
                        with ui.element("div").classes("w-full h-[150px] md:h-[180px] rounded-t-[10px] overflow-hidden"):
                            ui.image(college["img"]).classes("w-full h-full object-cover rounded-t-[10px]")
                        # Card body
                        with ui.element("div").classes("flex flex-col items-start p-4 md:px-6 md:pt-4"):
                            ui.label(college["name"]).classes("text-lg md:text-[24px] font-bold text-[#131315] mb-2 line-clamp-2")
                            ui.label(college["location"]).classes("text-sm md:text-[14px] font-medium text-black mb-2 line-clamp-2")
                        # Card footer
                        with ui.element("div").classes("flex flex-row justify-between items-center p-4 md:px-6 md:pb-6 w-full mt-auto"):
                            with ui.element("div").classes("flex items-center bg-white rounded-full px-3 md:px-4 py-1 shadow"):
                                ui.icon("star").classes("text-[#EBD402] text-[16px] md:text-[20px] mr-1")
                                ui.label(college["rating"]).classes("text-sm md:text-[16px] font-medium text-black")
                            with ui.element("div").classes("flex items-center bg-black rounded-[20px] px-3 md:px-4 py-1 ml-2"):
                                ui.label(college["tag"]).classes("text-white text-xs md:text-[14px] font-medium tracking-wider")
                            ui.button(icon="more_horiz").classes("w-8 h-8 md:w-[40px] md:h-[40px] bg-[#F2F2F2] rounded-full flex items-center justify-center ml-2")

        # Our Blogs Section
        with ui.element("section").classes("relative w-full max-w-[1200px] mx-auto py-8 md:py-[60px] mt-8 md:mt-[40px] bg-transparent px-4"):
            ui.label("Our Blogs").classes("block text-2xl md:text-[36px] font-bold leading-tight md:leading-[42px] text-left text-[#000] mb-6 md:mb-8")
            blog_data = [
                {
                    "img": "assets/party3.jpg",
                    "title": "How to Host a Successful Event",
                    "date": "Sep 10, 2025",
                    "author": "Jane Doe"
                },
                {
                    "img": "assets/party3.jpg",
                    "title": "Top 10 College Festivals in 2025",
                    "date": "Aug 22, 2025",
                    "author": "John Smith"
                },
                {
                    "img": "assets/party3.jpg",
                    "title": "Brand Partnerships: What Works?",
                    "date": "Jul 15, 2025",
                    "author": "Emily Lee"
                },
            ]
            with ui.column().classes("w-full md:flex md:flex-row md:gap-8 justify-center items-start"):
                for blog in blog_data:
                    with ui.card().classes("w-full md:w-[350px] h-auto md:h-[380px] bg-white rounded-[10px] flex flex-col justify-between shadow-[0px_-8px_80px_rgba(0,0,0,0.07),0px_-2.92013px_29.2013px_rgba(0,0,0,0.0482987)] mb-6 md:mb-0"):
                        # Blog image
                        with ui.element("div").classes("w-full h-[150px] md:h-[200px] rounded-[10px] overflow-hidden"):
                            ui.image(blog["img"]).classes("w-full h-full object-cover rounded-[10px]")
                        # Blog content
                        with ui.element("div").classes("flex flex-col p-4 md:p-6"):
                            ui.label(blog["title"]).classes("text-base md:text-[16px] font-bold text-black mb-2 line-clamp-2")
                            ui.label(f"{blog['date']} • {blog['author']}").classes("text-xs md:text-[12px] text-[#7848F4] mt-1")
   
    show_footer()