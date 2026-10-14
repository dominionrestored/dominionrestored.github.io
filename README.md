# Dominion Restored website

The public website of Kingdom Management Solutions, LLC for Dominion Restored: home, FAQ, support, about and the privacy policy. It holds none of the game's code, so it stays public when the game repository goes private.

Live at **https://aarongranade.github.io/kingdommanagementsolutions/** once GitHub Pages is on (Settings > Pages > Deploy from a branch > `main` / root). The privacy policy for the store listings is **https://aarongranade.github.io/kingdommanagementsolutions/privacy.html**.

- Edit the pages in `build.py`, then run `python3 build.py` here. It rewrites the five `.html` files from one shared header and footer. No packages are needed.
- Styles are in `assets/site.css`; fonts are self-hosted in `assets/fonts` (Silkscreen and Atkinson Hyperlegible, both under the SIL Open Font License), so the site loads nothing from other companies.
- Screenshots are in `assets/img`, cropped from the store screenshots.
- Store links and QR codes: see the comment above `stores` in `build.py`.
