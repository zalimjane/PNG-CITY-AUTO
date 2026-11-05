import os
from PIL import Image, ImageEnhance, ImageDraw
import requests
from io import BytesIO

print("=== PNG Automation Bot Started ===")

output_dir = "processed_pngs"
os.makedirs(output_dir, exist_ok=True)

filename = "processed_image.png"
file_path = os.path.join(output_dir, filename)

# 100% reliable public image URL (Wikimedia Commons)
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png"

try:
    print(f"Fetching image from web...")
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(image_url, headers=headers, timeout=10)
    
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content)).convert("RGBA")
        print("Image successfully fetched from web!")
    else:
        print("Web fetch failed, generating fallback PNG object...")
        img = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        d.rectangle([40, 40, 160, 160], fill=(34, 139, 34, 220))

except Exception as e:
    print(f"Error occurred: {e}. Generating fallback PNG object...")
    img = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle([40, 40, 160, 160], fill=(34, 139, 34, 220))

# Color Scheme / Saturation Enhancement
enhancer = ImageEnhance.Color(img)
img_modified = enhancer.enhance(1.8) 

# Save modified image
img_modified.save(file_path, "PNG")
print(f"Successfully saved locally at: {file_path}")
print("=== Bot Finished Successfully ===")
