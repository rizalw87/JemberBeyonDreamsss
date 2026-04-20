import os
import re

dir_path = r"c:\Magang\tugas akhir\jember"

for file in os.listdir(dir_path):
    if file.endswith('.html'):
        filepath = os.path.join(dir_path, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract title
        m_title = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        old_title = m_title.group(1).strip() if m_title else "Jember Beyond Dreams - Portal Informasi & Wisata"
        
        # Update title replacing Jember Dream with Jember Beyond Dreams
        new_title = old_title.replace("Jember Dream", "Jember Beyond Dreams")
        if "Jember Beyond Dreams" not in new_title:
            new_title = new_title + " | Jember Beyond Dreams"

        # Extract description
        m_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>', content, re.IGNORECASE | re.DOTALL)
        desc = m_desc.group(1).strip() if m_desc else "Portal informasi terpercaya mengenai potensi daerah, panduan wisata, pendidikan, dan berita terkini di Kabupaten Jember."

        # Make description cleaner
        desc = desc.replace('"', '&quot;')

        # Extract author
        author = "Jember Beyond Dreams"
        
        # Build new head
        new_head = f"""<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{new_title}</title>

    <!-- SEO & Meta Tags -->
    <meta name="description" content="{desc}">
    <meta name="keywords" content="Jember, Wisata Jember, wisata alam jember, Pantai Papuma, Berita Jember, Ekonomi Jember, Pendidikan Jember, Jember Beyond Dreams">
    <meta name="author" content="{author}">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    
    <!-- AI Overview (AEO & GEO) & Schema.org JSON-LD -->
    <meta name="revisit-after" content="1 days">
    <meta name="language" content="Indonesian">
    <meta name="geo.region" content="ID-JI">
    <meta name="geo.placename" content="Jember">
    <meta name="geo.position" content="-8.1721;113.7000">
    <meta name="ICBM" content="-8.1721, 113.7000">

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Jember Beyond Dreams",
      "url": "https://jemberdream.com/",
      "description": "Portal informasi terpercaya Kabupaten Jember. Temukan destinasi wisata unggulan, tips traveling, serta update berita lokal.",
      "publisher": {{
        "@type": "Organization",
        "name": "Jember Beyond Dreams",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://jemberdream.com/images/apple-touch-icon.png"
        }}
      }}
    }}
    </script>

    <!-- OpenGraph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://jemberdream.com/{file}">
    <meta property="og:site_name" content="Jember Beyond Dreams">
    <meta property="og:title" content="{new_title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:image" content="https://jemberdream.com/images/jember-hero.webp">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="Hero Image Jember Beyond Dreams">
    <meta property="og:locale" content="id_ID">

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="https://jemberdream.com/{file}">
    <meta name="twitter:title" content="{new_title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="https://jemberdream.com/images/jember-hero.webp">

    <link rel="canonical" href="https://jemberdream.com/{file}">

    <!-- Favicon Optimization -->
    <link rel="icon" type="image/x-icon" href="favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="images/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="images/apple-touch-icon.png">
    <meta name="theme-color" content="#78852B">

    <!-- Page Speed Optimization (Preconnect, Preload, Defer) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="dns-prefetch" href="https://fonts.googleapis.com">
    
    <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Poppins:wght@300;400;500;600&display=swap">
    <link rel="preload" as="style" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="preload" as="style" href="style.css">
    
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Outlined" rel="stylesheet" media="print" onload="this.media='all'">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" media="print" onload="this.media='all'">
    <link rel="stylesheet" href="style.css">
    
    <!-- Noscript fallback for deferred CSS -->
    <noscript>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Outlined" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </noscript>
</head>"""

        # Replace old head
        content = re.sub(r'<head>.*?</head>', new_head, content, flags=re.IGNORECASE | re.DOTALL)
        
        # Ensure defer on bootstrap JS and other non-essential JS
        content = re.sub(
            r'<script\s+src="https://cdn\.jsdelivr\.net/npm/bootstrap@5\.3\.0/dist/js/bootstrap\.bundle\.min\.js"\s*(defer)?>\s*</script>',
            r'<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" defer></script>',
            content
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Finished optimizing headers!")
