from nicegui import ui

@ui.page('/signup')
def show_signup_page():
        ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
        # Adding the fontawesome icons
        ui.add_head_html("<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>")
        
        with ui.element("div").classes("w-full h-screen flex flex-row m-0 p-0 gap-0 overflow-hidden"):
            with ui.element("div").classes("bg-[url('assets/party1.jpg')] bg-cover bg-center flex flex-col w-1/2 h-full justify-center items-center"):
                with ui.column().classes("items-center"):
                    ui.label("Welcome back").classes("text-white text-4xl font-bold mb-4")
                    ui.label("To keep connected with us provide us with your information").classes("text-white mb-4")
                    
                    with ui.link("","/signin").classes("no-underline"):
                        with ui.button(text=None).classes('relative px-4 rounded-lg flex items-center justify-center bg-transparent border-none'):
                            # The blurred overlay
                            ui.element('div').classes('absolute inset-0 backdrop-blur-sm bg-white/30')
                            # The text label (must be a separate element to avoid being blurred)
                            ui.label('Signin').classes('relative z-10 text-white font-semibold text-sm')
                
            with ui.column().classes('w-1/2 h-full bg-white flex flex-col justify-center items-center p-4'):
                with ui.row().classes('items-center'):
                    ui.label('Event').classes('text-2xl font-bold text-gray-800')
                    ui.label('Hive').classes('text-2xl font-bold text-blue-600')

                ui.label('Sign Up to Event Hive').classes('text-3xl font-bold text-gray-800')

                # Input fields
                ui.input('YOUR NAME', placeholder='Enter your name').classes('w-3/4').props("outlined")
                ui.input('YOUR EMAIL', placeholder='Enter your email').classes('w-3/4').props("outlined")
                ui.input('PASSWORD', placeholder='Enter your password', password=True, password_toggle_button=True).classes('w-3/4').props("outlined")
                ui.input('CONFIRM PASSWORD', placeholder='Enter your password', password=True, password_toggle_button=True).classes('w-3/4 mb-2').props("outlined")

                ui.button('Sign Up', icon='fa-solid fa-user-plus').classes("text-white bg-blue-600 w-[50%] p-2").props("flat dense no-caps")
                ui.label('Or').classes('text-gray-500')
                ui.button('Sign up with Google', icon='fa-brands fa-google').classes("text-white bg-blue-600 w-[50%] p-2").props("flat dense no-caps")