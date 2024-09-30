import random
from sty import fg

colors = [fg.red, fg.green, fg.yellow, fg.blue, fg.magenta, fg.cyan, fg.white]

text = "ceci est un texte"
randomColor = random.choice(colors)

print(randomColor + text + fg.rs)
