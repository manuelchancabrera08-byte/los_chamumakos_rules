import os, json, base64, random, textwrap
from pathlib import Path
from datetime import datetime, timezone
from PIL import Image, ImageDraw, ImageFont
from openai import OpenAI

ROOT = Path(__file__).resolve().parents[1]
REF_DIR = ROOT / "personajes" / "don_mako"
READY = ROOT / "memes" / "ready"
HISTORY = ROOT / "memes" / "history.json"
READY.mkdir(parents=True, exist_ok=True)
REF_DIR.mkdir(parents=True, exist_ok=True)

IDEAS = [
    {"text":"CUANDO TE DICEN:\n“NO HAY SISTEMA”\nMAKO: “PUES LLÁMALO.”",
     "scene":"Don Mako at the checkout of a modest Mexican neighborhood convenience store, holding cash, calmly looking toward an off-camera cashier after being told the system is down."},
    {"text":"MI CARRO NO ESTÁ VIEJO\nES CLÁSICO.",
     "scene":"Don Mako proudly leaning beside an old worn compact Mexican car on a neighborhood street, presenting it as if it were a collectible luxury classic."},
    {"text":"¿ESE HOYO EN EL TECHO?\nES EL QUEMACOCO.",
     "scene":"Don Mako inside an old compact car, confidently pointing at a rough improvised opening in the roof as though it were a factory sunroof."},
    {"text":"“BÁJALE A LA BOCINA”\nPUES MÉTASE A SU CASA.",
     "scene":"Don Mako outside his modest neighborhood house beside a very large speaker, relaxed and unapologetic, while a neighbor complains from off camera."},
    {"text":"YO NO LLEGO TARDE\nLA REUNIÓN EMPEZÓ TEMPRANO.",
     "scene":"Don Mako arriving calmly at a modest family gathering where everyone is already seated, acting completely convinced he is on time."},
    {"text":"NO ESTOY DESCANSANDO\nESTOY SUPERVISANDO SENTADO.",
     "scene":"Don Mako sitting comfortably in a hammock in a modest patio, watching activity off camera with the serious expression of a supervisor."},
    {"text":"SI TODAVÍA PRENDE\nTODAVÍA SIRVE.",
     "scene":"Don Mako proudly standing beside a visibly old battered household appliance that is somehow still working."},
    {"text":"“¿Y EL MANUAL?”\nYO TENGO EXPERIENCIA.",
     "scene":"Don Mako assembling a household object without instructions, extra screws scattered nearby, totally confident despite the questionable result."},
    {"text":"NO ESTÁ CHUECO\nES DISEÑO ARTESANAL.",
     "scene":"Don Mako proudly admiring a visibly crooked homemade shelf in a modest Mexican home as if it were premium craftsmanship."},
    {"text":"YO SÍ AHORRO\nNOMÁS QUE EL DINERO NO COOPERA.",
     "scene":"Don Mako at a modest neighborhood café opening an almost empty wallet, looking at it with dry disappointment."},
    {"text":"NO ME PERDÍ\nESTOY CONOCIENDO OTRA RUTA.",
     "scene":"Don Mako beside an old car on an unfamiliar neighborhood street, looking around while pretending the detour was intentional."},
    {"text":"YO NO DISCUTO\nEXPLICO POR QUÉ TENGO RAZÓN.",
     "scene":"Don Mako at a small family table calmly gesturing while someone off camera clearly disagrees with him."},
    {"text":"NO ES TERQUEDAD\nES EXPERIENCIA CONVENCIDA.",
     "scene":"Don Mako standing with arms crossed in a modest patio, half-lidded eyes, completely certain of himself while someone off camera argues."},
    {"text":"“MAKO, ESO NO VA AHÍ”\nAHORITA VEMOS.",
     "scene":"Don Mako doing a simple home repair with one obviously misplaced part, tool in hand, still completely confident."},
    {"text":"CUANDO TE DICEN “ES RÁPIDO”\nY SACAN UNA SILLA PARA QUE ESPERES.",
     "scene":"Don Mako sitting on a plastic chair waiting in a modest neighborhood office, arms crossed and half-lidded expression."},
    {"text":"NO ES IMPROVISADO\nES EDICIÓN LIMITADA.",
     "scene":"Don Mako proudly showing an improvised household object made from mismatched reused parts in a modest backyard."}
]

def load_history():
    if HISTORY.exists():
        try:
            return json.loads(HISTORY.read_text(encoding="utf-8"))
        except Exception:
            pass
    return []

def choose_idea(history):
    recent = {x.get("text") for x in history[-12:]}
    pool = [x for x in IDEAS if x["text"] not in recent] or IDEAS
    return random.choice(pool)

def references():
    files = []
    for pat in ("*.png","*.jpg","*.jpeg","*.webp"):
        files.extend(REF_DIR.glob(pat))
    return sorted(files)

def fit_4x5(img):
    target_ratio = 4/5
    w,h = img.size
    r=w/h
    if r > target_ratio:
        nw=int(h*target_ratio); left=(w-nw)//2
        img=img.crop((left,0,left+nw,h))
    elif r < target_ratio:
        nh=int(w/target_ratio); top=(h-nh)//2
        img=img.crop((0,top,w,top+nh))
    return img.resize((1080,1350), Image.Resampling.LANCZOS)

def font(size):
    paths=[
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"
    ]
    for p in paths:
        if Path(p).exists(): return ImageFont.truetype(p,size)
    return ImageFont.load_default()

def wrap_line(draw, text, fnt, max_width):
    words=text.split()
    lines=[]; cur=""
    for word in words:
        test=(cur+" "+word).strip()
        if draw.textbbox((0,0),test,font=fnt,stroke_width=2)[2] <= max_width:
            cur=test
        else:
            if cur: lines.append(cur)
            cur=word
    if cur: lines.append(cur)
    return lines

def overlay(img, meme_text):
    d=ImageDraw.Draw(img)
    f=font(58)
    lines=[]
    for raw in meme_text.split("\n"):
        lines.extend(wrap_line(d, raw, f, 960) or [""])
    y=55
    for line in lines:
        box=d.textbbox((0,0),line,font=f,stroke_width=5)
        x=(1080-(box[2]-box[0]))//2
        d.text((x,y),line,font=f,fill="white",stroke_width=5,stroke_fill="black")
        y += (box[3]-box[1])+14

    brand="Chapumakos"
    follow="síguenos @chapumakos"
    fb=font(30); fs=font(23)
    margin=28
    b1=d.textbbox((0,0),brand,font=fb,stroke_width=2)
    b2=d.textbbox((0,0),follow,font=fs,stroke_width=2)
    w=max(b1[2],b2[2])+28; h=78
    x=1080-w-margin; y=1350-h-margin
    d.rounded_rectangle((x,y,x+w,y+h),radius=14,fill=(0,0,0,150))
    d.text((x+14,y+8),brand,font=fb,fill="white",stroke_width=1,stroke_fill="black")
    d.text((x+14,y+44),follow,font=fs,fill="white",stroke_width=1,stroke_fill="black")
    return img

def main():
    refs=references()
    if not refs:
        raise SystemExit("Faltan referencias de Don Mako en personajes/don_mako")

    history=load_history()
    idea=choose_idea(history)
    prompt=f"""Use the supplied reference image(s) as the exact identity reference for Don Mako.
Create a NEW photorealistic social-media meme photograph in portrait 4:5 composition.

CHARACTER LOCK:
Don Mako is the same realistic anthropomorphic capuchin monkey shown in the references.
Preserve his recognizable face, natural imperfect fur, realistic facial skin folds and wrinkles,
slightly oversized round head, half-lidded eyes, calm street-smart Mexican-neighborhood attitude,
serious confident expression, short compact tail, realistic hands, feet and anatomy.
Do not cartoonize him. Do not make the fur polished, segmented or plastic-looking.

SCENE:
{idea['scene']}

STYLE:
Authentic everyday Mexican neighborhood realism. Modest believable environment, natural practical lighting,
candid photographic look, subtle dry humor. Don Mako is clearly the protagonist. No fantasy, no magic,
no written text, no captions, no logos, no watermark. Leave useful negative space near the upper area
because meme text will be added later. Avoid duplicate limbs, extra fingers, malformed hands or feet.
"""

    client=OpenAI()
    selected=refs[:3]
    handles=[open(p,"rb") for p in selected]
    try:
        result=client.images.edit(
            model="gpt-image-2",
            image=handles if len(handles)>1 else handles[0],
            prompt=prompt,
            size="1024x1280",
            quality="medium"
        )
    finally:
        for h in handles: h.close()

    raw=base64.b64decode(result.data[0].b64_json)
    stamp=datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    tmp=READY/f"_raw_{stamp}.png"
    tmp.write_bytes(raw)
    img=Image.open(tmp).convert("RGB")
    img=fit_4x5(img)
    img=overlay(img,idea["text"])
    out=READY/f"mako_{stamp}.jpg"
    img.save(out,"JPEG",quality=94,optimize=True)
    tmp.unlink(missing_ok=True)

    meta={
        "id":stamp,
        "created_at":datetime.now(timezone.utc).isoformat(),
        "image":out.name,
        "meme_text":idea["text"],
        "scene":idea["scene"],
        "caption":idea["text"].replace("\n"," "),
        "hashtags":["#Chapumakos","#DonMako","#HumorMexicano","#Memes","#ParaTi"],
        "status":"ready"
    }
    (READY/f"mako_{stamp}.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding="utf-8")
    history.append(meta)
    HISTORY.write_text(json.dumps(history[-200:],ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(meta,ensure_ascii=False))

if __name__=="__main__":
    main()
