from PIL import Image, ImageDraw
with Image.open('photo.jpg') as img:
    draw = ImageDraw.Draw(img)
    draw.text((593,356),'ARTEM')
    img2=Image.open('ZNAK.jpg').resize((459,343))
    img.paste(img2,(351,567))
    img.show()