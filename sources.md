# Sources - Nashville Crosswalks brief, 2026-11-13

Primary source for every figure: Crosswalks (Crosswalks_2_view), Metropolitan Government of Nashville and Davidson County, ArcGIS FeatureServer layer 0, services2.arcgis.com/HdTo6HJqh92wn4D8. Snapshot pulled November 13, 2026; server count 1,823, pulled count 1,823. Layer metadata archived at data/source-metadata-layer.json; pull log at data/pull_log.json.

- Record total, paint counter (G 734, P 683, F 389, NA 16, blank 1), feature counter (L 1,563, T 237, NC 16, blank 7), slope counter (less than or equal to 2 percent 626, 2 percent - 5 percent 1,020, greater than 5 percent 165, blank 12): counts of the pulled records, stats.json; panels at data/paint_panel.csv, data/type_panel.csv, and data/slope_panel.csv.
- Official definitions for FeatureType, PaintCondition, and CrossSlope codes and names: the coded-value domains in the archived layer metadata (data/source-metadata-layer.json). NC and NA appear in no domain in that metadata.
- Poor share (683 of 1,823, 37.5 percent): count of records with PaintCondition P over all pulled records, stats.json.
- Slope shares (626 of 1,811 recorded in the lowest bucket, 34.6 percent; 1,185 of 1,811 above 2 percent, 65.4 percent): counts of recorded CrossSlope values; the above-2-percent total is derived by summing the two upper buckets. Derived where labeled.
- Type splits (Transverse Poor 120 of 237, 50.6 percent; Longitudinal Poor 557 of 1,563, 35.6 percent; slope lowest-bucket shares by type): counts of the pulled records grouped by FeatureType, stats.json and data/type_panel.csv. Derived from the recorded fields.
- Width figures (populated 1,822, blank 1, zero 35, positive 1,787, median positive 10, median overall 10, distribution 23 / 179 / 1,568 / 17): counts and medians of the recorded Width values with the sentinel rule in brief Methods, stats.json and data/width_panel.csv. Width unit: the layer metadata states no unit; reported as recorded.
- Off-codebook control (the 16 NC records are the same 16 records as the 16 NA records, all with Width 0): record-ID set comparison on the pulled records, recorded in data/audit_output.txt and stats.json. Derived.
- Paint by slope cross-tabulation: counts of the pulled records, data/paint_slope_crosstab.csv. Derived.
- AuditDate figures (populated 1,816, blank 7, range March 13, 2023 to December 9, 2023 UTC, all dated audits in 2023): derived from the recorded AuditDate timestamps on the pulled records.
- AssetID figures (populated on all 1,823 records, 1,823 distinct): counts of the pulled records, stats.json.
- Service last-edit date (November 13, 2026): the editingInfo lastEditDate in the archived layer metadata (data/source-metadata-layer.json).
- Companion briefs referenced at prose level only: Machine Readable's Nashville Sidewalks brief (November 10, 2026) and Nashville Curb Ramps brief (November 11, 2026), published figures only; no records were joined.
- Human-scale conversions (about 1 in 3 recorded Poor; about 2 in 3 recorded slopes above the lowest bucket): derived from the headline counts above and labeled derived in the brief.
