from django import template

register = template.Library()

@register.filter
def stars(rating, max_stars=5):
    try:
        rating = float(rating or 0)
    except (TypeError, ValueError):
        rating = 0.0

    half_steps = int(round(rating * 2)) 
    full = half_steps // 2
    half = half_steps % 2

    out = ["full"] * min(full, max_stars)
    if len(out) < max_stars and half:
        out.append("half")
    while len(out) < max_stars:
        out.append("empty")
    return out