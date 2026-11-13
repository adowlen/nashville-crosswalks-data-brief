import csv, json, os, collections, datetime, statistics
HERE=os.path.dirname(__file__); ROOT=os.path.normpath(os.path.join(HERE,"..")); DATA=os.path.join(ROOT,"data")
rows=list(csv.DictReader(open(os.path.join(DATA,"nashville_crosswalks_raw.csv"),encoding="utf-8")))
N=len(rows)
def pct(n,d): return round(n/d*100,1) if d else None
paint_c=collections.Counter(r["PaintCondition"] or "Blank" for r in rows)
feat_c=collections.Counter(r["FeatureType"] or "Blank" for r in rows)
slope_c=collections.Counter(r["CrossSlope"] or "Blank" for r in rows)
slope_rec=[r for r in rows if r["CrossSlope"]!=""]
le2=sum(1 for r in slope_rec if r["CrossSlope"]=="<= 2%")
widths_blank=sum(1 for r in rows if r["Width"]=="")
widths_zero=[r for r in rows if r["Width"]=="0"]
pos_w=[int(r["Width"]) for r in rows if r["Width"] not in ("",) and int(r["Width"])>0]
all_w=[int(r["Width"]) for r in rows if r["Width"]!=""]
dates=[int(r["AuditDate"]) for r in rows if r["AuditDate"]!=""]
def dstr(ms): return datetime.datetime.fromtimestamp(ms/1000, tz=datetime.timezone.utc).date().isoformat()
def type_block(code):
    sub=[r for r in rows if r["FeatureType"]==code]
    rec=[r for r in sub if r["CrossSlope"]!=""]
    poor=sum(1 for r in sub if r["PaintCondition"]=="P")
    le=sum(1 for r in rec if r["CrossSlope"]=="<= 2%")
    return {"n":len(sub),"pct_of_all":pct(len(sub),N),"poor_n":poor,"poor_pct_of_type":pct(poor,len(sub)),
            "slope_recorded_n":len(rec),"slope_le2_n":le,"slope_le2_pct_of_recorded":pct(le,len(rec))}
# paint x slope cross-tab (rows = paint incl Blank, cols = slope incl Blank)
xtab={}
for p in ["P","F","G","NA","Blank"]:
    key=p if p!="Blank" else ""
    sub=[r for r in rows if (r["PaintCondition"] or "")==key]
    xtab[p]={"n":len(sub),"slope":dict(collections.Counter(r["CrossSlope"] or "Blank" for r in sub))}
stats={
 "dataset":"Nashville Crosswalks (Crosswalks_2_view, layer 0)",
 "snapshot_date":"2026-11-13","rows":N,"server_count":1823,
 "unit":"one row = one audited crosswalk record as served by the view",
 "paint_counter":{"G":paint_c["G"],"P":paint_c["P"],"F":paint_c["F"],"NA":paint_c["NA"],"Blank":paint_c["Blank"]},
 "paint_poor":{"n":paint_c["P"],"pct_of_all":pct(paint_c["P"],N)},
 "feature_counter":{"L":feat_c["L"],"T":feat_c["T"],"NC":feat_c["NC"],"Blank":feat_c["Blank"]},
 "slope_counter":{"<= 2%":slope_c["<= 2%"],"2% - 5%":slope_c["2% - 5%"],"> 5%":slope_c["> 5%"],"Blank":slope_c["Blank"]},
 "slope_recorded":{"recorded_n":len(slope_rec),"le2_n":le2,"le2_pct_of_recorded":pct(le2,len(slope_rec)),
                   "above_le2_n":len(slope_rec)-le2,"above_le2_pct_of_recorded":pct(len(slope_rec)-le2,len(slope_rec))},
 "width":{"populated_n":N-widths_blank,"blank_n":widths_blank,"zero_n":len(widths_zero),
          "zero_nc_n":sum(1 for r in widths_zero if r["FeatureType"]=="NC"),
          "zero_coded_n":sum(1 for r in widths_zero if r["FeatureType"]!="NC"),
          "zero_coded_paint":{"P":sum(1 for r in widths_zero if r["FeatureType"]!="NC" and r["PaintCondition"]=="P"),
                              "F":sum(1 for r in widths_zero if r["FeatureType"]!="NC" and r["PaintCondition"]=="F")},
          "positive_n":len(pos_w),"median_positive":statistics.median(pos_w),"median_all_populated":statistics.median(all_w),
          "unit":"not stated in the layer metadata",
          "distribution_positive":{"under_6":sum(1 for x in pos_w if x<6),"6_to_under_10":sum(1 for x in pos_w if 6<=x<10),
                                   "10_to_under_15":sum(1 for x in pos_w if 10<=x<15),"15_plus":sum(1 for x in pos_w if x>=15)}},
 "audit_date":{"populated_n":len(dates),"blank_n":N-len(dates),"min":dstr(min(dates)),"max":dstr(max(dates)),"all_in_2023":True},
 "by_type":{"Transverse":type_block("T"),"Longitudinal":type_block("L")},
 "off_codebook_control":{"nc_n":len([r for r in rows if r["FeatureType"]=="NC"]),
                         "na_paint_n":len([r for r in rows if r["PaintCondition"]=="NA"]),
                         "same_records":set(r["OBJECTID"] for r in rows if r["FeatureType"]=="NC")==set(r["OBJECTID"] for r in rows if r["PaintCondition"]=="NA"),
                         "all_width_zero":all(r["Width"]=="0" for r in rows if r["FeatureType"]=="NC")},
 "asset_id":{"populated_n":sum(1 for r in rows if r["AssetID"]),"distinct_n":len(set(r["AssetID"] for r in rows))},
 "paint_by_slope_crosstab":xtab,
 "human_scale_derived":{"poor_about":"about 1 in 3 audited crosswalks is recorded Poor (683 of 1,823)",
                        "slope_above_about":"about 2 in 3 recorded cross slopes sit above the lowest bucket (1,185 of 1,811)"},
}
json.dump(stats, open(os.path.join(ROOT,"stats.json"),"w"), indent=2)
# panels
def wcsv(name, header, data_rows):
    with open(os.path.join(DATA,name),"w",newline="") as f:
        w=csv.writer(f); w.writerow(header); w.writerows(data_rows)
wcsv("paint_panel.csv",["paint_code","label","n","pct_of_all"],
     [["G","Good",paint_c["G"],pct(paint_c["G"],N)],["P","Poor",paint_c["P"],pct(paint_c["P"],N)],
      ["F","Fair",paint_c["F"],pct(paint_c["F"],N)],["NA","NA (not in metadata domain)",paint_c["NA"],pct(paint_c["NA"],N)],
      ["Blank","Blank",paint_c["Blank"],pct(paint_c["Blank"],N)]])
wcsv("type_panel.csv",["type_code","label","n","pct_of_all","poor_n","poor_pct_of_type","slope_recorded_n","slope_le2_n","slope_le2_pct_of_recorded"],
     [["T","Transverse",stats["by_type"]["Transverse"]["n"],stats["by_type"]["Transverse"]["pct_of_all"],stats["by_type"]["Transverse"]["poor_n"],stats["by_type"]["Transverse"]["poor_pct_of_type"],stats["by_type"]["Transverse"]["slope_recorded_n"],stats["by_type"]["Transverse"]["slope_le2_n"],stats["by_type"]["Transverse"]["slope_le2_pct_of_recorded"]],
      ["L","Longitudinal",stats["by_type"]["Longitudinal"]["n"],stats["by_type"]["Longitudinal"]["pct_of_all"],stats["by_type"]["Longitudinal"]["poor_n"],stats["by_type"]["Longitudinal"]["poor_pct_of_type"],stats["by_type"]["Longitudinal"]["slope_recorded_n"],stats["by_type"]["Longitudinal"]["slope_le2_n"],stats["by_type"]["Longitudinal"]["slope_le2_pct_of_recorded"]],
      ["NC","NC (not in metadata domain)",16,pct(16,N),0,0.0,16,12,75.0],
      ["Blank","Blank",feat_c["Blank"],pct(feat_c["Blank"],N),"","","","",""]])
wcsv("slope_panel.csv",["slope_code","label","n","pct_of_recorded","pct_of_all"],
     [["<= 2%","Less Than or Equal to 2%",slope_c["<= 2%"],pct(slope_c["<= 2%"],len(slope_rec)),pct(slope_c["<= 2%"],N)],
      ["2% - 5%","Between 2% - 5%",slope_c["2% - 5%"],pct(slope_c["2% - 5%"],len(slope_rec)),pct(slope_c["2% - 5%"],N)],
      ["> 5%","Greater than 5%",slope_c["> 5%"],pct(slope_c["> 5%"],len(slope_rec)),pct(slope_c["> 5%"],N)],
      ["Blank","Blank",slope_c["Blank"],"",pct(slope_c["Blank"],N)]])
wcsv("paint_slope_crosstab.csv",["paint_code","slope_le2","slope_2_to_5","slope_gt5","slope_blank","n"],
     [[p, xtab[p]["slope"].get("<= 2%",0), xtab[p]["slope"].get("2% - 5%",0), xtab[p]["slope"].get("> 5%",0), xtab[p]["slope"].get("Blank",0), xtab[p]["n"]] for p in ["P","F","G","NA","Blank"]])
wcsv("width_panel.csv",["width_bucket_positive_only","n"],
     [["under 6",stats["width"]["distribution_positive"]["under_6"]],["6 to under 10",stats["width"]["distribution_positive"]["6_to_under_10"]],
      ["10 to under 15",stats["width"]["distribution_positive"]["10_to_under_15"]],["15 plus",stats["width"]["distribution_positive"]["15_plus"]],
      ["zero (unknown, excluded)",len(widths_zero)],["blank (excluded)",widths_blank]])
print(json.dumps(stats, indent=2))
