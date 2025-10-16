import json, pathlib

def card_project(p):
    bits = []
    if p.get("scope"): bits.append(p["scope"])
    if p.get("role"): bits.append(f"Role: {p['role']}")
    if p.get("impact"): bits.append(p["impact"])
    return f'''<article class="card">
  <h3>{p.get("title","")}</h3>
  <p>{' '.join(bits)}</p>
</article>'''

def card_book(b):
    return f'''<article class="card book">
  <h3>{b.get("title","")}</h3>
  <p>{b.get("blurb","")}</p>
  <a target="_blank" rel="noopener" href="{b.get("amazon","#")}" class="btn small">Amazon</a>
</article>'''

def build():
    data = json.loads(pathlib.Path("content.json").read_text(encoding="utf-8"))
    tpl = pathlib.Path("base.html").read_text(encoding="utf-8")
    projects_html = "\\n".join(card_project(p) for p in data.get("projects", []))
    books_html = "\\n".join(card_book(b) for b in data.get("books", []))
    out = (tpl
           .replace("{{SITE_TITLE}}", data.get("site_title","Steve Mutuku"))
           .replace("{{BIO}}", data.get("bio",""))
           .replace("{{PROJECTS_CARDS}}", projects_html)
           .replace("{{BOOKS_CARDS}}", books_html)
           .replace("{{EMAIL}}", data.get("email",""))
           .replace("{{LINKEDIN}}", data.get("linkedin",""))
           .replace("{{GITHUB}}", data.get("github",""))
           )
    pathlib.Path("index.html").write_text(out, encoding="utf-8")
    print("Built index.html")

if __name__ == "__main__":
    build()
