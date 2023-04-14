import random

colors = ["black", "brown", "red", 
        "orange", "yellow", "green", 
        "blue", "violet", "gray", 
        "white", "gold", "silver"]

color_band = {
    "black": "0", 
    "brown": "1", 
    "red": "2", 
    "orange": "3", 
    "yellow": "4", 
    "green": "5", 
    "blue": "6", 
    "violet": "7", 
    "gray": "8", 
    "white": "9"
}

# color_multiplier = {
#     "black": 0, 
#     "brown": 1, 
#     "red": 2, 
#     "orange": 3, 
#     "yellow": 4, 
#     "green": 5, 
#     "blue": 6, 
#     "violet": 7, 
#     "gold": -10, 
#     "silver": -100 
# }

color_multiplier = {
    "black": "1", 
    "brown": "10", 
    "red": "100", 
    "orange": "1k", 
    "yellow": "10k", 
    "green": "100k", 
    "blue": "1M", 
    "violet": "10M", 
    "gold": "0.1", 
    "silver": "0.01"
}

color_tolerance = {
    "brown": "1",
    "red": "2",
    "green": "0.50",
    "blue": "0.25",
    "violet": "0.10",
    "gold": "5",
    "silver": "10",
}


def resistor(c1, c2, c3, c4):
    r = \
"""
\\begin{tikzpicture}
    \definecolor{gold}{rgb}{1, 0.843, 0}
    \definecolor{silver}{rgb}{0.753, 0.753, 0.753}
    \\filldraw [gray!30]  (-0.5, -0.5) -- ++(0, 2)  -- ++(4.5, 0) -- ++(0, -2) -- cycle;
    \draw [ultra thick, %s] (0, 0) -- (0, 1);
    \draw [ultra thick, %s] (1, 0) -- (1, 1);
    \draw [ultra thick, %s] (2, 0) -- (2, 1);
    \draw [ultra thick, %s] (3.5, 0) -- (3.5, 1);
\end{tikzpicture}
"""

    r = r % (c1,c2,c3,c4)

    return r

def resistor_value(c1, c2, c3, c4):
             r = color_band[c1]+color_band[c2] + " x "  + color_multiplier[c3] + " +- "  + color_tolerance[c4] + " %"
             return r


def random_color():
    s1 = random.sample(list(color_band)[1:], 1)
    s2 = random.sample(list(color_band), 1)
    s3 = random.sample(list(color_multiplier), 1)
    s4 = random.sample(list(color_tolerance), 1)

    return s1 + s2 + s3 + s4


if __name__ == "__main__":
    seed_n = 1703
    random.seed(seed_n)
    N = 30

    rcolor = [random_color() for i in range(N)]

    with open(f"src/motstand_oppgaver_s{seed_n}.tex", "w") as f:
        for c in rcolor:
            print(resistor(*c), file=f)

    with open(f"fasit_motstand_oppgaver_s{seed_n}.txt", "w") as f:
        for i, c in enumerate(rcolor):
            value = resistor_value(*c)
            print(f"{i + 1}) {c}\n    {value}\n", file=f)











