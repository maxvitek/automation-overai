"""Generate Aegis profile picture — geometric shield motif."""
from PIL import Image, ImageDraw, ImageFont
import math

SIZE = 512
CENTER = SIZE // 2
img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# --- Background: dark circle ---
draw.ellipse([16, 16, SIZE - 16, SIZE - 16], fill=(18, 18, 28))

# --- Shield shape (hexagon-ish, pointed at bottom) ---
def shield_points(cx, cy, r, squash=0.85):
    """Create a pointed shield polygon."""
    pts = []
    # Top arc (wider)
    for angle in range(-140, -40, 5):
        rad = math.radians(angle)
        pts.append((cx + r * math.cos(rad), cy + r * 0.75 * math.sin(rad)))
    # Right side curving down to point
    pts.append((cx + r * 0.74, cy + r * 0.15))
    pts.append((cx + r * 0.6, cy + r * 0.55))
    pts.append((cx + r * 0.35, cy + r * 0.85))
    # Bottom point
    pts.append((cx, cy + r * 1.1))
    # Left side (mirror)
    pts.append((cx - r * 0.35, cy + r * 0.85))
    pts.append((cx - r * 0.6, cy + r * 0.55))
    pts.append((cx - r * 0.74, cy + r * 0.15))
    return pts

# Outer shield glow
for i in range(3, 0, -1):
    glow_pts = shield_points(CENTER, CENTER - 10, 180 + i * 4)
    alpha = 40 + i * 15
    draw.polygon(glow_pts, fill=(80, 180, 255, alpha))

# Main shield
pts = shield_points(CENTER, CENTER - 10, 180)
# Gradient-ish fill: draw multiple slightly smaller shields
for i in range(180, 0, -2):
    frac = i / 180
    inner_pts = shield_points(CENTER, CENTER - 10, i)
    r = int(20 + 30 * (1 - frac))
    g = int(80 + 120 * (1 - frac))
    b = int(160 + 90 * (1 - frac))
    draw.polygon(inner_pts, fill=(r, g, b))

# --- Inner geometric pattern: nested chevrons ---
for j in range(4):
    offset = 25 + j * 30
    alpha = 200 - j * 40
    w = 2
    chevron_y = CENTER - 50 + j * 35
    half_w = 80 - j * 15
    # Chevron lines
    line_pts = [
        (CENTER - half_w, chevron_y),
        (CENTER, chevron_y + 30),
        (CENTER + half_w, chevron_y),
    ]
    draw.line(line_pts, fill=(220, 240, 255, alpha), width=w + 1)

# --- Central eye/circle motif ---
draw.ellipse(
    [CENTER - 22, CENTER - 35, CENTER + 22, CENTER + 9],
    fill=(240, 248, 255),
    outline=(180, 220, 255),
    width=2,
)
draw.ellipse(
    [CENTER - 10, CENTER - 23, CENTER + 10, CENTER - 3],
    fill=(18, 18, 28),
)

# --- Subtle ring around shield ---
draw.ellipse(
    [24, 24, SIZE - 24, SIZE - 24],
    outline=(80, 180, 255, 100),
    width=2,
)

# --- Save ---
out_path = "/Users/overai/.openclaw/workspace/aegis_profile.png"
img.save(out_path, "PNG")
print(f"Saved to {out_path}")
