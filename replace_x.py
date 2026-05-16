import glob
import re

def fix_x_icon(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The twitter svg path
    twitter_path = '<path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"></path>'
    
    # The new X svg path
    x_path = '<path d="M4 4l11.733 16h4.267l-11.733 -16z"></path><path d="M4 20l6.768 -6.768m2.46 -2.46l6.772 -6.772"></path>'

    content = content.replace(twitter_path, x_path)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for file_path in glob.glob('*.html'):
    fix_x_icon(file_path)

print('Done')
