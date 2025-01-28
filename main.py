from pathlib import Path
from PIL import Image
import asyncio

async def compress_image(input_path: Path, output_path: Path, quality: int = 1) -> None:
    """Compress an image while maintaining reasonable quality."""
    with Image.open(input_path) as img:
        # Convert RGBA to RGB if needed
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        # Optimize and save as WEBP
        img.save(output_path, 'WEBP', quality=quality, optimize=True)

async def batch_compress_images(input_dir: Path, quality: int = 100):
    """Batch compress images in a directory."""
    paths = input_dir.glob('*.png')
    for p in paths:
        await compress_image(p, p.with_suffix('.webp'), quality=quality)

# Define the main async function
async def main():
    input_dir = Path(r'C:\Users\poort\OneDrive\Desktop\My IITM Course\Semester 4 Jan 2025\Images_for_comp')
    await batch_compress_images(input_dir)

# Run the main async function
if __name__ == "__main__":
    asyncio.run(main())