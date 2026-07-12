from PIL import Image
import io

def compress_image(image_bytes, quality):
    img = Image.open(io.BytesIO(image_bytes))
    
    # Convert RGBA to RGB if saving as JPEG
    if img.mode in ('RGBA', 'LA'):
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])
        img = background
    elif img.mode != 'RGB':
        img = img.convert('RGB')
        
    out_buffer = io.BytesIO()
    img.save(out_buffer, format="JPEG", quality=quality, optimize=True)
    return out_buffer.getvalue()