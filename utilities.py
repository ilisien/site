import svg
from random import random

def rand(max):
    return random()*max

def asterisk():
    WIDTH = 2000
    HEIGHT = 2000

    stars = [
        svg.Text(
            text="*",
            font_family="monospace",
            fill="white",
            x=xy[0],
            y=xy[1],
            transform=f"rotate({rand(360)})",
            transform_origin=(xy[0], xy[1])
        )
        for xy in [(rand(WIDTH), rand(HEIGHT)) for _ in range(1000)]
    ]

    group = svg.G(
        elements=stars,
        transform="rotate(0, 1000, 1000)" 
    )

    canvas = svg.SVG(
        width=WIDTH,
        height=HEIGHT,
        elements=[group]
    )

    with open("static/asterisk.svg", "w") as f:
        f.write(str(canvas))

if __name__ == "__main__":
    asterisk()