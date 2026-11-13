# Nashville Crosswalks - Machine Readable brief, 2026-11-13

Of the 1,823 records in Nashville's Crosswalks layer, 683 (37.5 percent) are recorded with Poor paint, and of the 1,811 records with a recorded cross slope, 626 (34.6 percent) sit in the lowest bucket (less than or equal to 2 percent) while 1,185 (65.4 percent, derived) sit in buckets above 2 percent. All dated audits in the layer fall in 2023, and the layer as published carries no street, district, or neighborhood field.

Full brief: brief-draft.md. Headline graphic: hero.png.

## Contents
- brief-draft.md - the brief
- stats.json - every headline figure with its population printed
- charts/ - paint condition, cross slope buckets, Poor share by type, width distribution, paint by slope
- data/ - panels, the raw snapshot CSV, the pre-flight audit output, the pull log, the source layer metadata, and the independent verifier output
- code/ - pull_data.py, audit_section10.py, build_stats.py, verify_independent.py, charts.py, hero_composite.py
- verification.md - pre-flight audit, methods checklist, sync gate, story gate
- sources.md, reviewer-notes.md, social-drafts.md

## Reproduce
```
python3 code/pull_data.py
python3 code/audit_section10.py
python3 code/build_stats.py
python3 code/verify_independent.py
python3 code/charts.py
python3 code/hero_composite.py
```
Dependencies (matching the code's actual imports): Python 3 standard library plus pandas (verifier only), matplotlib and numpy (charts only), and Pillow (hero composite only). The pull, audit, and build scripts use only the standard library.

## Source
Crosswalks (Crosswalks_2_view), Metropolitan Government of Nashville and Davidson County, ArcGIS FeatureServer layer 0 (services2.arcgis.com/HdTo6HJqh92wn4D8). Snapshot November 13, 2026; audit dates in the layer are in 2023.

## License
Brief text and derived data products: CC BY 4.0 (see LICENSE). Underlying records are Metro Nashville government open data.

Part of Machine Readable: https://adowlen.github.io/machine-readable/
