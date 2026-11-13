# Reviewer notes - Nashville Crosswalks, 2026-11-13

Thesis (recorded before final prose, from the pre-analysis data profile): Nashville's 2023 crosswalk audit records more than a third of audited crosswalks with Poor paint (683 of 1,823, 37.5 percent) and about two-thirds of recorded cross slopes in buckets above the data's lowest 2 percent category, and the published layer carries no street or district field, so the audit's findings cannot be placed by neighborhood or street from the layer as published.

Claims most likely to be challenged:
- The slope figures invite a compliance reading the brief deliberately does not print. The metadata names the buckets and states no compliance standard; the brief reports buckets as recorded and calls the 2 percent boundary the data's own lowest category. A reader with the applicable standard could add a reading the brief does not make.
- The Width 0 sentinel rule: 0 is treated as unknown on the basis that an audited crosswalk cannot be read as zero-width from this field alone, supported by all 16 off-codebook control records carrying 0. If Metro states that 0 is a measured value for a defined case, the width distribution denominators would change; the medians would not (10 either way, printed both ways in the brief).
- The placeability finding is about the public view as published. Location may exist in a companion asset system keyed by AssetID; the brief states that alternative in What this might mean and asks the publisher, in Who can act, to publish the field or the pointer.
- NC and NA are called off-codebook because they appear in no coded-value domain in the archived layer metadata. If Metro publishes a fuller codebook elsewhere, the codes may have definitions this layer's metadata does not carry; the brief's claim is scoped to the layer metadata as archived.
- The audit is dated 2023 while the pull is 2026. Every finding is dated to the audit; a challenger could note conditions may have changed, which the Caveats already state.

Methods checks that could not be completed:
- Street, district, or neighborhood analysis: impossible from the layer as published (no such field exists in the view). Cut, not estimated.
- Joined comparison with the Sidewalks (2026-11-10) and Curb Ramps (2026-11-11) briefs: cut as a data join, because the crosswalks view carries no shared geography key. Prose-level reference to their published figures only.
- Exposure normalization: no traffic, pedestrian, street-mile, or crossing-use denominator exists in the layer; the brief says so prominently and computes no use-based rate.
- Coverage question: whether the 1,823 audited records are all Nashville crosswalks is not stated in the layer metadata; the brief uses the audited set as its population and claims nothing wider.

Surprising findings:
- The 16 NC records and the 16 NA records are exactly the same records, and all 16 carry Width 0: three separate fields align on one small subpopulation.
- Only 34.6 percent of recorded cross slopes sit in the layer's lowest bucket, while paint condition and slope bucket do not separate in the cross-tabulation: the lowest-bucket share is similar for Poor, Fair, and Good records.
- A layer served in 2026, with service data last edited November 13, 2026, carries an audit whose every dated record is from 2023.
- AssetID is complete and fully distinct (1,823 of 1,823) in a layer that otherwise carries off-codebook codes, a sentinel width, and no location field.

No finding in this brief reflects badly on a named individual. The publisher-level findings (missing location field, unstated width unit, off-codebook codes, audit dating) name NDOT as the layer publisher in the Who can act section, in measured terms, with baselines and the outcome measures that would show a fix.
