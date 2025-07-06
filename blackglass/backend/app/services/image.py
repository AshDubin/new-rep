from io import BytesIO
import requests
from PIL import Image
from PIL import ExifTags



def analyze_image(url: str):
    resp = requests.get(url)
    resp.raise_for_status()
    image = Image.open(BytesIO(resp.content))
    exif = image.getexif()
    exif_data = {ExifTags.TAGS.get(k, k): v for k, v in exif.items()}
    return {"format": image.format, "size": image.size, "exif": exif_data}
