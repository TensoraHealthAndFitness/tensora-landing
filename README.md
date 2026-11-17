# Tensora landing page

The marketing site for **Tensora**, the training app by Tensora: plan your week, log every set and see every muscle you train.

## Layout

| Path | What it is |
|---|---|
| `site/` | The deployable static site: `index.html`, `privacy.html`, `terms.html`, `404.html`, `brand/` (logo, icons) and `media/` (app clips and stills). |
| `site/media/` | Light and dark phone clips (`<name>.mp4/.webm/.jpg` and `<name>-dark.*`) cut from screen recordings of the app. `manifest.json` records each clip's source, time range and content. |
| `site-src/` | `landing_template.html` (styles, layout, scripts) and `build_landing.py`, which fills in the feature chapters, FAQ and clip lists and writes `site/index.html`. |

## Build

Edit `site-src/landing_template.html` or the copy in `site-src/build_landing.py`, then:

```bash
python3 site-src/build_landing.py
```

When clips are re-cut under the same file names, bump `LIGHT_V` (in `build_landing.py`) or `DARK_V` (in `landing_template.html`) so browsers fetch the new files.

## Preview

```bash
cd site && python3 -m http.server 8773
```

Then open http://127.0.0.1:8773/.

## Deploy (Cloudflare Pages)

The `tensora-page` Pages project is connected to `TensoraHealthAndFitness/tensora-landing` on GitHub. It publishes the committed `site/` directory from `main` after each push. The Pages build output directory is `site` and no build command is configured, so run the build locally and commit `site/index.html` whenever the template or feature copy changes.

For a manual redeploy of the current `site/` directory:

```bash
npx wrangler pages deploy site --project-name tensora-page --branch main
```

## Before launch

- Set `SIGNUP_ENDPOINT` in `site-src/landing_template.html` so the early access form stores addresses (it only validates today).
- Replace the `{{privacy policy}}` and `{{terms of use}}` placeholders in `site/privacy.html` and `site/terms.html`.
