def f(t,n):
    from PIL import Image, ImageDraw, ImageFont
    im = Image.new("RGB", (200,200), color=("#00F0FF"))
    font = ImageFont.truetype("C:/Windows/Fonts/Bahnschrift.ttf", size=22)
    draw_text = ImageDraw.Draw(im)
    draw_text.text((100,100),
        t,
        font = font,
        fill=("#FFFFFF"))
    im.show()
    im.save(f"C:/Users/user/Documents/142/мельниккартинки{n}.jpg")
    
t = ["1",
     "2",
     "3"]
for i in range (3):
    f(t[i],i)
    
