from PIL import Image, ImageDraw, ImageFont
import os
os.makedirs(r'c:\Users\shara\OneDrive\Desktop\portfolio\client\public\projects', exist_ok=True)
for name,text in [('sign-language.jpg','Sign\nLanguage'),('exam-sensor.jpg','Exam\nSensor')]:
    img = Image.new('RGB',(400,240),(30,40,50))
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.load_default()
    except:
        f = None
    # calculate approximate text position
    try:
        w,h = d.textsize(text,font=f)
    except AttributeError:
        # fallback for newer Pillow
        bbox = d.textbbox((0,0), text, font=f)
        w,h = bbox[2]-bbox[0], bbox[3]-bbox[1]
    d.text(((400-w)/2,(240-h)/2),text,fill=(200,200,200),font=f)
    img.save(os.path.join(r'c:\Users\shara\OneDrive\Desktop\portfolio\client\public\projects',name))
print('placeholders created')
