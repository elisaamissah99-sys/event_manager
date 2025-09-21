from nicegui import ui
import datetime

def show_event_card(event):
    # Calculate days until event for the "trending" badge logic
    event_date = datetime.datetime.strptime(event['start_time'], '%Y-%m-%d %H:%M')
    days_until = (event_date - datetime.datetime.now()).days
    
    with ui.card().on(type="click",
                      handler=lambda: ui.navigate.to(f"/event?id={event['id']}")).classes("""
        cursor-pointer w-[350px] h-[380px] bg-white rounded-xl flex flex-col justify-between 
        shadow-lg hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1
        overflow-hidden border border-gray-100
    """):
        # Event Image with overlay
        with ui.element("div").classes("relative w-full h-[180px] overflow-hidden"):
            ui.image(source=event['image']).classes("w-full h-full object-cover")
            
            # Image overlay gradient
            ui.element("div").classes("absolute inset-0 bg-gradient-to-t from-black/30 to-transparent opacity-70")
            
            # FREE Tag
            if event.get('is_free', True):
                with ui.element("div").classes("absolute top-3 left-3 bg-white rounded-md px-3 py-1 flex items-center justify-center shadow-md"):
                    ui.label("FREE").classes("text-xs font-bold text-[#7848F4]")
            
            # Trending badge (if event is within 7 days)
            if days_until <= 7 and days_until >= 0:
                with ui.element("div").classes("absolute top-3 right-3 bg-red-500 rounded-md px-2 py-1 flex items-center justify-center shadow-md"):
                    ui.label("TRENDING").classes("text-xs font-bold text-white")
            
            # Date badge
            with ui.element("div").classes("absolute bottom-3 left-3 bg-white/90 rounded-lg px-3 py-2 flex flex-col items-center justify-center"):
                ui.label(event_date.strftime('%d')).classes("text-lg font-bold text-[#7848F4] leading-none")
                ui.label(event_date.strftime('%b')).classes("text-xs font-medium text-gray-700 uppercase")
        
        # Event content
        with ui.column().classes("p-4 flex-1 flex flex-col justify-between"):
            # Event Title
            ui.label(text=event['title']).classes("text-lg font-bold text-gray-900 line-clamp-2 leading-tight mb-2")
            
            # Event details
            with ui.column().classes("space-y-2"):
                # Time
                with ui.row().classes("items-center gap-2"):
                    ui.icon("schedule", size="sm", color="#7848F4").classes("flex-shrink-0")
                    ui.label(text=event_date.strftime('%a, %b %d · %I:%M %p')).classes("text-sm text-gray-600")
                
                # Location
                with ui.row().classes("items-center gap-2"):
                    ui.icon("location_on", size="sm", color="#7848F4").classes("flex-shrink-0")
                    ui.label(text=event['venue']).classes("text-sm text-gray-600 line-clamp-1")
            
            # Interested count
            with ui.row().classes("items-center justify-between pt-3 mt-3 border-t border-gray-100"):
                with ui.row().classes("items-center gap-1"):
                    ui.icon("people", size="sm", color="#7848F4")
                    ui.label(f"{event.get('interested', 0)} interested").classes("text-xs text-gray-500")
                
                # Category tag
                if event.get('category'):
                    ui.element("div").classes(f"px-2 py-1 rounded-full text-xs font-medium {get_category_color(event['category'])}") \
                        .style(f"background-color: {get_category_bg_color(event['category'])}") \
                        .text(event['category'])

# Helper function for category colors
def get_category_color(category):
    color_map = {
        "Music": "#D53F8C",      # Pink
        "Art": "#38A169",        # Green
        "Food": "#DD6B20",       # Orange
        "Tech": "#3182CE",       # Blue
        "Sports": "#E53E3E",     # Red
        "Business": "#805AD5",   # Purple
    }
    return color_map.get(category, "#7848F4")  # Default purple

# Helper function for category background colors
def get_category_bg_color(category):
    bg_color_map = {
        "Music": "rgba(213, 63, 140, 0.1)",
        "Art": "rgba(56, 161, 105, 0.1)",
        "Food": "rgba(221, 107, 32, 0.1)",
        "Tech": "rgba(49, 130, 206, 0.1)",
        "Sports": "rgba(229, 62, 62, 0.1)",
        "Business": "rgba(128, 90, 213, 0.1)",
    }
    return bg_color_map.get(category, "rgba(120, 72, 244, 0.1)")  # Default purple with opacity

# Example usage
if __name__ in {"__main__", "__mp_main__"}:
    # Sample event data
    sample_event = {
        'id': 1,
        'title': 'Summer Music Festival with International Artists',
        'start_time': '2023-08-15 19:00',
        'venue': 'Central Park, New York City',
        'image': 'https://images.unsplash.com/photo-1540039155733-5bb30b53aa14?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1074&q=80',
        'is_free': True,
        'interested': 245,
        'category': 'Music'
    }
    
    # Add custom CSS for line clamping
    ui.add_head_html("""
    <style>
        .line-clamp-1 {
            overflow: hidden;
            display: -webkit-box;
            -webkit-box-orient: vertical;
            -webkit-line-clamp: 1;
        }
        .line-clamp-2 {
            overflow: hidden;
            display: -webkit-box;
            -webkit-box-orient: vertical;
            -webkit-line-clamp: 2;
        }
    </style>
    """)
    
    # Show the card
    show_event_card(sample_event)
    ui.run()