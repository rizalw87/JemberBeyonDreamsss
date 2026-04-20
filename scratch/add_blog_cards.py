import os
import re

html_file = r"c:\Magang\tugas akhir\jember\blog.html"

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Generate new cards
# Economy
new_cards = []
for i in range(2, 8):
    card = f"""
                <div class="col-md-4 blog-card-container" data-category="ekonomi">
                    <article class="blog-card">
                        <div style="height:200px;background:linear-gradient(135deg,#ECE4D3,#ddd4bb);display:flex;align-items:center;justify-content:center;border-radius:12px 12px 0 0;">
                            <span class="material-icons-outlined" style="font-size:3rem;color:#78852B;">trending_up</span>
                        </div>
                        <div class="blog-content">
                            <div class="blog-meta">
                                <span class="blog-category" style="background:rgba(120,133,43,.10);color:#78852B;">Ekonomi</span>
                                <span>•</span><span>20 April 2026</span>
                            </div>
                            <h3 class="blog-title"><a href="economy-{i}.html">Perkembangan Ekonomi UMKM Jember Bagian {i}</a></h3>
                            <p class="blog-excerpt">Artikel mendalam tentang pemberdayaan dan perkembangan sektor ekonomi dan UMKM di Jember.</p>
                            <a href="economy-{i}.html" class="text-decoration-none fw-semibold d-inline-flex align-items-center" style="color: var(--c-olive);">Baca Selengkapnya <span class="material-icons-outlined ms-1" style="font-size:1rem;">arrow_forward</span></a>
                        </div>
                    </article>
                </div>"""
    new_cards.append(card)

# Study
for i in range(2, 8):
    card = f"""
                <div class="col-md-4 blog-card-container" data-category="pendidikan">
                    <article class="blog-card">
                        <div style="height:200px;background:linear-gradient(135deg,#ECE4D3,#ddd4bb);display:flex;align-items:center;justify-content:center;border-radius:12px 12px 0 0;">
                            <span class="material-icons-outlined" style="font-size:3rem;color:#78852B;">school</span>
                        </div>
                        <div class="blog-content">
                            <div class="blog-meta">
                                <span class="blog-category" style="background:rgba(120,133,43,.10);color:#78852B;">Pendidikan</span>
                                <span>•</span><span>20 April 2026</span>
                            </div>
                            <h3 class="blog-title"><a href="study-{i}.html">Inovasi Pendidikan di Kabupaten Jember Bagian {i}</a></h3>
                            <p class="blog-excerpt">Membahas inovasi, fasilitas, dan tantangan di sektor pendidikan tingkat dasar hingga perguruan tinggi.</p>
                            <a href="study-{i}.html" class="text-decoration-none fw-semibold d-inline-flex align-items-center" style="color: var(--c-olive);">Baca Selengkapnya <span class="material-icons-outlined ms-1" style="font-size:1rem;">arrow_forward</span></a>
                        </div>
                    </article>
                </div>"""
    new_cards.append(card)

# Tour
for i in range(2, 8):
    card = f"""
                <div class="col-md-4 blog-card-container" data-category="pariwisata">
                    <article class="blog-card">
                        <div style="height:200px;background:linear-gradient(135deg,#ECE4D3,#ddd4bb);display:flex;align-items:center;justify-content:center;border-radius:12px 12px 0 0;">
                            <span class="material-icons-outlined" style="font-size:3rem;color:#78852B;">tour</span>
                        </div>
                        <div class="blog-content">
                            <div class="blog-meta">
                                <span class="blog-category" style="background:rgba(120,133,43,.10);color:#78852B;">Pariwisata</span>
                                <span>•</span><span>20 April 2026</span>
                            </div>
                            <h3 class="blog-title"><a href="tour-{i}.html">Destinasi Wisata Tersembunyi Jember Bagian {i}</a></h3>
                            <p class="blog-excerpt">Eksplorasi destinasi wisata alam, pantai, dan pegunungan memukau yang ada di Kabupaten Jember.</p>
                            <a href="tour-{i}.html" class="text-decoration-none fw-semibold d-inline-flex align-items-center" style="color: var(--c-olive);">Baca Selengkapnya <span class="material-icons-outlined ms-1" style="font-size:1rem;">arrow_forward</span></a>
                        </div>
                    </article>
                </div>"""
    new_cards.append(card)

new_cards_html = "\n".join(new_cards)
insertion_point = 'id="blogContainer">'

content = content.replace(insertion_point, insertion_point + "\n" + new_cards_html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated blog.html")
