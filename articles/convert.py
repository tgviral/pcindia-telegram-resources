import re, os

def md_to_html(content, title):
    html = f"""<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{title} - भारत के Telegram Channels 2026 Hindi SEO Article">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://tgviral.github.io/pcindia-telegram-resources/">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif; background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); min-height: 100vh; color: #e0e0e0; line-height: 1.7; }}
        .header {{ background: rgba(38,165,228,0.1); border-bottom: 1px solid rgba(255,255,255,0.08); padding: 20px 0; text-align: center; }}
        .header a {{ color: #26a5e4; text-decoration: none; font-size: 14px; }}
        .header a:hover {{ text-decoration: underline; }}
        .header h1 {{ color: #fff; font-size: clamp(18px, 4vw, 28px); margin: 10px 20px; font-weight: 800; }}
        .breadcrumb {{ color: #888; font-size: 12px; margin-top: 8px; }}
        .breadcrumb a {{ color: #26a5e4; text-decoration: none; }}
        .container {{ max-width: 900px; margin: 0 auto; padding: 40px 20px; }}
        .article-meta {{ display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; margin-bottom: 30px; }}
        .meta-badge {{ padding: 5px 14px; border-radius: 20px; font-size: 12px; background: rgba(255,255,255,0.08); color: #aaa; border: 1px solid rgba(255,255,255,0.1); }}
        h2 {{ font-size: 22px; color: #26a5e4; margin: 40px 0 20px; padding-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.08); }}
        h3 {{ font-size: 18px; color: #fff; margin: 30px 0 14px; }}
        p {{ margin-bottom: 16px; color: #ccc; font-size: 15px; }}
        ul, ol {{ margin: 0 0 16px 24px; color: #ccc; }}
        li {{ margin-bottom: 8px; font-size: 15px; }}
        a {{ color: #26a5e4; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        blockquote {{ background: rgba(38,165,228,0.08); border-left: 4px solid #26a5e4; padding: 16px 20px; margin: 20px 0; border-radius: 0 8px 8px 0; color: #bbb; font-size: 15px; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 14px; }}
        th {{ background: rgba(38,165,228,0.15); color: #26a5e4; padding: 12px; text-align: left; font-weight: 600; border-bottom: 2px solid rgba(38,165,228,0.3); }}
        td {{ padding: 10px 12px; border-bottom: 1px solid rgba(255,255,255,0.06); color: #ccc; }}
        tr:hover td {{ background: rgba(255,255,255,0.03); }}
        hr {{ border: none; border-top: 1px solid rgba(255,255,255,0.08); margin: 30px 0; }}
        .toc {{ background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px; margin-bottom: 30px; }}
        .toc h2 {{ margin-top: 0; border-bottom: none; color: #fff; font-size: 16px; }}
        .toc ul {{ list-style: none; margin: 0; padding: 0; }}
        .toc li {{ margin-bottom: 8px; padding-left: 12px; }}
        .toc a {{ color: #26a5e4; font-size: 14px; }}
        .disclaimer {{ background: rgba(255,107,107,0.08); border: 1px solid rgba(255,107,107,0.2); border-radius: 12px; padding: 20px; margin-top: 40px; color: #ccc; font-size: 14px; }}
        .disclaimer h2 {{ color: #ff6b6b; margin-top: 0; font-size: 16px; border-bottom: none; }}
        .nav-cards {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 16px; margin: 30px 0; }}
        .nav-card {{ background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 20px; text-decoration: none; color: inherit; display: block; transition: all 0.3s; }}
        .nav-card:hover {{ background: rgba(255,255,255,0.09); border-color: rgba(38,165,228,0.4); transform: translateY(-2px); }}
        .nav-card h4 {{ color: #fff; font-size: 14px; margin-bottom: 6px; }}
        .nav-card p {{ color: #888; font-size: 12px; margin: 0; }}
        .footer {{ text-align: center; padding: 40px 20px; border-top: 1px solid rgba(255,255,255,0.06); color: #666; font-size: 13px; }}
        .footer a {{ color: #26a5e4; text-decoration: none; }}
        .footer a:hover {{ text-decoration: underline; }}
        strong {{ color: #fff; }}
        em {{ color: #b0b0b0; }}
        @media (max-width: 600px) {{ table {{ font-size: 12px; }} td, th {{ padding: 8px 6px; }} }}
    </style>
</head>
<body>
"""

    lines = content.split('\n')
    in_table = False
    table_rows = []
    in_list = False
    html_body = []

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        # Table detection
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_rows = []
            row_cells = [c.strip() for c in line.split('|')[1:-1]]
            # Check if separator row
            if all(re.match(r'^[\s\-:]+$', c) for c in row_cells):
                in_table = False
                html_body.append('<table><thead>')
                html_body.append('<tr>' + ''.join(f'<th>{c}</th>' for c in table_rows[0]) + '</tr>')
                html_body.append('</thead><tbody>')
                for row in table_rows[1:]:
                    html_body.append('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>')
                html_body.append('</tbody></table>')
                table_rows = []
                i += 1
                continue
            table_rows.append(row_cells)
            i += 1
            continue
        elif in_table:
            in_table = False
            html_body.append('<table><thead>')
            html_body.append('<tr>' + ''.join(f'<th>{c}</th>' for c in table_rows[0]) + '</tr>')
            html_body.append('</thead><tbody>')
            for row in table_rows[1:]:
                html_body.append('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>')
            html_body.append('</tbody></table>')
            table_rows = []

        # Headers
        if line.startswith('### '):
            html_body.append(f'<h3>{inline_format(line[4:])}</h3>')
        elif line.startswith('## '):
            html_body.append(f'<h2>{inline_format(line[3:])}</h2>')
        elif line.startswith('# '):
            pass  # Title already in head
        # hr
        elif re.match(r'^-{3,}$', line.strip()) or re.match(r'^\*{3,}$', line.strip()):
            html_body.append('<hr>')
        # Blockquote
        elif line.startswith('> '):
            html_body.append(f'<blockquote>{inline_format(line[2:])}</blockquote>')
        # List items
        elif line.startswith('- '):
            if not in_list:
                html_body.append('<ul>')
                in_list = True
            html_body.append(f'<li>{inline_format(line[2:])}</li>')
        elif re.match(r'^\d+\. ', line):
            if not in_list:
                html_body.append('<ul>')
                in_list = True
            html_body.append(f'<li>{inline_format(re.sub(r"^\d+\. ", "", line))}</li>')
        else:
            if in_list:
                html_body.append('</ul>')
                in_list = False
            if line.strip():
                html_body.append(f'<p>{inline_format(line)}</p>')

        i += 1

    if in_list:
        html_body.append('</ul>')
    if in_table and table_rows:
        html_body.append('<table><thead>')
        html_body.append('<tr>' + ''.join(f'<th>{c}</th>' for c in table_rows[0]) + '</tr>')
        html_body.append('</thead><tbody>')
        for row in table_rows[1:]:
            html_body.append('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>')
        html_body.append('</tbody></table>')

    html += '\n'.join(html_body)

    # Navigation cards
    html += """
    <div class="container">
        <h2 style="margin-top:50px;">📚 More Articles / अन्य लेख</h2>
        <div class="nav-cards">
            <a href="index.html" class="nav-card">
                <h4>🏆 सभी चैनल - Complete List</h4>
                <p>9,500+ भारतीय Telegram चैनल</p>
            </a>
            <a href="india-ssc-bank-railway-upsc-telegram-channels-2026-hindi.html" class="nav-card">
                <h4>📚 शिक्षा - Education</h4>
                <p>SSC, Bank, Railway, UPSC</p>
            </a>
            <a href="india-crypto-trading-telegram-channels-2026-hindi.html" class="nav-card">
                <h4>💰 क्रिप्टो - Crypto</h4>
                <p>Airdrop, Trading Signals</p>
            </a>
            <a href="india-movies-webseries-telegram-channels-2026-hindi.html" class="nav-card">
                <h4>🎬 मूवी - Movies</h4>
                <p>Bollywood, Hollywood, Web Series</p>
            </a>
            <a href="india-shopping-deals-telegram-channels-2026-hindi.html" class="nav-card">
                <h4>🛒 डील्स - Deals</h4>
                <p>Flipkart, Amazon Discounts</p>
            </a>
            <a href="india-cricket-gaming-telegram-channels-2026-hindi.html" class="nav-card">
                <h4>🏏 क्रिकेट - Cricket</h4>
                <p>Cricket, Gaming, Rummy</p>
            </a>
        </div>
    </div>
    """

    html += """
    <footer class="footer">
        <p>
            🇮🇳 <a href="https://tgviral.com" target="_blank">tgviral.com</a>
            &nbsp;|&nbsp; <a href="https://letstg.com" target="_blank">letstg.com</a>
            &nbsp;|&nbsp; <a href="https://github.com/tgviral/pcindia-telegram-resources" target="_blank">GitHub</a>
        </p>
        <p style="margin-top:10px;">Last Updated: April 2026 | 9,500+ Channels | 🇮🇳 Hindi</p>
    </footer>
</body>
</html>"""
    return html

def inline_format(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2" target="_blank">\1</a>', text)
    text = re.sub(r'^### (.+)$', r'\1', text)
    return text

articles = [
    ('india-top-10000-telegram-channels-list-2026-hindi.md',
     'india-top-10000-telegram-channels-list-2026-hindi.html',
     'भारत के 10000+ सर्वश्रेष्ठ Telegram चैनल 2026'),
    ('india-ssc-bank-railway-upsc-telegram-channels-2026-hindi.md',
     'india-ssc-bank-railway-upsc-telegram-channels-2026-hindi.html',
     'SSC, Bank, Railway, UPSC Telegram चैनल 2026'),
    ('india-crypto-trading-telegram-channels-2026-hindi.md',
     'india-crypto-trading-telegram-channels-2026-hindi.html',
     'क्रिप्टोकरेंसी और Trading Telegram चैनल 2026'),
    ('india-movies-webseries-telegram-channels-2026-hindi.md',
     'india-movies-webseries-telegram-channels-2026-hindi.html',
     'मूवी और Web Series Telegram चैनल 2026'),
    ('india-shopping-deals-telegram-channels-2026-hindi.md',
     'india-shopping-deals-telegram-channels-2026-hindi.html',
     'Shopping Deals और Coupons Telegram चैनल 2026'),
    ('india-cricket-gaming-telegram-channels-2026-hindi.md',
     'india-cricket-gaming-telegram-channels-2026-hindi.html',
     'Cricket, Gaming और Rummy Telegram चैनल 2026'),
]

base_dir = r'c:\Users\1\Desktop\项目测试\pcindia\articles'

for md_file, html_file, title in articles:
    md_path = os.path.join(base_dir, md_file)
    html_path = os.path.join(base_dir, html_file)
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    html = md_to_html(content, title)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Converted: {html_file}')

print('All done!')
