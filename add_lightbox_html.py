import glob
import os

trek_files = glob.glob("*-trek.html")
lightbox_html = '''
    <!-- Lightbox Modal -->
    <div id="lightbox-modal" class="lightbox-modal">
        <span class="close-lightbox" onclick="closeLightbox()">&times;</span>
        <img class="lightbox-content" id="lightbox-img">
    </div>
'''

print("Injecting Lightbox HTML into trek pages...")
for filename in trek_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'id="lightbox-modal"' in content:
        print(f"[SKIP] {filename} already has lightbox.")
        continue
        
    # Insert before main.js script tag
    target = '<script src="js/main.js"></script>'
    if target in content:
        new_content = content.replace(target, lightbox_html + '\n    ' + target)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[SUCCESS] Added lightbox to {filename}")
    else:
        print(f"[ERROR] Could not find insertion point in {filename}")
