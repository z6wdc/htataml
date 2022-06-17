import os
from dotenv import load_dotenv
load_dotenv()

with open(os.getenv('INPUT')) as r:
    lines = r.readlines()

html = []

for line in lines:
    text = line.replace('\n', '<br />')
    if line == '\n':
        html.append(text)
    else:
        i = text.find('<br />')
        html.append('<p class="">' + text[:i] + '</p>' + text[i:])

with open(os.getenv('OUTPUT'), 'w') as rh:
    for e in html:
        rh.write(e + '\n')
