import os

def write_html_with_app_name(app_name, subdir):
    with open('template.html', 'r') as file:
        template = file.read()

    output_html = template.replace('{{APP_NAME}}', app_name)
    output_filename = f"{app_name.replace(' ', '_').lower()}_landing_page.html"
    output_path = os.path.join(subdir, output_filename)

    with open(output_path, 'w') as file:
        file.write(output_html)

# Define the subdirectory name
subdirectory = "generated_htmls"

# Check if the subdirectory exists, and if not, create it
if not os.path.exists(subdirectory):
    os.makedirs(subdirectory)

app_names = [
    "Realty Beats", 
    "PlotPoint Trends", 
    "Terralytics Hub", 
    "PlotPoint Analytics", 
    "PlotPoint Nexus"         
]

for name in app_names:
    write_html_with_app_name(name, subdirectory)

