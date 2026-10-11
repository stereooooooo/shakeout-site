# Wraps each page body in the shared header and footer. Run: python3 _src/build.py
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
pages = {
    "index.html": ("Dewline: Running Weather", "", None),
    "how-it-works/index.html": ("How this works · Dewline", "../", "how"),
    "privacy/index.html": ("Privacy policy · Dewline", "../", "privacy"),
    "support/index.html": ("Support · Dewline", "../", "support"),
}
nav = [("how", "how-it-works/", "How this works"), ("privacy", "privacy/", "Privacy"), ("support", "support/", "Support")]
for path, (title, up, current) in pages.items():
    body = (root / "_src" / ("index.html" if path == "index.html" else path.replace("/index.html", ".html"))).read_text()
    links = "\n".join(
        f'      <a href="{up}{href}"' + (' aria-current="page"' if key == current else "") + f">{label}</a>"
        for key, href, label in nav
    )
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="Dewline is an iPhone weather app for runners: a full forecast, with what heat and dew point will do to your paces.">
  <meta name="color-scheme" content="light dark">
  <link rel="icon" href="{up}icon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{up}style.css">
</head>
<body>
<div class="page">
  <header class="site">
    <a class="brand" href="{up or './'}"><img src="{up}icon.svg" alt="">Dewline</a>
    <nav class="site" aria-label="Site">
{links}
    </nav>
  </header>
  <main>
{body.rstrip()}
  </main>
  <footer class="site">
    <p>Dewline: Running Weather, for iPhone. Weather data from Apple Weather.</p>
    <p><a href="{up}privacy/">Privacy policy</a> · <a href="{up}support/">Support</a></p>
  </footer>
</div>
</body>
</html>
"""
    out = root / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print("wrote", path)
