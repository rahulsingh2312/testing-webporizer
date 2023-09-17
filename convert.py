from PIL import Image
import os
import re


# Function to convert a JPG image to WebP and save it in the same location
def convert_jpg_to_webp(input_file):
    try:
        # Open the JPG image using Pillow
        with Image.open(input_file) as img:
            # Create a WebP version of the image
            # hi test
            output_file = os.path.splitext(input_file)[0] + ".webp"
            img.save(output_file, "webp" , optimize = True ,quality = 10)
            print(f"Converted {input_file} to {output_file}")

            os.remove(input_file)
            print(f"Deleted {input_file}")
    except Exception as e:
        print(f"Error converting {input_file}: {e}")



# Function to update image references in a file
def update_image_references(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Define a regular expression to match <img src="xyz.jpg">
            jpg_pattern = r'<img\s+src="([^"]+\.jpg)"\s*>'

            # Find all JPG image references in the file
            jpg_matches = re.findall(jpg_pattern, content)

            if jpg_matches:
                for jpg_file in jpg_matches:
                    # Replace .jpg with .webp in the image reference
                    webp_file = jpg_file.replace('.jpg', '.webp')
                    content = content.replace(jpg_file, webp_file)

                # Write the modified content back to the file
                with open(file_path, 'w', encoding='utf-8') as updated_file:
                    updated_file.write(content)

                print(f"Updated image references in {file_path}")
    except Exception as e:
        print(f"Error updating image references in {file_path}: {e}")




# Specify the directory containing JPG images
# Specify the directory containing JPG images using a raw string (r)
imagendcode_directory = r"C:\Users\Rahul\Documents\rahulvsc\tcet-opensource\webporizer"

# Loop through files in the directory
for root, dirs, files in os.walk(imagendcode_directory):
    
       
    for file in files:
        if file.lower().endswith(".jpg"):
            jpg_path = os.path.join(root, file)
            convert_jpg_to_webp(jpg_path)
        if file.lower().endswith((".html", ".jsx")):
            file_path = os.path.join(root, file)
            update_image_references(file_path)



