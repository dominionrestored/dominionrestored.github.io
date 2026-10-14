# Dominion Restored website

The public website of Kingdom Management Solutions, LLC for Dominion Restored: home, FAQ, support, about and the privacy policy. It holds none of the game's code, so it stays public when the game repository goes private.

Live at **https://dominionrestored.github.io** (GitHub Pages, from `main` / root). For the store listings:
- privacy policy: **https://dominionrestored.github.io/privacy.html**
- support: **https://dominionrestored.github.io/support.html**
- marketing: **https://dominionrestored.github.io/**

- Edit the pages in `build.py`, then run `python3 build.py` here. It rewrites the five `.html` files from one shared header and footer. No packages are needed.
- Styles are in `assets/site.css`; fonts are self-hosted in `assets/fonts` (Atkinson Hyperlegible for all text, and Silkscreen only for the logo and the game's title; both under the SIL Open Font License), so the site loads nothing from other companies.
- Screenshots are in `assets/img`, cropped from the store screenshots.
- Store links and QR codes: see the comment above `stores` in `build.py`.
