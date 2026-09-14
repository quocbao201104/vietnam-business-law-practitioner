"""Build the Vietnam Business Law Practitioner vector kit.
Dependencies: fonttools, uharfbuzz, resvg-py, svglib, reportlab, Pillow, numpy, pypdf.
Use --deps to load an isolated dependency directory; no system font installation needed.
"""
import argparse,sys,json,hashlib,io,xml.etree.ElementTree as ET
from pathlib import Path
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument("--deps",help="Optional directory of Python dependencies")
args=ap.parse_args()
if args.deps: sys.path.insert(0,args.deps)
import numpy as np
from PIL import Image,ImageDraw,ImageFont
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.svgLib.path import parse_path
import uharfbuzz as hb
import resvg_py
from svglib.svglib import svg2rlg
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parent.parent
SOURCE=ROOT/"source"
M=json.loads((SOURCE/"master.json").read_text(encoding="utf-8"))
for name in ("svg","png","banner","favicon","pdf","qa"): (ROOT/name).mkdir(exist_ok=True)
FONT=SOURCE/M["font"]["file"]
FB=FONT.read_bytes()
REF=SOURCE/"reference.png"
refhash=hashlib.sha256(REF.read_bytes()).hexdigest()
font_meta=TTFont(FONT)
words=[]
for line in M["lines"]:
    axes={"wght":line["weight"],"opsz":M["font"]["opsz"]}
    ft=instantiateVariableFont(TTFont(FONT),axes,inplace=False)
    gs=ft.getGlyphSet();order=ft.getGlyphOrder();upem=ft["head"].unitsPerEm
    hf=hb.Font(hb.Face(FB));hf.scale=(upem,upem);hf.set_variations(axes);hb.ot_font_set_funcs(hf)
    buf=hb.Buffer();buf.add_str(line["text"]);buf.guess_segment_properties()
    hb.shape(hf,buf,{"kern":True,"liga":False})
    p=SVGPathPen(gs);offset=0;s=line["size"]/upem
    for info,pos in zip(buf.glyph_infos,buf.glyph_positions):
        gs[order[info.codepoint]].draw(TransformPen(p,(s,0,0,-s,offset+pos.x_offset*s,-pos.y_offset*s)))
        offset+=pos.x_advance*s+line["tracking"]
    raw=p.getCommands();bp=BoundsPen(None);parse_path(raw,bp)
    x0,y0,x1,y1=bp.bounds;a,b,c,d=line["targetInkBox"]
    sx=(c-a)/(x1-x0);sy=(d-b)/(y1-y0)
    matrix=(sx,0,0,sy,a-sx*x0,b-sy*y0)
    out=SVGPathPen(None);parse_path(raw,TransformPen(out,matrix))
    words.append({"d":out.getCommands(),"matrix":matrix,"bounds":[a,b,c,d]})

def svg(kind="symbol",variant="color",bg=None,editable=False):
    vb=M["favicon"]["viewBox"] if kind=="favicon" else M["symbolViewBox"] if kind=="symbol" else M["bannerViewBox"]
    color=M[variant]
    paths=M["favicon"]["paths"] if kind=="favicon" else M["paths"]
    x,y,w,h=vb
    elements=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    elements+='<g id="symbol" fill="'+color+'">'+''.join('<path id="'+p["id"]+'" d="'+p["d"]+'"/>' for p in paths)+'</g>'
    if kind=="lockup":
        for i,(line,word) in enumerate(zip(M["lines"],words)):
            if editable:
                mt=" ".join(f"{n:.9f}" for n in word["matrix"])
                elements+=f'<text transform="matrix({mt})" x="0" y="0" font-family="Inter" font-size="{line["size"]}" font-weight="{line["weight"]}" letter-spacing="{line["tracking"]}" style="font-optical-sizing:none;font-variation-settings:&#39;opsz&#39;32" fill="{color}">{line["text"]}</text>'
            else: elements+=f'<path id="word-{i+1}" fill="{color}" d="{word["d"]}"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{" ".join(map(str,vb))}" role="img" aria-label="{M["name"]}"><title>{M["name"]}</title><desc>Reconstructed vector artwork. {"Editable Inter replacement type." if editable else "All lettering outlined. No embedded raster or font dependency."}</desc>{elements}</svg>'
def write(p,t):p.write_text(t,encoding="utf-8",newline="\n")
def render(s,width=None,height=None):
    return Image.open(io.BytesIO(resvg_py.svg_to_bytes(svg_string=s,width=width,height=height,skip_system_fonts=True))).convert("RGBA")
def backed(im,color="#FFFFFF"):
    out=Image.new("RGBA",im.size,color);out.alpha_composite(im);return out.convert("RGB")
def ui_font(n):
    try:return ImageFont.truetype("arial.ttf",n)
    except OSError:return ImageFont.load_default(size=n)

for kind in ("symbol","lockup"):
    for v in ("color","black","white"):
        s=svg(kind,v);write(ROOT/"svg"/f"{kind}-{v}.svg",s)
        render(s).save(ROOT/"qa"/f"{kind}-{v}-render.png")
        if kind=="symbol":
            for n in (32,64,128,256,512,1024):
                render(s,n,n).save(ROOT/"png"/f"symbol-{v}-{n}.png")
        else:render(s).save(ROOT/"png"/f"lockup-{v}-1600.png")
for mode,v,bg in (("light","color","#FFFFFF"),("dark","white",M["color"])):
    s=svg("lockup",v,bg)
    write(ROOT/"banner"/f"readme-banner-{mode}.svg",s)
    render(s).convert("RGB").save(ROOT/"banner"/f"readme-banner-{mode}.png")
write(SOURCE/"lockup-editable.svg",svg("lockup","color",editable=True))
for v in ("color","black","white"):write(ROOT/"favicon"/f"favicon-optical-{v}.svg",svg("favicon",v))
fav=[render(svg("favicon"),n,n) for n in (16,32,48)]
fav[-1].save(ROOT/"favicon"/"favicon.ico",format="ICO",sizes=[(16,16),(32,32),(48,48)],append_images=fav[:-1])

pdf=ROOT/"pdf"/"vietnam-business-law-practitioner-vector.pdf"
c=canvas.Canvas(str(pdf));c.setTitle(M["name"]+" — Vector logo kit")
for v in ("color","black","white"):
    for kind in ("symbol","lockup"):
        drawing=svg2rlg(io.BytesIO(svg(kind,v).encode()))
        factor=(288 if kind=="symbol" else 576)/drawing.width
        w,h=drawing.width*factor,drawing.height*factor;c.setPageSize((w,h))
        if v=="white":
            c.setFillColorRGB(15/255,67/255,82/255);c.rect(0,0,w,h,fill=1,stroke=0)
        c.saveState();c.scale(factor,factor);renderPDF.draw(drawing,c,0,0);c.restoreState();c.showPage()
c.save()

# Check geometry, transparency, and outlined output.
ns={"s":"http://www.w3.org/2000/svg"}
checks={}
for kind in ("symbol","lockup"):
    signatures=[];alphas=[]
    for v in ("color","black","white"):
        r=ET.parse(ROOT/"svg"/f"{kind}-{v}.svg").getroot()
        assert not r.findall(".//s:image",ns) and not r.findall(".//s:text",ns)
        assert all("href" not in k for e in r.iter() for k in e.attrib)
        signatures.append([(e.tag,e.get("d"),e.get("transform")) for e in r.iter() if e.tag.endswith(("path","g"))])
        im=render(svg(kind,v))
        assert im.getchannel("A").getextrema()==(0,255)
        alphas.append(np.array(im)[:,:,3])
    assert signatures[0]==signatures[1]==signatures[2]
    assert all(np.array_equal(alphas[0],a) for a in alphas[1:])
    checks[kind+"_geometry_and_alpha_identical"]=True
for n in (32,64,128,256,512,1024):
    aa=[]
    for v in ("color","black","white"):
        im=Image.open(ROOT/"png"/f"symbol-{v}-{n}.png")
        assert im.mode=="RGBA" and im.size==(n,n)
        assert im.getchannel("A").getextrema()==(0,255) and im.getpixel((0,0))[3]==0
        aa.append(np.array(im)[:,:,3])
    assert all(np.array_equal(aa[0],a) for a in aa[1:])
ico=Image.open(ROOT/"favicon"/"favicon.ico")
assert ico.ico.sizes()=={(16,16),(32,32),(48,48)}
for dims in ico.ico.sizes():
    im=ico.ico.getimage(dims).convert("RGBA")
    assert im.getchannel("A").getextrema()==(0,255)
    assert np.array_equal(np.array(im),np.array(render(svg("favicon"),*dims)))
reader=PdfReader(pdf)
assert len(reader.pages)==6
for page in reader.pages:
    assert len(page.images)==0
    data=page.get_contents().get_data()
    assert b"Tj" not in data and b"TJ" not in data
    assert b" m" in data and b" l" in data

# Reference comparison is raster QA only; no bitmap is embedded into SVG/PDF.
ref=Image.open(REF).convert("RGB")
assert ref.size==(1672,941)
crop=ref.crop((118,209,630,721))
a=np.array(crop);mask=(a[:,:,0]<80)&(a[:,:,1]<130)
vmask=np.array(render(svg()))[:,:,3]>127
iou=float((mask&vmask).sum()/(mask|vmask).sum())
overlay=np.zeros((512,512,3),np.uint8)+255
overlay[mask]=[232,80,115];overlay[vmask]=[30,150,190];overlay[mask&vmask]=[15,67,82]
Image.fromarray(overlay).save(ROOT/"qa"/"symbol-overlay.png")
reference_lock=ref.crop((49,245,1649,685))
comparison=Image.new("RGB",(1280,690),"#F4F5F5");d=ImageDraw.Draw(comparison)
d.text((20,15),"PNG reference",font=ui_font(20),fill=M["color"])
d.text((660,15),"Vector / Inter replacement",font=ui_font(20),fill=M["color"])
comparison.paste(crop.resize((270,270)),(180,60))
comparison.paste(backed(render(svg(),270,270)),(820,60))
comparison.paste(reference_lock.resize((620,171)),(10,370))
comparison.paste(backed(render(svg("lockup"),620,171)),(650,370))
d.text((20,585),f"Symbol silhouette mask IoU: {iou:.4f}. Font is a documented substitute, not an exact-font claim.",font=ui_font(16),fill=M["color"])
d.text((20,625),"Banner: 1600 x 440 px. Original three-line hierarchy and logo-to-type spacing retained.",font=ui_font(16),fill=M["color"])
comparison.save(ROOT/"qa"/"reference-comparison.png")

small=Image.new("RGB",(1000,600),"white");d=ImageDraw.Draw(small)
for row,v in enumerate(("color","black","white")):
    y=20+row*135;d.text((20,y),v,font=ui_font(18),fill="black")
    for col,n in enumerate((16,32,64,128)):
        x=180+col*180
        small.paste(backed(render(svg("symbol",v),n,n),M["color"] if v=="white" else "#FFFFFF"),(x,y))
        d.text((x+134,y+14),str(n)+" px",font=ui_font(14),fill="black")
d.text((20,460),"Favicon optical",font=ui_font(18),fill="black")
for col,n in enumerate((16,32,48)):
    x=210+col*180;small.paste(backed(fav[col]),(x,460))
    d.text((x,530),str(n)+" px",font=ui_font(14),fill="black")
small.save(ROOT/"qa"/"small-size-check.png")
overview=Image.new("RGB",(1200,660),"white")
for row,v in enumerate(("color","black","white")):
    bg=M["color"] if v=="white" else "#FFFFFF"
    ImageDraw.Draw(overview).rectangle((0,row*220,1200,row*220+220),fill=bg)
    overview.paste(backed(render(svg("symbol",v),200,200),bg),(40,row*220+10))
    overview.paste(backed(render(svg("lockup",v),800,220),bg),(340,row*220))
overview.save(ROOT/"qa"/"vector-overview.png")
readme=Image.new("RGB",(920,610),"#F6F8FA");d=ImageDraw.Draw(readme)
readme.paste(backed(render(svg("lockup","color","#FFFFFF"),830,228)),(45,35))
d.text((45,310),"Vietnam Business Law Practitioner",font=ui_font(30),fill="#1F2328")
d.text((45,365),"Stable reasoning. Live law.",font=ui_font(20),fill="#1F2328")
d.line((45,415,875,415),fill="#D1D9E0")
d.text((45,445),"Preview at 830 px content width",font=ui_font(16),fill="#59636E")
d.text((45,485),"Banner keeps the selected logo and type hierarchy; extra vertical whitespace removed.",font=ui_font(16),fill="#59636E")
readme.save(ROOT/"qa"/"readme-width-preview.png")
preexisting=json.loads((SOURCE/"preexisting-sha256.json").read_text())
editable_bytes=resvg_py.svg_to_bytes(svg_path=str(SOURCE/"lockup-editable.svg"),skip_system_fonts=True,font_files=[str(FONT)])
(ROOT/"qa"/"editable-render.png").write_bytes(editable_bytes)
editable_mask=np.array(Image.open(io.BytesIO(editable_bytes)).convert("RGBA"))[:,:,3]>127
outlined_mask=np.array(render(svg("lockup")))[:,:,3]>127
editable_iou=float((editable_mask&outlined_mask).sum()/(editable_mask|outlined_mask).sum())
assert editable_iou>0.995
for folder in ("svg","banner","favicon"):
    for path in (ROOT/folder).glob("*.svg"):
        doc=ET.parse(path).getroot()
        assert not doc.findall(".//s:image",ns) and not doc.findall(".//s:text",ns)
        assert "data:" not in path.read_text(encoding="utf-8")
        im=render(path.read_text(encoding="utf-8"))
        if folder=="banner": assert im.getchannel("A").getextrema()==(255,255)
        else: assert im.getchannel("A").getextrema()==(0,255)
repo=ROOT.parent.parent
preexisting_status={p:("missing_at_final_check" if not (repo/p).is_file() else "unchanged" if hashlib.sha256((repo/p).read_bytes()).hexdigest()==sha else "changed_at_final_check") for p,sha in preexisting.items()}
assert hashlib.sha256(REF.read_bytes()).hexdigest()==refhash
checks.update(svg_main_files=6,banner_svg_files=2,svg_embedded_images=0,svg_distribution_text_elements=0,
 png_symbol_rgba_files=18,png_lockup_rgba_files=3,png_sizes=[32,64,128,256,512,1024],
 ico_sizes=[16,32,48],pdf_pages=6,pdf_raster_images=0,pdf_text_operators=0,
 symbol_mask_iou=iou,font_version=font_meta["name"].getDebugName(5),
 font_sha256=hashlib.sha256(FB).hexdigest(),reference_sha256=refhash,
 preexisting_assets_status=preexisting_status,reference_copy_unchanged=True,editable_vs_outlined_iou=editable_iou,word_optical_transforms=[w["matrix"] for w in words])
write(ROOT/"qa"/"verification.json",json.dumps(checks,indent=2))
print(json.dumps(checks,indent=2))
