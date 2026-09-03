css_content = """
body {
    background-color: #f4f4f9;
    background-image: url(d6zzgcg-0bcb4436-c270-4351-97af-f55074d54579.png);
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    font-family: 'Poppins', sans-serif;
    color: #333;
    line-height: 1.6;
}

html {
    scroll-behavior: smooth;
}

.main h1 {
    text-align: center;
    font-size: 50px;
    color: #2c3e50;
    margin-top: 50px;
    text-shadow: 2px 2px 4px rgba(255,255,255,0.8);
}
.main p {
    text-align: center;
    font-size: 22px;
    color: #34495e;
    max-width: 800px;
    margin: 0 auto;
    background: rgba(255, 255, 255, 0.85);
    padding: 20px;
    border-radius: 12px;
}

.introduction, .charecter, .levels, .race, .organisation {
    background: rgba(255, 255, 255, 0.90);
    margin: 40px auto;
    padding: 40px;
    max-width: 1000px;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

h1 {
    text-align: center;
    font-size: 36px;
    color: #1a252f;
    margin-bottom: 20px;
    border-bottom: 3px solid #e74c3c;
    padding-bottom: 10px;
}

h2, h3 {
    color: #c0392b;
    font-size: 28px;
    margin-top: 30px;
}

ul, ol {
    font-size: 20px;
    color: #2c3e50;
    margin-left: 20px;
}
li {
    margin-bottom: 10px;
}

/* Unified Row Styles for all characters */
div[class$="-row"] {
    display: flex;
    align-items: center;
    gap: 30px;
    margin-top: 30px;
    margin-bottom: 30px;
    width: 100%;
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    overflow: hidden;
}

div[class$="-row"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 25px rgba(0,0,0,0.15);
}

div[class^="para_"], .gotie-para {
    flex: 1;
    padding: 30px;
    display: flex;
    align-items: center;
}

div[class^="para_"] p, .gotie-para p {
    font-size: 18px;
    color: #444;
    margin: 0;
    text-align: left;
}

div[class$="-img"], .img {
    width: 250px;
    min-width: 250px;
    background: #fdfdfd;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
    border-left: 1px solid #eee;
}

/* Specific handling because images are sometimes on the left by default if they are placed first in html or flex reverse */
div[class$="-img"] img, .img img {
    width: 100%;
    max-height: 200px;
    object-fit: contain;
    border-radius: 12px;
    transition: transform 0.5s ease;
}

div[class$="-img"] img:hover, .img img:hover {
    transform: scale(1.08);
}

/* Organization section specific */
.gotie-li {
    display: flex;
    gap: 40px;
    padding: 20px;
    background: #f9f9f9;
    border-radius: 12px;
    margin-top: 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}
.left-list ul {
    list-style: none;
    font-weight: bold;
    color: #c0392b;
    margin: 0;
}
.right-list ul {
    list-style: none;
    margin: 0;
}

.introduction-org h1 {
    position: relative;
    isolation: isolate;
    text-align: center;
    color: #e74c3c;
    padding: 40px;
    border: 4px solid #e74c3c;
    border-radius: 12px;
    transition: transform 0.3s ease, background-color 0.3s ease, color 0.3s ease;
    cursor: pointer;
    background-color: transparent;
    margin: 40px auto;
    max-width: 600px;
}
.introduction-org h1::before {
    content: "";
    position: absolute;
    inset: 0;
    z-index: -1;
    background-image: url(OIP.jpg);
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    opacity: 0.2;
    border-radius: 8px;
    transition: opacity 0.3s ease;
}
.introduction-org h1:hover {
    transform: translateY(-4px);
    color: #fff;
    background-color: #e74c3c;
}
.introduction-org h1:hover::before {
    opacity: 0;
}
"""

with open('web.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Done")
