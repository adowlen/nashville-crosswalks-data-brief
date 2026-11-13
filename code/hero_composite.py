from PIL import Image, ImageDraw, ImageFont
import os, glob
HERE=os.path.dirname(__file__); ROOT=os.path.normpath(os.path.join(HERE,".."))
src=sorted(glob.glob(os.path.join(ROOT,"hero_source","*.webp")))[0]
im=Image.open(src).convert("RGB")
W,H=im.size
overlay=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(overlay)
for y in range(int(H*0.42)):
    a=int(200*(1-y/(H*0.42)))
    d.line([(0,y),(W,y)], fill=(10,12,14,a))
im=Image.alpha_composite(im.convert("RGBA"), overlay); d=ImageDraw.Draw(im)
def font(sz):
    for path in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        try: return ImageFont.truetype(path, sz)
        except: pass
    return ImageFont.load_default()
d.text((60,50),"37.5% of audited crosswalks",font=font(92),fill=(232,163,23,255))
d.text((60,160),"are recorded with Poor paint",font=font(92),fill=(255,255,255,255))
d.text((60,285),"683 of 1,823 records in Nashville's 2023 crosswalk audit",font=font(40),fill=(180,230,228,255))
d.text((60,345),"Machine Readable - Metro Nashville Crosswalks, Nov 13, 2026",font=font(34),fill=(220,220,220,255))
im.convert("RGB").save(os.path.join(ROOT,"hero.png"))
open(os.path.join(ROOT,"hero-headline.txt"),"w").write("37.5% of audited crosswalks are recorded with Poor paint\n")
print("hero done", im.size)
