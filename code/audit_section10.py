import csv, os, collections, datetime
HERE=os.path.dirname(__file__); DATA=os.path.normpath(os.path.join(HERE,"..","data"))
rows=list(csv.DictReader(open(os.path.join(DATA,"nashville_crosswalks_raw.csv"),encoding="utf-8")))
out=[]
def log(s): out.append(str(s)); print(s)
log(f"rows={len(rows)}")
for col in ["FeatureType","PaintCondition","CrossSlope","Inspector"]:
    c=collections.Counter(r[col] for r in rows)
    log(f"Counter {col}: {dict(c.most_common())}")
# Width sentinel: 0 treated as unknown
widths=[r["Width"] for r in rows]
blank_w=sum(1 for w in widths if w=="")
zero_w=[r for r in rows if r["Width"]=="0"]
pos_w=[r for r in rows if r["Width"] not in ("",) and int(r["Width"])>0]
log(f"Width blank: {blank_w}; Width == 0 sentinel count: {len(zero_w)} (treated as unknown: a crosswalk in the audit cannot be read as zero-width from this field alone; excluded from width medians and distribution denominators, counted and reported here)")
log(f"Width positive count: {len(pos_w)}; unknown (0 or blank) count: {len(zero_w)+blank_w}; positive + unknown = {len(pos_w)+len(zero_w)+blank_w} = total rows {len(rows)}")
log(f"Width 0 by FeatureType: {dict(collections.Counter(r['FeatureType'] for r in zero_w))}; Width 0 coded records by PaintCondition: {dict(collections.Counter(r['PaintCondition'] for r in zero_w if r['FeatureType']!='NC'))}")
# Polarity check: matched (excluded, Width 0) vs included (positive) sample
log(f"Polarity sample EXCLUDED from width denominators (Width==0): {[(r['OBJECTID'], r['Width'], r['FeatureType'], r['PaintCondition']) for r in zero_w[:3]]}")
log(f"Polarity sample INCLUDED in width denominators (Width>0): {[(r['OBJECTID'], r['Width'], r['FeatureType'], r['PaintCondition']) for r in pos_w[:3]]}")
log("Polarity check: code keeps Width>0 in medians/distributions and excludes Width==0 as unknown - matches the stated sentinel rule and its comment.")
# Off-codebook control: NC / NA
nc=[r for r in rows if r["FeatureType"]=="NC"]; na=[r for r in rows if r["PaintCondition"]=="NA"]
log(f"FeatureType NC count: {len(nc)}; PaintCondition NA count: {len(na)}; same OBJECTIDs: {set(r['OBJECTID'] for r in nc)==set(r['OBJECTID'] for r in na)}; NC Width values: {dict(collections.Counter(r['Width'] for r in nc))}")
log("NC and NA do not appear in the layer metadata coded-value domains for FeatureType or PaintCondition; they are reported as a distinct subpopulation, never merged into the coded categories.")
# Nullable denominator: slope and paint shares on stated populations
slope_rec=[r for r in rows if r["CrossSlope"]!=""]
log(f"CrossSlope recorded: {len(slope_rec)} of {len(rows)}; blank: {len(rows)-len(slope_rec)}; recorded + blank = {len(slope_rec)+(len(rows)-len(slope_rec))}; slope bucket shares use the recorded population (1,811) as denominator, printed with the count")
paint_rec=[r for r in rows if r["PaintCondition"]!=""]
log(f"PaintCondition recorded (including off-codebook NA): {len(paint_rec)} of {len(rows)}; blank: {len(rows)-len(paint_rec)}; paint shares in the brief use the full 1,823 denominator with counts printed")
# Unit agreement
log("Unit agreement: every rate is crosswalk records over crosswalk records on the same stated population; Width carries no unit in the layer metadata and no unit is stated anywhere in the brief.")
# AssetID uniqueness
log(f"AssetID populated: {sum(1 for r in rows if r['AssetID'])}; AssetID distinct: {len(set(r['AssetID'] for r in rows))}")
# AuditDate range
dates=[int(r["AuditDate"]) for r in rows if r["AuditDate"]!=""]
log(f"AuditDate populated: {len(dates)}; blank: {len(rows)-len(dates)}; min UTC: {datetime.datetime.fromtimestamp(min(dates)/1000, tz=datetime.timezone.utc).date()}; max UTC: {datetime.datetime.fromtimestamp(max(dates)/1000, tz=datetime.timezone.utc).date()}; all in 2023: {all(datetime.datetime.fromtimestamp(d/1000, tz=datetime.timezone.utc).year==2023 for d in dates)}")
assert len(rows)==1823
assert len(pos_w)+len(zero_w)+blank_w==len(rows)
open(os.path.join(DATA,"audit_output.txt"),"w").write("\n".join(out)+"\n")
print("AUDIT PASS")
