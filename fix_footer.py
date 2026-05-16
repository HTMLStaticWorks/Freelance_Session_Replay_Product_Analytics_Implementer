import glob
import re

twitter_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-5 h-5 text-slate-700 dark:text-slate-200 group-hover:text-white transition-colors"><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"></path></svg>'''

linkedin_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-5 h-5 text-slate-700 dark:text-slate-200 group-hover:text-white transition-colors"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect width="4" height="12" x="2" y="9"></rect><circle cx="4" cy="4" r="2"></circle></svg>'''

github_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-5 h-5 text-slate-700 dark:text-slate-200 group-hover:text-white transition-colors"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"></path><path d="M9 18c-4.51 2-5-2-7-2"></path></svg>'''

def fix_footer(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change year
    content = content.replace('2024 InsightAnalytics', '2026 InsightAnalytics')
    
    # Replace lucide tags
    content = re.sub(r'<i data-lucide="twitter"[^>]*></i>', twitter_svg, content)
    content = re.sub(r'<i data-lucide="linkedin"[^>]*></i>', linkedin_svg, content)
    content = re.sub(r'<i data-lucide="github"[^>]*></i>', github_svg, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for file_path in glob.glob('*.html'):
    fix_footer(file_path)

print('Done')
