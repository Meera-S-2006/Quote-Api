import os
import json
import random
import time
from xml.sax.saxutils import escape
from string import Template
from flask import Flask, Response
from api.Images import Images_Url

app = Flask(__name__)   

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FACTS_PATH = os.path.join(BASE_DIR, "facts.json")




def load_facts():
    try:
        if not os.path.exists(FACTS_PATH):
            return ["No facts file found."]
        with open(FACTS_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                facts = data.get("facts", [])
            elif isinstance(data, list):
                facts = data
            else:
                facts = []
            facts = [str(x) for x in facts]
            return facts or ["No facts available."]
    except Exception as exc:
        return [f"Could not load facts: {str(exc)}"]


from string import Template
from xml.sax.saxutils import escape

def make_svg(text):
    t = escape(text)
    Png = random.choice(Base64Codes) 
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="760" height="250" viewBox="0 0 760 250">

  <defs>

    
    <linearGradient id="cuteGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffe5f1"/>
      <stop offset="100%" stop-color="#e3f2ff"/>
    </linearGradient>

    
    <radialGradient id="blobPink" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffd5f7"/>
      <stop offset="100%" stop-color="#ffd5f700"/>
    </radialGradient>

    <radialGradient id="blobBlue" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#d6efff"/>
      <stop offset="100%" stop-color="#d6efff00"/>
    </radialGradient>

    
    <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="14" result="blur"/>
      <feOffset dx="0" dy="6" result="offsetBlur"/>
      <feFlood flood-color="rgba(0,0,0,0.15)"/>
      <feComposite in2="offsetBlur" operator="in"/>
      <feMerge>
        <feMergeNode/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    
    <style>
      .fadeIn {{
        opacity: 0;
        animation: fadeIn 1.4s ease forwards 0.3s;
      }}
      @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(6px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}

      .sparkle {{
        animation: twinkle 1.8s infinite ease-in-out alternate;
      }}
      @keyframes twinkle {{
        from {{ opacity: 0.2; transform: scale(0.8); }}
        to {{ opacity: 1; transform: scale(1.3); }}
      }}
    </style>

  </defs>

  
  <rect width="100%" height="100%" rx="38"
        fill="url(#cuteGrad)" filter="url(#softShadow)"/>

  
  <circle cx="150" cy="75" r="95" fill="url(#blobPink)" opacity="0.55"/>
  <circle cx="620" cy="200" r="130" fill="url(#blobBlue)" opacity="0.55"/>

  
  <text x="710" y="50" class="sparkle" font-size="26">✨</text>
  <text x="60" y="240" class="sparkle" font-size="24">✨</text>
  <text x="640" y="90" class="sparkle" font-size="22">⭐</text>

  

  <text x="680" y="230" font-size="26" opacity="0.85">💗</text>

  

<g transform="translate(600, 20) scale(0.9)">
    <image 
        href="{Png}"
        x="0"
        y="0"
        width="80"
        height="80"
    />
</g>

  <text x="48" y="64"
        font-size="28"
        font-weight="700"
        font-family="'Poppins','Segoe UI', system-ui"
        fill="#ff66a8">
     Random Quote 
  </text>

  
  <foreignObject x="48" y="105" width="664" height="150" class="fadeIn">
    <div xmlns="http://www.w3.org/1999/xhtml"
      style="font-family:'Poppins','Segoe UI', system-ui;
             font-size:22px; color:#444; line-height:1.45; word-wrap:break-word;">
      <p style="margin:0; font-weight:500;">{t}</p>
    </div>
  </foreignObject>

</svg>'''

@app.route("/", methods=["GET"])
@app.route("/Fact", methods=["GET"])
def random_fact_root():
    facts = load_facts()
    fact = random.choice(facts)
    svg = make_svg(fact)

    res = Response(svg, mimetype="image/svg+xml")
    res.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    res.headers["Pragma"] = "no-cache"
    res.headers["Expires"] = "0"
    res.headers["ETag"] = str(time.time())

    return res


