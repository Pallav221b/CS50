from PIL import Image, ImageFilter

before = Image.open("loki.jpg")
after = before.filter(ImageFilter.BLUR)
after.save("out.jpg")
