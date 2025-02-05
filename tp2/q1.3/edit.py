from PIL import Image, ImageFilter, ImageEnhance
import os


def get_files():
    files = []
    try:
        with os.scandir("./images/") as directory:
            for content in directory:
                if content.is_file(follow_symlinks=False):
                    files.append(content.name)
        return files
    except PermissionError:
        print(f"Access denied")

for file in get_files():
    img = Image.open(f"./images/{file}")
    
    embossed = img.filter(ImageFilter.EMBOSS)
    enhanced = ImageEnhance.Contrast(embossed).enhance(3.0)
    enhanced.save(f"./embossed/{file}")

    blurred = img.filter(ImageFilter.GaussianBlur(6))
    blurred.save(f"./blurred/{file}")
    

    
