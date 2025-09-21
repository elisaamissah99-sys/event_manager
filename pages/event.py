from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer
from components.event_card import show_event_card
import requests
from utils.api import base_url
import random
from datetime import datetime

# Some random Unsplash image categories for variety
HERO_IMAGES = [
    "https://cdn.pixabay.com/photo/2020/02/07/09/25/new-zealand-4826675_960_720.jpg",
    "https://cdn.pixabay.com/photo/2017/08/15/21/16/christchurch-2645596_960_720.jpg",
]

MAP_IMAGES = [
    "https://cdn.pixabay.com/photo/2017/08/17/07/47/travel-2650303_960_720.jpg",
    "https://cdn.pixabay.com/photo/2020/10/14/07/15/map-5653495_1280.jpg",
]

@ui.page('/event')
def show_event_page():
    hero_image = random.choice(HERO_IMAGES)
    map_image = random.choice(MAP_IMAGES)

    show_navbar()
    event_id = ui.context.client.request.query_params.get("id")
    
    if not event_id:
        ui.notify("Event ID not provided", type="negative")
        show_footer()
        return
    
    try:
        response = requests.get(f"{base_url}/events/{event_id}")
        if response.status_code == 200:
            json_data = response.json()
            event = json_data["data"]
            
            # Format date and time
            def format_event_datetime(event):
                try:
                    start_date = datetime.fromisoformat(event["start_date"].replace('Z', '+00:00'))
                    end_date = datetime.fromisoformat(event["end_date"].replace('Z', '+00:00'))
                    
                    formatted_date = start_date.strftime("%A, %B %d %Y")
                    formatted_time = f"{start_date.strftime('%I:%M %p')} - {end_date.strftime('%I:%M %p')}"
                    
                    return formatted_date, formatted_time
                except:
                    return "Saturday, March 18 2023", "9:30 PM - 11:30 PM"
            
            event_date, event_time = format_event_datetime(event)
            
        else:
            ui.notify(f"Error loading event: {response.status_code}", type="negative")
            show_footer()
            return
            
    except Exception as e:
        ui.notify(f"Error: {str(e)}", type="negative")
        show_footer()
        return

    # PAGE CONTAINER
    with ui.element('div').classes(
        'w-full max-w-[1320px] mx-auto mt-4 md:mt-[40px] bg-white rounded-[10px] shadow-lg overflow-hidden'
    ):
        # HERO SECTION 
        with ui.element('div').classes(
            f"relative h-[400px] md:h-[600px] bg-cover bg-center rounded-t-[10px] overflow-hidden"
        ).style(f"background-image: url('{event.get('image', hero_image)}')"):
            # Overlay
            ui.element('div').classes('absolute inset-0 bg-black/60')

            # Back Button
            with ui.element('a').props('href=javascript:history.back()').classes(
                'absolute top-4 md:top-[30px] left-4 md:left-[30px] flex items-center gap-2 px-3 md:px-4 py-2 '
                'bg-[#7848F4] text-white rounded shadow-md cursor-pointer hover:bg-[#6937d9] transition-colors z-10'
            ):
                ui.icon('arrow_back').classes('text-white text-sm md:text-base')
                ui.label('Back').classes('text-white text-sm md:text-[16px]')

            # HERO TEXT
            with ui.element('div').classes(
                'absolute top-1/2 transform -translate-y-1/2 left-4 md:left-[60px] right-4 md:right-auto '
                'max-w-[600px] flex flex-col gap-4 md:gap-6 text-center md:text-left'
            ):
                ui.label(event["title"]).classes(
                    'text-3xl md:text-[64px] font-bold text-white leading-tight drop-shadow-lg'
                )
                ui.label(event.get("venue", "IIIT Sonepat")).classes(
                    'text-xl md:text-[36px] font-bold text-white drop-shadow'
                )
                ui.label(event.get("description", "Event description not available")
                ).classes('text-white text-sm md:text-[16px] leading-relaxed max-w-full md:max-w-[550px] line-clamp-3 md:line-clamp-none')
                
                # View Map link
                with ui.element('div').classes(
                    'flex items-center gap-2 text-white mt-2 justify-center md:justify-start'
                ):
                    ui.icon('place')
                    ui.label('View map').classes('text-base md:text-[18px] cursor-pointer')

            # EVENT INFO CARD (Right Side)
            with ui.element('div').classes(
                'absolute bottom-4 md:bottom-auto md:top-[140px] right-4 md:right-[60px] '
                'w-full md:w-[385px] max-w-md bg-white rounded-[10px] shadow-xl p-4 md:p-6 flex flex-col gap-4 md:gap-6'
            ):
                ui.label('Date & Time').classes('text-xl md:text-[24px] font-bold text-black')
                ui.separator().classes('bg-gray-200')
                
                with ui.column().classes('gap-2'):
                    ui.label(event_date).classes('text-[#7E7E7E] text-base md:text-[18px] font-semibold')
                    ui.label(event_time).classes('text-[#7E7E7E] text-base md:text-[18px]')
                
                ui.label('Add to calendar').classes('text-[#7848F4] text-sm md:text-[16px] cursor-pointer hover:underline')
                ui.separator().classes('bg-gray-200')

                # Signup Buttons
                with ui.element('div').classes('flex flex-col gap-3 mt-2'):
                    ui.button('Book Now', color='primary').classes(
                        'w-full text-white rounded-[5px] py-3 bg-[#7848F4] hover:bg-[#6937d9] transition-colors'
                    )
                    ui.button('Program Promoter', color='secondary').classes(
                        'w-full text-gray-700 bg-gray-200 rounded-[5px] py-3 hover:bg-gray-300 transition-colors'
                    )

                ui.label('No Refunds').classes('text-center text-[#7E7E7E] text-sm md:text-[16px] mt-2')

        # MAIN CONTENT BELOW HERO 
        with ui.element('section').classes(
            'p-4 md:p-10 bg-[#FAFAFA] grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-[40px]'
        ):
            # LEFT COLUMN
            with ui.element('div').classes('md:col-span-2 flex flex-col gap-6 md:gap-[40px]'):
                # Description
                with ui.element('div').classes('flex flex-col gap-4'):
                    ui.label('Description').classes('text-2xl md:text-[28px] font-bold text-black')
                    ui.label(
                        event.get("description", 
                        'This workshop introduced participants to the world of 3D modeling. '
                        'It was designed for both beginners and advanced learners, covering everything '
                        'from the basics of Blender to rendering competitions.')
                    ).classes('text-[#7E7E7E] text-base md:text-[18px] leading-relaxed')

                # Hours
                with ui.element('div').classes('flex flex-col gap-4'):
                    ui.label('Hours').classes('text-2xl md:text-[28px] font-bold text-black')

                    with ui.element('div').classes('flex items-center gap-2 text-base md:text-[18px]'):
                        ui.label('Weekdays hour:').classes('text-[#7E7E7E]')
                        ui.label('7PM - 10PM').classes('text-[#7848F4] font-semibold')

                    with ui.element('div').classes('flex items-center gap-2 text-base md:text-[18px]'):
                        ui.label('Sunday hour:').classes('text-[#7E7E7E]')
                        ui.label('7PM - 10PM').classes('text-[#7848F4] font-semibold')

                # Organizer Contact
                with ui.element('div').classes('flex flex-col gap-4'):
                    ui.label('Organizer Contact').classes('text-2xl md:text-[28px] font-bold text-black')
                    ui.label(
                        'Please go to www.sneakypeeks.com and refer the FAQ section for more detail.'
                    ).classes('text-[#7E7E7E] text-base md:text-[18px] leading-relaxed')

            # RIGHT SIDEBAR
            with ui.element('div').classes('flex flex-col gap-6 md:gap-[40px]'):
                # Location
                with ui.element('div').classes(
                    'flex flex-col gap-4 bg-white p-4 rounded-[10px] shadow'
                ):
                    ui.label('Event Location').classes('text-xl md:text-[24px] font-bold text-black')
                    ui.element('div').classes(
                        f"w-full h-[200px] md:h-[220px] rounded-[10px] bg-cover bg-center"
                    ).style(f"background-image: url('{map_image}')")
                    ui.label(event.get("venue", "Dream world wide in Jakarta")).classes(
                        'text-lg md:text-[20px] font-semibold text-black'
                    )
                    ui.label(
                        'Dummy location model by RSU... generates more realistic dummy locations.'
                    ).classes('text-[#7E7E7E] text-sm md:text-[16px] leading-relaxed')

                # Tags
                with ui.element('div').classes(
                    'flex flex-col gap-3 bg-white p-4 rounded-[10px] shadow'
                ):
                    ui.label('Tags').classes('text-xl md:text-[24px] font-bold text-black')
                    with ui.element('div').classes('flex flex-wrap gap-2'):
                        tags = event.get("tags", ["Design", "3D", "Workshop", "Blender"])
                        for tag in tags:
                            ui.label(tag).classes(
                                'px-3 md:px-4 py-1 bg-[#F8F8FA] rounded text-sm md:text-[14px]'
                            )

                # Share
                with ui.element('div').classes(
                    'flex flex-col gap-3 bg-white p-4 rounded-[10px] shadow'
                ):
                    ui.label('Share with friends').classes('text-xl md:text-[24px] font-bold text-black')

                    with ui.element('div').classes('flex gap-3 md:gap-4 justify-center md:justify-start'):
                        social_links = [
                            ('facebook', 'https://facebook.com', '#1877F2'),
                            ('linkedin', 'https://linkedin.com', '#0A66C2'),
                            ('twitter', 'https://twitter.com', '#1DA1F2'),
                            ('whatsapp', 'https://wa.me/123456789', '#25D366')
                        ]
                        
                        for platform, url, color in social_links:
                            with ui.element('a').props(f'href={url} target=_blank').classes(
                                f'p-2 rounded-full bg-{color} text-white hover:scale-110 transition-transform'
                            ):
                                ui.icon(f'fa-brands fa-{platform}').classes('text-lg')

    show_footer()

# Add custom CSS for better mobile experience
ui.add_head_html('''
<style>
    @media (max-width: 768px) {
        .event-hero-content {
            padding: 0 1rem;
        }
        .event-info-card {
            position: relative !important;
            margin: 1rem;
            width: auto !important;
        }
    }
    
    .line-clamp-3 {
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    
    .transition-colors {
        transition: background-color 0.2s ease;
    }
    
    .transition-transform {
        transition: transform 0.2s ease;
    }
</style>
''')