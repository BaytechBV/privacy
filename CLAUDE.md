# BaytechBV/privacy

- Site base is `https://apps.baytech.nl/` (`landing.BASE`). Never write `baytechbv.github.io/privacy` in a page: not in canonical, og:url/og:image, nor the "Privacy:" link copied from App Store description text.
- Before every commit/PR that adds or edits pages, run and fix until it exits 0 (same check as the `seo` workflow):
  `python3 -c "import seo, sys; sys.exit(1 if seo.audit('/tmp/DENETIM.md') else 0)"; cat /tmp/DENETIM.md`
- Don't merge a PR whose `seo` check is red: a red main makes every later PR red too.
