import os
from datetime import datetime

dir_path = r"c:\Magang\tugas akhir\jember"

urls = []
date_str = datetime.now().strftime("%Y-%m-%d")

for file in os.listdir(dir_path):
    if file.endswith('.html'):
        priority = "0.64"
        if file == "index.html":
            priority = "1.00"
        elif file in ["blog.html", "destinations.html", "profile.html", "contact.html"]:
            priority = "0.80"

        urls.append(f"""  <url>
    <loc>https://jemberdream.com/{file}</loc>
    <lastmod>{date_str}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>""")

sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset
      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
{chr(10).join(urls)}
</urlset>"""

with open(os.path.join(dir_path, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_content)

robots_content = """User-agent: *
Allow: /

Sitemap: https://jemberdream.com/sitemap.xml
"""

with open(os.path.join(dir_path, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_content)

print("Generated sitemap.xml and robots.txt")
