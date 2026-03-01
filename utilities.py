import svg
from random import random, choice

def rand(max):
    return random()*max

def asterisk():
    WIDTH = 10000
    HEIGHT = 10000

    stars = [
        svg.Text(
            text=xys[2],
            font_family="JetBrains Mono",
            font_size=40,
            fill="white",
            x=xys[0],
            y=xys[1],
            transform=f"rotate({rand(360)})",
            transform_origin=(xys[0], xys[1])
        )
        for xys in [(rand(WIDTH), rand(HEIGHT), choice(['+','.'])) for _ in range(1000)]
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