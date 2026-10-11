# shakeout-site

The public pages for Dewline: Running Weather (iPhone): a privacy policy, support, and How this works. Served by GitHub Pages from `main`.

- Pages are written in `_src/` and wrapped in the shared header and footer by `python3 _src/build.py`. Commit the generated `index.html` files too; Pages serves them as they are (Jekyll skips `_src/`).
- Colours are Field's page tokens and condition-word fills (`design/field-v7.1/tokens.json` in the app repo); the page follows the system appearance.
- Fonts: Funnel Display and Funnel Sans, SIL OFL 1.1 (`fonts/`), served from the site so visitors make no third-party requests.
- The app links to `/privacy/`; keep that path.
