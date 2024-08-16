from docx import Document
import requests
import os

def extract_images(docx_path, output_folder):
    doc = Document(docx_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    images = []
    for rel in doc.part.rels.values():
        if rel.target_ref.endswith('.jpeg') or rel.target_ref.endswith('.png'):
            image_data = rel.target_part.blob
            image_ext = rel.target_part.content_type.split('/')[1]
            image_filename = os.path.join(output_folder, f"image_{rel.target_part.partname.split('/')[-1]}.{image_ext}")
            
            with open(image_filename, 'wb') as img_file:
                img_file.write(image_data)
            
            images.append(image_filename)
            print(f"Extracted image saved as {image_filename}")
    
    return images



# Example usage
docx_path = 'demo.docx'
output_folder = 'images'

# Extract images from the .docx file
extract_images(docx_path, output_folder)


