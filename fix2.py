import glob, re, os

project_dir = r'c:\Users\Shalani A\Documents\Shalan\Client projects(MAY)\Freelance Session Replay & Product Analytics Implementer'

for f in glob.glob(os.path.join(project_dir, '*.html')):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Replace RTL icon with align-right
    content = re.sub(
        r'(<button id="rtl-toggle"[^>]*>.*?<i data-lucide=")[^"]+("[^>]*></i>.*?</button>)', 
        r'\g<1>align-right\g<2>', 
        content, 
        flags=re.DOTALL
    )
    
    # 2. Make buttons consistently curved (rounded-full)
    # We replace rounded-lg, rounded-xl, rounded-2xl with rounded-full on button tags and specific a tags
    content = re.sub(r'(<button[^>]*class="[^"]*)rounded-(?:sm|md|lg|xl|2xl|3xl)([^"]*"[^>]*>)', r'\1rounded-full\2', content)
    content = re.sub(r'(<a[^>]*class="[^"]*bg-(?:primary|slate|white)[^"]*)rounded-(?:sm|md|lg|xl|2xl|3xl)([^"]*"[^>]*>)', r'\1rounded-full\2', content)
    
    # For inputs
    content = re.sub(r'(<input[^>]*class="[^"]*)rounded-(?:sm|md|lg|xl|2xl|3xl)([^"]*"[^>]*>)', r'\1rounded-full\2', content)

    # 3. For containers, ensure they are rounded-[2.5rem] or rounded-3xl if they were less rounded
    # Ensure glass-card and other cards are rounded-3xl if they were rounded-2xl or rounded-xl
    content = re.sub(r'(class="[^"]*(?:glass-card|bg-white|bg-slate)[^"]*)rounded-(?:lg|xl|2xl)([^"]*")', r'\1rounded-3xl\2', content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print('Done')
