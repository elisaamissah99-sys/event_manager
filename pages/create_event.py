from nicegui import ui
import requests
from components.navbar import show_navbar
from components.footer import show_footer
from utils.api import base_url

_event_image = None

def _handle_image_upload(event):
    global _event_image
    _event_image = event.content
    ui.notify("Image uploaded successfully!", type="positive")

def _post_event(data, files):
    # Validate required fields
    required_fields = ["title", "venue", "start_time", "end_time", "start_date", "end_date", "description"]
    missing_fields = [field for field in required_fields if not data.get(field)]
    
    if missing_fields:
        return ui.notify(
            message=f"Please fill in all required fields: {', '.join(missing_fields)}",
            type="warning"
        )
    
    if not _event_image:
        return ui.notify(
            message="Please upload an event image",
            type="warning"
        )
    
    try:
        response = requests.post(f"{base_url}/events", data=data, files=files)
        print(response.status_code, response.content)
        
        if response.status_code == 200:
            ui.notify(
                message="Event created successfully!",
                type="positive"
            )
            return ui.navigate.to("/")
        elif response.status_code == 422:
            return ui.notify(
                message="Please ensure all inputs are filled correctly",
                type="warning"
            )
        else:
            return ui.notify(
                message=f"Error creating event: {response.status_code}",
                type="negative"
            )
    except Exception as e:
        ui.notify(
            message=f"Network error: {str(e)}",
            type="negative"
        )

@ui.page('/create_event')
def show_create_event_page():
    ui.query(".nicegui-content").classes('m-0 p-0 gap-0')
    show_navbar()
    
    # Main container
    with ui.element("div").classes("w-full min-h-screen bg-blue-50 py-8 px-4 md:px-8"):
        # Page title
        ui.label("Create New Event").classes("font-bold text-2xl md:text-3xl text-center mb-8 text-gray-800")
        
        # Form container
        with ui.card().classes("w-full max-w-4xl mx-auto p-6 md:p-8 shadow-lg rounded-xl"):
            # Event Details Section
            with ui.column().classes("w-full gap-6"):
                # Event Title
                with ui.column().classes("w-full gap-2"):
                    ui.label("Event Title *").classes("font-semibold text-gray-700")
                    event_title = ui.input(placeholder="Enter event title").props("outlined dense").classes("w-full")
                
                # Event Venue
                with ui.column().classes("w-full gap-2"):
                    ui.label("Event Venue *").classes("font-semibold text-gray-700")
                    event_venue = ui.input(placeholder="Enter the venue").props("outlined dense").classes("w-full")
                
                # Date and Time Section
                with ui.column().classes("w-full gap-4"):
                    ui.label("Event Date & Time *").classes("font-semibold text-gray-700")
                    
                    # Date row
                    with ui.row().classes("w-full gap-4 flex-wrap"):
                        with ui.column().classes("flex-1 min-w-[200px] gap-2"):
                            ui.label("Start Date").classes("text-sm text-gray-600")
                            event_start_date = ui.input().props('type=date outlined dense').classes('w-full')
                        
                        with ui.column().classes("flex-1 min-w-[200px] gap-2"):
                            ui.label("End Date").classes("text-sm text-gray-600")
                            event_end_date = ui.input().props('type=date outlined dense').classes('w-full')
                    
                    # Time row
                    with ui.row().classes("w-full gap-4 flex-wrap"):
                        with ui.column().classes("flex-1 min-w-[150px] gap-2"):
                            ui.label("Start Time").classes("text-sm text-gray-600")
                            event_start_time = ui.input().props('type=time outlined dense').classes('w-full')
                        
                        with ui.column().classes("flex-1 min-w-[150px] gap-2"):
                            ui.label("End Time").classes("text-sm text-gray-600")
                            event_end_time = ui.input().props('type=time outlined dense').classes('w-full')
                
                # Event Description
                with ui.column().classes("w-full gap-2"):
                    ui.label("Event Description *").classes("font-semibold text-gray-700")
                    event_description = ui.textarea(placeholder="Describe your event...").props("outlined dense").classes("w-full min-h-[100px]")
                
                # Event Image Upload
                with ui.column().classes("w-full gap-2"):
                    ui.label("Event Image *").classes("font-semibold text-gray-700")
                    with ui.card().classes("w-full p-4 border-2 border-dashed border-gray-300 rounded-lg"):
                        ui.upload(
                            auto_upload=True, 
                            on_upload=_handle_image_upload,
                            label="Click or drop image here"
                        ).props('accept=image/*').classes('w-full')
                        ui.label("Supported formats: JPG, PNG, GIF").classes("text-xs text-gray-500 mt-2")
                
                # Submit Button
                with ui.column().classes("w-full gap-2 mt-4"):
                    ui.button(
                        "Create Event", 
                        on_click=lambda: _post_event(
                            data={
                                "title": event_title.value,
                                "venue": event_venue.value,
                                "start_time": event_start_time.value,
                                "end_time": event_end_time.value,
                                "start_date": event_start_date.value,
                                "end_date": event_end_date.value,
                                "description": event_description.value,
                            },
                            files={"image": _event_image}
                        )
                    ).props("unelevated").classes("w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-lg")
                    
                    ui.label("* Required fields").classes("text-xs text-gray-500 text-center mt-2")
    
    show_footer()

# Add some custom CSS for better styling
ui.add_head_html('''
<style>
    .nicegui-content {
        font-family: 'Inter', sans-serif;
    }
    .q-field__outline {
        border-radius: 8px;
    }
    .q-uploader__header {
        background-color: #f8fafc !important;
    }
    .q-btn {
        text-transform: none;
        font-weight: 500;
    }
</style>
''')