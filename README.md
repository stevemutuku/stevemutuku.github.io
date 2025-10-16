# Content-driven site (updates via content.json)

**Stop losing info in chats.** Put your bio, projects, and books in `content.json`.  
On every change, GitHub Actions runs `build.py` to regenerate `index.html` and commit it.

## Setup
1. Upload to your repo root:
   - content.json
   - base.html
   - build.py
   - styles.css
   - script.js
2. Create folder `.github/workflows/` and add `update-site.yml` inside.
3. Ensure Pages deploys from the `main` branch, folder `/`.
4. (Optional) Add `.nojekyll` empty file.

## Update
- Edit `content.json` (bio, projects, books, links).
- Commit to `main` → Action builds site → Pages publishes.

You can also customize layout in `base.html` and styles in `styles.css`.
