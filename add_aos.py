import re

with open('web.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add AOS css
content = content.replace('</head>', '    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">\n</head>')

# Add AOS js
content = content.replace('</body>', '    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n    <script>AOS.init({duration: 1000, once: true});</script>\n</body>')

# Add data-aos attributes to rows
content = re.sub(r'<div\s+class\s*=\s*[\'"]([a-zA-Z0-9_\.-]+row)[\'"]', r'<div class="\1" data-aos="fade-up"', content)
# It seems `class = "kush.row"` is in there, so `\.-` handles dots as well.

# Let's also animate titles
content = re.sub(r'<div\s+class\s*=\s*[\'"](introduction|charecter|levels|race|organisation)[\'"]', r'<div class="\1" data-aos="fade-in"', content)

# Write back
with open('web.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
