import glob
import re

def fix_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace space-x with gap in the specific header divs
    content = content.replace('lg:space-x-3 xl:space-x-6', 'lg:gap-3 xl:gap-6')
    content = content.replace('lg:space-x-2 xl:space-x-4', 'lg:gap-2 xl:gap-4')
    content = content.replace('lg:space-x-0 xl:space-x-1', 'lg:gap-0 xl:gap-1')
    content = content.replace('space-x-2', 'gap-2')
    content = content.replace('space-x-4', 'gap-4')
    
    # Replace the languages icon with arrow-left-right for RTL toggle
    # Make sure we only replace it inside the rtl-toggle button
    pattern = re.compile(r'(<button id="rtl-toggle"[^>]*>.*?<i data-lucide=")languages("[^>]*></i>.*?</button>)', re.DOTALL)
    content = pattern.sub(r'\g<1>arrow-left-right\g<2>', content)
    
    pattern_mobile = re.compile(r'(<button id="rtl-toggle-mobile"[^>]*>.*?<i data-lucide=")languages("[^>]*></i>.*?</button>)', re.DOTALL)
    content = pattern_mobile.sub(r'\g<1>arrow-left-right\g<2>', content)

    pattern_sidebar = re.compile(r'(<button id="rtl-toggle-sidebar"[^>]*>.*?<i data-lucide=")languages("[^>]*></i>.*?</button>)', re.DOTALL)
    content = pattern_sidebar.sub(r'\g<1>arrow-left-right\g<2>', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for file_path in glob.glob('*.html'):
    fix_html(file_path)

print('Done')
