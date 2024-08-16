import os
import zipfile

def extract_images(docx_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    images = []
    
    # Open the DOCX file as a ZIP archive
    with zipfile.ZipFile(docx_path, 'r') as docx:
        # Loop through all files in the DOCX
        for file in docx.namelist():
            if file.startswith('word/media/') and (file.endswith('.jpeg') or file.endswith('.png')):
                # Read the image data
                image_data = docx.read(file)
                
                # Get the image extension
                image_ext = file.split('.')[-1]
                
                # Define the output image path
                image_filename = os.path.join(output_folder, f"{os.path.basename(file)}")
                
                # Save the image
                with open(image_filename, 'wb') as img_file:
                    img_file.write(image_data)
                
                images.append(image_filename)
                print(f"Extracted image saved as {image_filename}")
    
    return images

# Example usage
docx_path = 'demo.docx'  # Path to your DOCX file
output_folder = 'images'  # Folder to save extracted images

# Extract images from the .docx file
extract_images(docx_path, output_folder)
