import os, glob, re

SVG_LOGO = '''<div class="flex items-center gap-1.5">
    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" fill="#10B981" fill-opacity="0.1" stroke="#10B981" stroke-width="1.5"></path>
        <circle cx="12" cy="10" r="3" fill="#10B981"></circle>
        <path d="M6 19l2-8h8l2 8H6z" fill="#10B981" stroke="#10B981"></path>
    </svg>
    <span class="text-xl md:text-2xl font-bold tracking-tight text-on-surface" style="font-family: 'Inter', sans-serif;">Micro<span style="color: #10B981">Mart</span></span>
</div>'''

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Text Rebranding
    content = content.replace('Pranav Enterprises', 'MicroMart')
    content = content.replace('pranaventerprises', 'micromart')
    content = content.replace('Delivering Quality, Building Trust.', 'Hyperlocal Commerce for Underserved Towns')
    content = content.replace('Your trusted source for professional enterprise solutions and products.', 'Hyperlocal Commerce for Underserved Towns')
    content = content.replace('Professional Solutions', 'Hyperlocal Commerce')
    content = content.replace('YOUR TRUSTED ENTERPRISE', 'YOUR LOCAL NEIGHBORHOOD MARKET')
    
    # 2. Logo Replacement
    # Need to match <img src="/logo.png".../> including line breaks and optional attributes before/after
    content = re.sub(r'<img[^>]*src=[\"\'\']/logo.png[\"\'\'][^>]*>', SVG_LOGO, content)
    
    # 3. Section Renaming (Our Work -> Everyday Essentials)
    content = content.replace('Our Work', 'Everyday Essentials')
    content = content.replace('Discover our portfolio of creative and successful projects.', 'Daily household, hygiene, and personal care products delivered fast.')
    content = content.replace('#workGrid', '#essentialsGrid')
    content = content.replace('id="workGrid"', 'id="essentialsGrid"')
    content = content.replace('loadMoreBtnWork', 'loadMoreBtnEssentials')
    content = content.replace('loadMoreContainerWork', 'loadMoreContainerEssentials')
    content = content.replace('Work Gallery', 'Everyday Essentials')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Processed {filepath}')

html_files = glob.glob('*.html')
js_files = glob.glob('*.js')
for file in html_files + js_files:
    if file not in ['tailwind.config.js', 'postcss.config.js']:
        process_file(file)
