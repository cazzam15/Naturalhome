from PIL import Image, ImageDraw, ImageFont
import os, math

# ── Paths ──────────────────────────────────────────────────────────
FONTS = r"C:\Users\cmorr\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\f9f802de-99a5-4ebf-af45-894de4052532\d5054810-f542-4da0-a4d4-6f3aae4aef0e\skills\canvas-design\canvas-fonts"
OUT   = r"C:\Users\cmorr\Downloads\Website\instagram"
os.makedirs(OUT, exist_ok=True)

def F(name): return os.path.join(FONTS, name)

# ── Fonts ──────────────────────────────────────────────────────────
def font(name, size): return ImageFont.truetype(F(name), size)

ITALIANA    = "Italiana-Regular.ttf"
LORA_I      = "Lora-Italic.ttf"
LORA_R      = "Lora-Regular.ttf"
LORA_B      = "Lora-Bold.ttf"
CRIMSON_I   = "CrimsonPro-Italic.ttf"
CRIMSON_R   = "CrimsonPro-Regular.ttf"
JURA_L      = "Jura-Light.ttf"
JURA_M      = "Jura-Medium.ttf"
INST_SANS   = "InstrumentSans-Regular.ttf"
INST_BOLD   = "InstrumentSans-Bold.ttf"

# ── Palette ────────────────────────────────────────────────────────
PAPER       = (250, 246, 239)
PAPER_WARM  = (242, 235, 223)
PAPER_DEEP  = (230, 219, 200)
INK         = (31,  27,  22 )
INK_SOFT    = (74,  67,  57 )
INK_MUTE    = (132, 122, 110)
RUST        = (160, 73,  45 )
SAGE        = (107, 127, 92 )
SAGE_D      = (63,  79,  51 )
GOLD        = (184, 137, 60 )
ROSE        = (185, 102, 94 )
TEAL        = (46,  107, 94 )
BROWN       = (123, 79,  46 )

SIZE = 1080

# ── Helpers ────────────────────────────────────────────────────────
def new_canvas(bg=PAPER):
    img = Image.new("RGB", (SIZE, SIZE), bg)
    return img, ImageDraw.Draw(img)

def cx(draw, text, y, fnt, fill, width=SIZE):
    """Centre text horizontally."""
    bb = draw.textbbox((0,0), text, font=fnt)
    w = bb[2] - bb[0]
    draw.text(((width - w) // 2, y), text, font=fnt, fill=fill)

def hline(draw, y, x0=80, x1=SIZE-80, fill=INK_MUTE, w=1):
    draw.line([(x0, y), (x1, y)], fill=fill, width=w)

def label(draw, text, y, fill=RUST, size=22):
    fnt = font(JURA_L, size)
    cx(draw, text.upper(), y, fnt, fill)

def footer(draw, accent=RUST):
    """Shared footer strip."""
    draw.rectangle([(0, SIZE-80), (SIZE, SIZE)], fill=INK)
    fnt_b  = font(ITALIANA, 28)
    fnt_h  = font(JURA_L, 18)
    cx(draw, "The Natural Home Collection", SIZE-58, fnt_b, PAPER_WARM)
    # handle bottom-right
    fnt_s = font(JURA_L, 16)
    draw.text((SIZE-290, SIZE-30), "@naturalhomelivinguk", font=fnt_s, fill=(200,190,178))

def ornament(draw, x, y, size=28, fill=RUST):
    fnt = font(ITALIANA, size)
    draw.text((x, y), "❋", font=fnt, fill=fill)

def wrap_text(draw, text, x, y, max_w, fnt, fill, line_gap=8):
    """Simple word-wrap. Returns final y."""
    words = text.split()
    lines, line = [], ""
    for w in words:
        test = (line + " " + w).strip()
        bb = draw.textbbox((0,0), test, font=fnt)
        if bb[2]-bb[0] <= max_w:
            line = test
        else:
            if line: lines.append(line)
            line = w
    if line: lines.append(line)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        bb = draw.textbbox((0,0), ln, font=fnt)
        y += (bb[3]-bb[1]) + line_gap
    return y

def volume_tag(draw, text, y, accent):
    label(draw, text, y, fill=accent, size=20)

# ══════════════════════════════════════════════════════════════════
# POST 1 — Brand Launch
# ══════════════════════════════════════════════════════════════════
def post_01():
    img, draw = new_canvas(PAPER)

    # Background botanical stem — centre
    def stem_leaf(cx_, cy, length, angle, col, alpha=200):
        rad = math.radians(angle)
        ex = cx_ + length * math.sin(rad)
        ey = cy - length * math.cos(rad)
        draw.line([(cx_, cy), (ex, ey)], fill=col, width=2)

    # Main stem
    sx = SIZE // 2
    for i in range(30):
        y_ = 820 - i * 22
        draw.ellipse([(sx-1, y_-1), (sx+1, y_+1)], fill=SAGE_D)
    draw.line([(sx, 180), (sx, 820)], fill=SAGE_D, width=2)

    # Leaves along stem
    leaf_positions = [280, 350, 430, 510, 590, 670, 750]
    for i, ly in enumerate(leaf_positions):
        side = -1 if i % 2 == 0 else 1
        lx = sx + side * 2
        ex = lx + side * (55 + (i % 3) * 10)
        ey = ly - 18
        draw.line([(lx, ly), (ex, ey)], fill=SAGE if i % 2 else SAGE_D, width=2)
        # leaf tip
        draw.ellipse([(ex-5, ey-5), (ex+5, ey+5)], fill=SAGE)

    # Flower at top
    fx, fy = sx, 180
    petal_len = 32
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        px = fx + int(petal_len * math.cos(rad))
        py = fy + int(petal_len * math.sin(rad))
        draw.line([(fx, fy), (px, py)], fill=RUST, width=3)
        draw.ellipse([(px-7, py-7), (px+7, py+7)], fill=RUST)
    draw.ellipse([(fx-12, fy-12), (fx+12, fy+12)], fill=PAPER)
    draw.ellipse([(fx-6, fy-6), (fx+6, fy+6)], fill=RUST)

    # Thin border
    draw.rectangle([(40, 40), (SIZE-40, SIZE-40)], outline=INK_MUTE, width=1)
    draw.rectangle([(48, 48), (SIZE-48, SIZE-48)], outline=(210, 200, 185), width=1)

    # Ornament
    cx(draw, "❋", 96, font(ITALIANA, 36), RUST)

    # Main headline — left column
    headline = font(ITALIANA, 88)
    draw.text((80, 160), "Slow", font=headline, fill=INK)
    draw.text((80, 240), "living,", font=font(LORA_I, 80), fill=INK)

    hline(draw, 340, x0=80, x1=460, fill=RUST, w=1)

    draw.text((80, 360), "plainly", font=font(CRIMSON_I, 52), fill=INK_SOFT)
    draw.text((80, 415), "written.", font=font(CRIMSON_I, 52), fill=INK_SOFT)

    hline(draw, 490, x0=80, x1=460, fill=INK_MUTE, w=1)

    sub_fnt = font(JURA_L, 22)
    wrap_text(draw, "Five handbooks for a calmer, more natural home.", 80, 510, 400, sub_fnt, INK_SOFT, line_gap=10)

    # Stats row
    hline(draw, 620, x0=80, x1=460, fill=(210,200,185), w=1)
    stats = [("5", "Handbooks"), ("170+", "Recipes"), ("£20", "Full series")]
    sx = 80
    for num, lbl in stats:
        draw.text((sx, 638), num, font=font(LORA_B, 36), fill=RUST)
        bb = draw.textbbox((0,0), num, font=font(LORA_B, 36))
        draw.text((sx, 678), lbl.upper(), font=font(JURA_L, 16), fill=INK_MUTE)
        sx += 130

    hline(draw, 720, x0=80, x1=460, fill=(210,200,185), w=1)

    # Tagline at bottom-left
    draw.text((80, 745), "Slow living, plainly written.", font=font(CRIMSON_I, 28), fill=INK_SOFT)

    # Domain
    draw.text((80, SIZE-108), "thenaturalhome.co.uk", font=font(JURA_L, 18), fill=INK_MUTE)

    footer(draw)
    img.save(os.path.join(OUT, "01-launch.png"))
    print("OK 01-launch.png")

# ══════════════════════════════════════════════════════════════════
# BOOK POSTS 2–6 — shared template
# ══════════════════════════════════════════════════════════════════
def rosette(draw, cx_, cy, r, accent):
    """Draw a small botanical rosette using circles — replaces ❋."""
    draw.ellipse([(cx_-r, cy-r), (cx_+r, cy+r)], fill=accent)
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        px = cx_ + int((r*1.8) * math.cos(rad))
        py = cy + int((r*1.8) * math.sin(rad))
        pr = int(r * 0.55)
        draw.ellipse([(px-pr, py-pr), (px+pr, py+pr)], fill=accent)
    # White centre dot
    draw.ellipse([(cx_-r//2, cy-r//2), (cx_+r//2, cy+r//2)], fill=PAPER)

def book_post(filename, vol_label, title_lines, hook, accent, bg_tint, illustration_fn, stats):
    img, draw = new_canvas(PAPER)

    # Accent band — top quarter
    draw.rectangle([(0, 0), (SIZE, 320)], fill=bg_tint)

    # Thin double rule below band
    hline(draw, 320, fill=accent, w=2)
    hline(draw, 324, fill=accent, w=1)

    # Volume label
    draw.text((80, 52), vol_label.upper(), font=font(JURA_L, 22), fill=accent)

    # Drawn rosette top-right (replaces ❋ text)
    rosette(draw, SIZE-72, 78, 9, accent)

    # Illustration in the band
    illustration_fn(draw, 540, 170, accent)

    # Title
    y = 360
    for i, line in enumerate(title_lines):
        fnt = font(ITALIANA, 72) if i == 0 else font(LORA_I, 64)
        col = INK if i == 0 else accent
        draw.text((80, y), line, font=fnt, fill=col)
        bb = draw.textbbox((0,0), line, font=fnt)
        y += (bb[3]-bb[1]) + 8

    hline(draw, y + 20, x0=80, x1=SIZE-80, fill=accent, w=1)

    # Hook
    y += 48
    hook_fnt = font(CRIMSON_I, 38)
    y = wrap_text(draw, f'"{hook}"', 80, y, SIZE-160, hook_fnt, INK_SOFT, line_gap=6)

    # Stats row — fills the gap after hook
    stat_y = max(y + 36, 660)
    # Decorative dot row
    for dx in range(0, 60, 16):
        draw.ellipse([(80+dx, stat_y), (86+dx, stat_y+6)], fill=accent)
    hline(draw, stat_y+3, x0=148, x1=SIZE-80, fill=(210,200,185), w=1)

    stat_y += 22
    for i, (num, lbl) in enumerate(stats):
        sx = 80 + i * 220
        draw.text((sx, stat_y), num, font=font(LORA_B, 32), fill=accent)
        bb = draw.textbbox((0,0), num, font=font(LORA_B, 32))
        draw.text((sx, stat_y + bb[3]-bb[1] + 4), lbl.upper(),
                  font=font(JURA_L, 17), fill=INK_MUTE)

    price_y = stat_y + 80
    hline(draw, price_y, x0=80, x1=SIZE-80, fill=(210,200,185), w=1)
    draw.text((80, price_y+14), "£3.99  ·  Kindle  ·  Amazon UK",
              font=font(JURA_L, 24), fill=INK_SOFT)

    # Domain
    hline(draw, SIZE-108, x0=80, x1=SIZE-80, fill=(210,200,185), w=1)
    draw.text((80, SIZE-98), "thenaturalhome.co.uk", font=font(JURA_L, 18), fill=INK_MUTE)

    # Thin border
    draw.rectangle([(30, 30), (SIZE-30, SIZE-30)], outline=(210, 200, 185), width=1)

    footer(draw, accent)
    img.save(os.path.join(OUT, filename))
    print(f"OK {filename}")

# ── Illustrations ──────────────────────────────────────────────────
def illus_spray(draw, cx_, cy, accent):
    # Spray bottle silhouette
    bx, by = cx_-25, cy-70
    draw.rectangle([(bx, by+30), (bx+50, by+120)], outline=accent, width=2)
    draw.rectangle([(bx+8, by+10), (bx+42, by+32)], fill=accent)
    draw.rectangle([(bx+20, by), (bx+30, by+12)], fill=SAGE_D)
    draw.line([(bx+30, by+4), (bx+70, by+4)], fill=SAGE_D, width=2)
    # Leaf accent
    for i in range(3):
        ox = bx - 40 - i*20
        oy = by + 30 + i*25
        draw.ellipse([(ox, oy), (ox+18, oy+10)], outline=SAGE, width=1)

def illus_flower(draw, cx_, cy, accent):
    for angle in range(0, 360, 60):
        rad = math.radians(angle)
        px = cx_ + int(38 * math.cos(rad))
        py = cy + int(38 * math.sin(rad))
        draw.ellipse([(px-14, py-14), (px+14, py+14)], fill=accent)
    draw.ellipse([(cx_-18, cy-18), (cx_+18, cy+18)], fill=PAPER_WARM)
    draw.ellipse([(cx_-8, cy-8), (cx_+8, cy+8)], fill=accent)
    # Stem
    draw.line([(cx_, cy+38), (cx_, cy+90)], fill=SAGE_D, width=2)
    draw.ellipse([(cx_-20, cy+60), (cx_, cy+70)], fill=SAGE, outline=SAGE)

def illus_jar(draw, cx_, cy, accent):
    jx, jy = cx_-35, cy-55
    draw.rectangle([(jx, jy+15), (jx+70, jy+110)], outline=accent, width=2)
    draw.rectangle([(jx-5, jy+8), (jx+75, jy+18)], fill=accent)
    draw.rectangle([(jx+8, jy+18), (jx+62, jy+110)], fill=(*accent[:3],) if len(accent)==3 else accent)
    # Carrot tops
    for i in range(5):
        ox = jx + 8 + i*14
        draw.line([(ox, jy+8), (ox-4, jy-28)], fill=SAGE, width=1)
    draw.ellipse([(jx+15, jy+50), (jx+55, jy+80)], outline=PAPER_WARM, width=1)

def illus_bottle(draw, cx_, cy, accent):
    bx, by = cx_-20, cy-65
    draw.rectangle([(bx, by+25), (bx+40, by+120)], fill=accent)
    draw.rectangle([(bx+8, by+10), (bx+32, by+27)], fill=SAGE_D)
    draw.rectangle([(bx+5, by+45), (bx+35, by+65)], fill=PAPER_WARM)
    # Leaves
    for side in [-1, 1]:
        ox = cx_ + side * 55
        draw.ellipse([(ox-15, cy-10), (ox+15, cy+10)], fill=SAGE)

def illus_paw(draw, cx_, cy, accent):
    draw.ellipse([(cx_-22, cy-18), (cx_+22, cy+18)], fill=accent)
    for dx, dy in [(-18,-22),(0,-28),(18,-22),(-28,0)]:
        draw.ellipse([(cx_+dx-9, cy+dy-9), (cx_+dx+9, cy+dy+9)], fill=accent)
    # Tin outline
    draw.ellipse([(cx_-48, cy-48), (cx_+48, cy+48)], outline=accent, width=1)

# ── Build posts 2-6 ────────────────────────────────────────────────
def post_02():
    book_post("02-green-clean.png", "— Volume I —",
              ["The Green", "Clean Handbook"],
              "Replace every shop-bought spray with 7 ingredients.",
              SAGE, (229, 235, 221), illus_spray,
              [("38", "Recipes"), ("34", "Pages")])

def post_03():
    book_post("03-natural-beauty.png", "— Volume II —",
              ["The Natural", "Beauty Handbook"],
              "Skincare, hair, body & lips — from oils, butters and the kindest plants.",
              ROSE, (245, 224, 221), illus_flower,
              [("32", "Recipes"), ("34", "Pages")])

def post_04():
    book_post("04-zero-waste.png", "— Volume III —",
              ["The Zero-Waste", "Kitchen"],
              "Save £800 a year. Turn yesterday's peelings into tonight's stock.",
              TEAL, (216, 232, 226), illus_jar,
              [("30", "Recipes"), ("32", "Pages")])

def post_05():
    book_post("05-herbal-remedies.png", "— Volume IV —",
              ["Natural Herbal", "Remedies at Home"],
              "Teas, tinctures, syrups & salves. Built from plants on a windowsill.",
              GOLD, (240, 229, 204), illus_bottle,
              [("35", "Recipes"), ("40", "Pages")])

def post_06():
    book_post("06-pet-care.png", "— Volume V —",
              ["Natural Pet", "Care at Home"],
              "Chemical-free grooming and gentle remedies for dogs and cats.",
              BROWN, (235, 223, 208), illus_paw,
              [("30", "Recipes"), ("33", "Pages")])

# ══════════════════════════════════════════════════════════════════
# RECIPE POSTS 7–11 — shared template
# ══════════════════════════════════════════════════════════════════
def recipe_post(filename, vol_tag, title, hook, ingredients, accent):
    img, draw = new_canvas(PAPER)

    # Left accent bar
    draw.rectangle([(0, 0), (10, SIZE)], fill=accent)

    # Thin border
    draw.rectangle([(30, 30), (SIZE-30, SIZE-30)], outline=(210, 200, 185), width=1)

    # Ornament top-right
    draw.text((SIZE-100, 50), "❋", font=font(ITALIANA, 38), fill=accent)

    # Tag + rule
    fnt_tag = font(JURA_L, 20)
    draw.text((80, 60), vol_tag.upper(), font=fnt_tag, fill=accent)
    hline(draw, 100, x0=80, x1=SIZE-80, fill=(210, 200, 185), w=1)

    # Title
    title_words = title.split()
    # Try to split into 2 lines naturally
    mid = len(title_words) // 2
    line1 = " ".join(title_words[:mid])
    line2 = " ".join(title_words[mid:])
    draw.text((80, 160), line1, font=font(ITALIANA, 74), fill=INK)
    draw.text((80, 238), line2, font=font(LORA_I, 66), fill=accent)

    hline(draw, 326, x0=80, x1=SIZE-80, fill=accent, w=1)

    # Hook
    hook_fnt = font(CRIMSON_I, 36)
    y = wrap_text(draw, hook, 80, 350, SIZE-160, hook_fnt, INK_SOFT, line_gap=8)

    # Ingredients section
    y = max(y + 40, 520)
    draw.text((80, y), "INGREDIENTS", font=font(JURA_L, 18), fill=INK_MUTE)
    hline(draw, y+28, x0=80, x1=SIZE-80, fill=(210,200,185), w=1)
    y += 44

    ing_fnt = font(LORA_R, 28)
    for i, ing in enumerate(ingredients):
        dot_x = 80
        draw.text((dot_x, y), "·", font=font(ITALIANA, 32), fill=accent)
        draw.text((dot_x+26, y), ing, font=ing_fnt, fill=INK_SOFT)
        y += 46
        if y > SIZE - 200:
            break

    # Callout box
    box_y = max(y + 20, 760)
    draw.rectangle([(80, box_y), (SIZE-80, box_y+70)], fill=PAPER_WARM)
    draw.rectangle([(80, box_y), (80+4, box_y+70)], fill=accent)
    draw.text((100, box_y+10),
              "Full recipe at thenaturalhome.co.uk",
              font=font(JURA_L, 22), fill=INK_SOFT)
    draw.text((100, box_y+38),
              "Free — no sign-up required.",
              font=font(CRIMSON_I, 22), fill=INK_MUTE)

    # Domain
    hline(draw, SIZE-108, x0=80, x1=SIZE-80, fill=(210,200,185), w=1)
    draw.text((80, SIZE-98), "thenaturalhome.co.uk", font=font(JURA_L, 18), fill=INK_MUTE)

    footer(draw, accent)
    img.save(os.path.join(OUT, filename))
    print(f"OK {filename}")

def post_07():
    recipe_post("07-recipe-spray.png",
                "Free Recipe · Vol. I  Green Clean",
                "Bicarbonate All-Purpose Spray",
                "Replaces 5 cleaning products. Costs 30p. Takes 5 minutes.",
                ["Bicarbonate of soda", "White vinegar", "Essential oil", "Warm water"],
                SAGE)

def post_08():
    recipe_post("08-recipe-lipbalm.png",
                "Free Recipe · Vol. II  Natural Beauty",
                "Four-Ingredient Lip Balm",
                "Ten minutes. Makes six tins. Lasts six months.",
                ["Beeswax", "Shea butter", "Sweet almond oil", "Raw honey"],
                ROSE)

def post_09():
    recipe_post("09-recipe-pesto.png",
                "Free Recipe · Vol. III  Zero-Waste Kitchen",
                "Carrot Top Pesto",
                "The leafy bits everyone bins. Free, fast, absurdly good.",
                ["Carrot tops", "Garlic", "Parmesan", "Olive oil", "Lemon"],
                TEAL)

def post_10():
    recipe_post("10-recipe-elderberry.png",
                "Free Recipe · Vol. IV  Herbal Remedies",
                "Elderberry Immune Syrup",
                "The £2 batch that replaces years of pharmacy runs.",
                ["Dried elderberries", "Raw honey", "Cloves", "Fresh ginger"],
                GOLD)

def post_11():
    recipe_post("11-recipe-pawbalm.png",
                "Free Recipe · Vol. V  Pet Care",
                "Winter Paw Balm",
                "Four ingredients. Protects paws from grit, salt & ice.",
                ["Beeswax", "Shea butter", "Coconut oil", "Calendula oil"],
                BROWN)

# ══════════════════════════════════════════════════════════════════
# POST 12 — Free Companion Guide
# ══════════════════════════════════════════════════════════════════
def post_12():
    img, draw = new_canvas(PAPER)

    # Dark ink panel — left half
    draw.rectangle([(0, 0), (SIZE//2, SIZE)], fill=INK)

    # Thin border inner left
    draw.rectangle([(20, 20), (SIZE//2 - 20, SIZE-20)], outline=(60, 54, 46), width=1)

    # Left panel content
    draw.text((52, 60), "FREE", font=font(JURA_M, 22), fill=RUST)
    draw.text((52, 88), "DOWNLOAD", font=font(JURA_M, 22), fill=RUST)
    hline(draw, 122, x0=52, x1=SIZE//2-52, fill=(70, 62, 52), w=1)

    draw.text((52, 148), "The", font=font(CRIMSON_I, 52), fill=(210, 200, 185))
    draw.text((52, 200), "Recommended", font=font(ITALIANA, 54), fill=PAPER)
    draw.text((52, 258), "Products", font=font(ITALIANA, 54), fill=PAPER)
    draw.text((52, 316), "List", font=font(LORA_I, 54), fill=RUST)

    hline(draw, 390, x0=52, x1=SIZE//2-52, fill=(70, 62, 52), w=1)

    facts = ["146 products", "12 categories", "20 pages", "No sign-up"]
    y = 410
    for f_txt in facts:
        draw.text((52, y), "—  " + f_txt, font=font(JURA_L, 24), fill=(180, 168, 152))
        y += 46

    hline(draw, y+10, x0=52, x1=SIZE//2-52, fill=(70,62,52), w=1)
    draw.text((52, y+26), "thenaturalhome.co.uk", font=font(JURA_L, 18), fill=(120,110,98))

    # Right panel — mock document stack
    # Background pages (offset)
    for offset, shade in [(18, PAPER_DEEP), (10, PAPER_WARM)]:
        draw.rectangle([(SIZE//2+52+offset, 80+offset),
                         (SIZE-52+offset, SIZE-100+offset)], fill=shade, outline=(200,190,175), width=1)

    # Front page
    px0, py0 = SIZE//2+52, 80
    px1, py1 = SIZE-52, SIZE-100
    draw.rectangle([(px0, py0), (px1, py1)], fill=PAPER, outline=(180,170,158), width=1)
    draw.rectangle([(px0+12, py0+12), (px1-12, py1-12)], outline=(210,200,185), width=1)

    # Page content
    pmid = (px0+px1)//2
    draw.text((pmid-60, py0+36), "— A COMPANION GUIDE —",
              font=font(JURA_L, 13), fill=RUST)
    draw.text((pmid-80, py0+72), "The", font=font(CRIMSON_I, 30), fill=INK_SOFT)
    draw.text((pmid-100, py0+104), "RECOMMENDED", font=font(JURA_M, 22), fill=INK)
    draw.text((pmid-50, py0+134), "Products", font=font(LORA_I, 34), fill=RUST)
    draw.text((pmid-30, py0+172), "LIST", font=font(JURA_M, 22), fill=INK)

    # Rule with ornament
    hline(draw, py0+212, x0=px0+40, x1=px1-40, fill=RUST, w=1)
    draw.text((pmid-10, py0+200), "❋", font=font(ITALIANA, 22), fill=RUST)

    # Faux text lines
    line_y = py0 + 240
    for i in range(9):
        w_ = (px1-px0-80) if i % 3 != 2 else (px1-px0-130)
        shade_ = (220, 212, 198) if i % 2 == 0 else (210, 202, 188)
        draw.rectangle([(px0+40, line_y), (px0+40+w_, line_y+6)], fill=shade_)
        line_y += 20

    draw.text((pmid-52, py1-48), "by C. Morrison",
              font=font(CRIMSON_I, 20), fill=INK_SOFT)

    # Tag ribbon
    draw.rectangle([(px1-90, py0-14), (px1+10, py0+16)], fill=INK)
    draw.text((px1-82, py0-12), "FREE · 20 PP", font=font(JURA_L, 14), fill=PAPER_WARM)

    # Right panel border
    draw.rectangle([(SIZE//2, 0), (SIZE//2+2, SIZE)], fill=PAPER)  # seam
    draw.rectangle([(SIZE-30, 30), (SIZE-30, SIZE-30)], outline=(210,200,185), width=1)

    footer(draw, RUST)
    img.save(os.path.join(OUT, "12-free-guide.png"))
    print("OK 12-free-guide.png")

# ── Run all ────────────────────────────────────────────────────────
post_01()
post_02()
post_03()
post_04()
post_05()
post_06()
post_07()
post_08()
post_09()
post_10()
post_11()
post_12()
print("All 12 posts generated.")
