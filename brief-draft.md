# Nashville crosswalks: 683 of 1,823 audited records are Poor paint, and the published layer carries no street or district field

**One-line summary:** Of the 1,823 records in Nashville's Crosswalks layer pulled on November 13, 2026, 683 (37.5 percent) are recorded with Poor paint, and of the 1,811 records with a recorded cross slope, 626 (34.6 percent) sit in the lowest bucket (less than or equal to 2 percent) while 1,185 (65.4 percent, derived) sit in buckets above 2 percent; all dated audits in the layer are from 2023, and the layer as published carries no street, district, or neighborhood field.

Start with the scale. Machine Readable pulled the full layer from Metro's ArcGIS service on November 13, 2026; the pulled row count matches the server's own count exactly (1,823). One row is one audited crosswalk record. The layer is the published view of a field audit: every dated AuditDate in the layer falls in 2023 (March 13 to December 9, 2023), so the figures below describe the audit snapshot as recorded in 2023, not conditions on the pull date, and no trend over time can be printed from this layer. No exposure denominator exists in the layer - there is no traffic volume, pedestrian count, street-mile, or crossing-use field - so this brief reports counts and shares of audited records, and makes no claim about how the audited set compares with all crosswalks in Nashville or about risk at any crossing.

## Paint condition

Paint condition is recorded against the layer metadata's coded domain: P is Poor, F is Fair, G is Good.

- Good: 734 records (40.3 percent of 1,823).
- Poor: 683 records (37.5 percent).
- Fair: 389 records (21.3 percent).
- NA: 16 records (0.9 percent). NA does not appear in the metadata domain for this field; see the off-codebook records section below.
- Blank: 1 record.

Human scale (derived): about 1 in 3 audited crosswalks is recorded Poor.

## Recorded cross slope

Cross slope is recorded in three buckets defined in the layer metadata: less than or equal to 2 percent, between 2 percent and 5 percent, and greater than 5 percent. Cross slope is recorded on 1,811 of 1,823 records and blank on 12.

- Less than or equal to 2 percent: 626 records (34.6 percent of the 1,811 recorded).
- Between 2 percent and 5 percent: 1,020 records (56.3 percent of recorded).
- Greater than 5 percent: 165 records (9.1 percent of recorded).
- In buckets above 2 percent combined: 1,185 records (65.4 percent of recorded, derived).

Human scale (derived): about 2 in 3 recorded cross slopes sit above the data's lowest bucket. The 2 percent boundary is the lowest category the layer itself defines. The layer metadata names the buckets and states no compliance standard, so this brief reports the buckets as recorded and prints no compliance or noncompliance figure.

## By crosswalk type

Feature type is recorded against the metadata domain: L is Longitudinal, T is Transverse.

- Longitudinal: 1,563 records (85.7 percent). Of these, 557 are recorded Poor (35.6 percent of longitudinal records, count printed). Cross slope is recorded on 1,553 longitudinal records, of which 516 are in the lowest bucket (33.2 percent of recorded).
- Transverse: 237 records (13.0 percent). Of these, 120 are recorded Poor (50.6 percent of transverse records, count printed). Cross slope is recorded on 235 transverse records, of which 96 are in the lowest bucket (40.9 percent of recorded).
- NC: 16 records (0.9 percent), and blank on 7 records. NC does not appear in the metadata domain for this field; see below.

The transverse group holds 237 records, above the small-count threshold in the methods checklist, and every percentage above is printed with its underlying count.

## Width, as recorded

Width is an integer field. The layer metadata states no unit for it, so width values in this brief are reported as recorded, unit not stated in the layer metadata.

- Width is populated on 1,822 records and blank on 1.
- Width 0 occurs on 35 records. A crosswalk in the audit cannot be read as zero-width from this field alone, so this brief treats Width 0 as unknown: it is excluded from the width medians and the distribution below, and it is counted and reported here and in the audit. The 35 records are the 16 off-codebook records described below plus 19 other records (18 recorded Poor and 1 recorded Fair).
- On the 1,787 records with a positive width, the median width is 10. The median across all 1,822 populated records, zeros included, is also 10.
- Distribution on positive widths: under 6 on 23 records, 6 to under 10 on 179, 10 to under 15 on 1,568, and 15 or above on 17.

## The off-codebook records (the built-in control)

16 records carry FeatureType NC and PaintCondition NA. Neither NC nor NA appears in the metadata coded-value domains for its field. The 16 NC records are exactly the 16 NA records (same records, verified by record ID), and all 16 carry Width 0. This brief reports them as a distinct subpopulation throughout and never merges them into the coded categories. Their pattern is the brief's built-in control: a separate group of records, coded outside the published domains and carrying the sentinel width, behaves as its own population in every field checked, which is the evidence that the Width 0 and off-codebook values are a property of how those records were entered, not random scattered entries.

## Paint by slope

The cross-tabulation of the two recorded condition fields is in data/paint_slope_crosstab.csv. Of the records in each paint group with a recorded slope, the share in the lowest slope bucket is similar across groups: Poor records record 238 of 677 in the lowest bucket, Fair records 129 of 387, and Good records 246 of 730. The brief prints the panel counts and draws no pattern claim from them beyond that similarity, because no exposure or location field exists to normalize the comparison.

## What the layer cannot place

The view carries no street, district, or neighborhood field. Its fields are OBJECTID, Inspector, AuditDate, FeatureType, Width, CrossSlope, PaintCondition, GlobalID, AssetID, and editor tracking fields. AssetID is populated on all 1,823 records and all 1,823 values are distinct, so each record is individually identifiable by its asset identifier, but the layer as published gives no field from which a finding can be assigned to a street, a council district, or a neighborhood. The layer as published also carries no geometry in this pull (the pull requested attributes only), so no map is printed. Two companion Machine Readable briefs in this series - Sidewalks (November 10, 2026) and Curb Ramps (November 11, 2026) - were built from their own layers with their own published figures; this brief makes no joined claim across the three layers, because the crosswalks view carries no shared geography field to join on. The comparison is prose-level only and is recorded in the verification file.

## What this might mean

One possible reading is that the 2023 audit, as published, records condition findings (Poor paint on more than a third of records, most recorded slopes above the lowest bucket) that cannot be assigned to places from the published layer, so a reader who wants to know which streets or neighborhoods the findings concern cannot answer that from this layer alone. The strongest alternative explanation is that location is held in a companion asset system keyed by AssetID and was not included in this public view by design, in which case the findings are placeable inside Metro's systems and only the public view lacks the field. On the data as published, the placeability finding is about the public layer, and any use that needs findings by street or district needs a field or a join key this view does not carry.

## Who can act

- **NDOT (Nashville Department of Transportation and Multimodal Infrastructure), as the layer publisher:** publish a street, district, or neighborhood field on the crosswalks view, or publish a note in the layer metadata stating which companion source, keyed by AssetID, carries location for these records. Cost class: low-cost operational change (metadata and export configuration, no new collection implied by this brief). Outcome measure: the presence of a location field, or the metadata note, on the next pull of this layer, against the November 13, 2026 baseline of no such field among the view's 13 fields.
- **NDOT:** state the unit of the Width field and the meaning of Width 0 in the layer metadata, or correct the 35 zero values if they are entry errors. Cost class: low-cost operational change. Outcome measure: the Width 0 count and a stated unit on the next pull, against the baseline of 35 zero records and no stated unit.
- **NDOT:** add the NC and NA codes to the published metadata domains with their definitions, or recode the 16 records into the published domains. Cost class: low-cost operational change. Outcome measure: the off-codebook count on the next pull, against the baseline of 16 records.
- **NDOT:** publish a current audit round or state the audit cycle in the metadata, so readers can date the snapshot without reading every AuditDate. Cost class: low-cost operational change for the metadata note; a new audit round itself would be a budget decision, and the brief does not estimate a figure. Outcome measure: the share of records with an AuditDate in the most recent audit year on a future pull, against the baseline of 1,816 dated records all in 2023.

## Methods

- Source: Crosswalks (Crosswalks_2_view), Metropolitan Government of Nashville and Davidson County, ArcGIS FeatureServer layer 0 (services2.arcgis.com/HdTo6HJqh92wn4D8). Snapshot pulled November 13, 2026; pulled count 1,823 equals the server count. Layer metadata archived at data/source-metadata-layer.json; the metadata editingInfo records the service data as last edited on November 13, 2026.
- Official definitions: the coded-value domains in the layer metadata define FeatureType (L Longitudinal, T Transverse), PaintCondition (P Poor, F Fair, G Good), and CrossSlope (the three buckets, with the names Less Than or Equal to 2 percent, Between 2 percent - 5 percent, Greater than 5 percent). NC and NA are not in those domains and are reported as off-codebook values as recorded.
- Width sentinel rule: Width 0 is treated as unknown and excluded from width medians and distribution denominators; the basis is that an audited crosswalk cannot be read as zero-width from this field alone, and all 16 off-codebook control records carry the same 0 value. Zeros are counted and reported wherever width is discussed.
- Exposure: no traffic, pedestrian, street-mile, or crossing-use denominator exists in the layer, so no rate per crossing-use or per mile is computed and no causal pattern is implied. The audited set is the population for every share; whether it is all Nashville crosswalks is not stated in the layer metadata and is not claimed.
- Causality direction: the brief reports recorded condition only. It does not claim that type causes paint condition or slope; the type split is printed as recorded shares with counts.
- Category and definition changes: all dated audits fall in a single year (2023), so no within-layer trend or definition-change comparison is printed. The audit is a snapshot served in a layer whose service data was last edited in 2026; the brief dates every finding to the 2023 audit.
- Joins: no dataset join is used in the published figures. The view carries no street or district field, so there is no shared geography key; the Sidewalks and Curb Ramps comparison is prose-level, using only those briefs' published figures, and is recorded in verification.md.
- Small counts: the smallest group given a percentage claim is Transverse (237 records). The off-codebook group (16 records) and blank groups are reported as counts, with no standalone percentage claims in the prose beyond their shares of the full layer printed with counts.

## Caveats

- The audit dates are in 2023. Paint and slope conditions may have changed since the audit; nothing in the layer shows a repair, a repaint, or a later inspection.
- Cross slope is recorded in buckets, not as a measured value, and the metadata states no compliance standard; no compliance reading is printed.
- Width carries no stated unit, and 35 records carry the sentinel 0 value treated here as unknown.
- Inspector is recorded as initials on the pulled records; this brief makes no inspector-level claim, because no inspector definition or assignment geography exists in the layer.
- The snapshot is a single pull of a live layer; counts may drift by small numbers as the service is edited.

Sources for every figure are in sources.md. The pre-flight audit, independent verification, and story gate are in verification.md.
