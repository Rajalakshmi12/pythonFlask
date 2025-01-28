from pathlib import Path
from PIL import Image
import os

def compress_losslessly(input_path, output_path, target_size):
    """
    Compress an image losslessly to achieve a target file size.
    """
    with Image.open(input_path) as img:
        # Do not convert from RGBA to RGB
        
        # Start with original dimensions
        width, height = img.size
        while True:
            # Save the image as WEBP losslessly
            img.save(output_path, format="WEBP", lossless=True)
            
            # Check file size
            if os.path.getsize(output_path) <= target_size:
                break
            
            # Reduce dimensions by 10% each iteration
            width = int(width * 1)
            height = int(height * 1)
            img = img.resize((width, height), Image.LANCZOS)
    
    return os.path.getsize(output_path)

# Example Usage
input_image = Path(r"c:\Users\poort\OneDrive\Desktop\My IITM Course\Semester 4 Jan 2025\Images_for_comp\shapes.png")
output_image = Path(r"c:\Users\poort\OneDrive\Desktop\My IITM Course\Semester 4 Jan 2025\Images_for_comp\shapes.webp")
target_size = 1500  # Target size in bytes
    

final_size = compress_losslessly(input_image, output_image, target_size)
print(f"Final size: {final_size} bytes")
