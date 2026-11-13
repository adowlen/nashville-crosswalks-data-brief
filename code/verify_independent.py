import pandas as pd, json, os
HERE=os.path.dirname(__file__); ROOT=os.path.normpath(os.path.join(HERE,"..")); DATA=os.path.join(ROOT,"data")
df=pd.read_csv(os.path.join(DATA,"nashville_crosswalks_raw.csv"), low_memory=False, dtype={"FeatureType":str,"PaintCondition":str,"CrossSlope":str}, keep_default_na=False)
df["Width"]=pd.to_numeric(df["Width"], errors="coerce")
checks={}
checks["rows"]=(len(df)==1823)
checks["poor_n"]=(int((df["PaintCondition"]=="P").sum())==683)
checks["poor_pct"]=bool(abs((df["PaintCondition"]=="P").mean()*100-37.5)<0.06)
rec=df[df["CrossSlope"]!=""]
checks["slope_le2_pct"]=bool(abs((rec["CrossSlope"]=="<= 2%").mean()*100-34.6)<0.06)
checks["slope_above_n"]=(int((rec["CrossSlope"]!="<= 2%").sum())==1185)
checks["transverse_poor_pct"]=bool(abs((df[df["FeatureType"]=="T"]["PaintCondition"]=="P").mean()*100-50.6)<0.06)
checks["nc_na_same_records"]=bool(set(df.loc[df["FeatureType"]=="NC","OBJECTID"])==set(df.loc[df["PaintCondition"]=="NA","OBJECTID"]) and len(set(df.loc[df["FeatureType"]=="NC","OBJECTID"]))==16)
pos=df.loc[df["Width"]>0,"Width"]
checks["width_median_positive"]=bool(float(pos.median())==10.0)
checks["width_zero_n"]=(int((df["Width"]==0).sum())==35)
checks["asset_all_distinct"]=bool(df["AssetID"].nunique()==1823 and df["AssetID"].notna().all())
dates=pd.to_datetime(df["AuditDate"], unit="ms", utc=True)
checks["audit_all_2023"]=bool(dates.dt.year.dropna().eq(2023).all() and int(dates.notna().sum())==1816)
out={"checks":{k:bool(v) for k,v in checks.items()},"pass_count":int(sum(bool(v) for v in checks.values())),"total":len(checks),"all_pass":bool(all(checks.values()))}
json.dump(out, open(os.path.join(DATA,"verify_independent_output.json"),"w"), indent=2)
print(out); assert out["all_pass"]
