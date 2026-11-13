import json, os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE=os.path.dirname(__file__); ROOT=os.path.normpath(os.path.join(HERE,".."))
stats=json.load(open(os.path.join(ROOT,"stats.json")))
plt.rcParams.update({"font.size":10,"axes.facecolor":"white"})
AMBER="#E8A317"; TEAL="#0E7C7B"; CHAR="#222222"
FOOT="Source: Metro Nashville Crosswalks layer (Crosswalks_2_view), 1,823 records pulled Nov 13, 2026.\nAudit dates in the layer are in 2023."
def save(fig,name):
    fig.tight_layout(); fig.savefig(os.path.join(ROOT,"charts",name), dpi=200, bbox_inches="tight"); plt.close(fig); print(name)
# 1 paint condition
labels=["Good (G)","Poor (P)","Fair (F)","NA (off-codebook)","Blank"]
vals=[734,683,389,16,1]
fig,ax=plt.subplots(figsize=(8,4.4)); bars=ax.bar(labels, vals, color=[TEAL,AMBER,CHAR, "#888888", "#BBBBBB"])
for i,v in enumerate(vals): ax.text(i,v+22,f"{v}\n({v/1823*100:.1f}%)",ha="center",fontsize=9)
ax.set_ylabel("Crosswalk records"); ax.set_ylim(0,880)
ax.set_title("Paint condition in Nashville's 2023 crosswalk audit\nPoor is 683 of 1,823 records (37.5%)")
fig.text(0.01,-0.04,FOOT,fontsize=7,ha="left")
save(fig,"chart_paint_condition.png")
# 2 cross slope buckets (recorded population)
labels2=["<= 2%\n(lowest bucket)","2% - 5%","> 5%"]
vals2=[626,1020,165]
fig,ax=plt.subplots(figsize=(8,4.4)); ax.bar(labels2, vals2, color=[TEAL,AMBER,CHAR])
for i,v in enumerate(vals2): ax.text(i,v+30,f"{v}\n({v/1811*100:.1f}% of recorded)",ha="center",fontsize=9)
ax.set_ylabel("Crosswalk records"); ax.set_ylim(0,1250)
ax.set_title("Recorded cross slope: 626 of 1,811 in the lowest bucket (34.6%)\n1,185 of 1,811 (65.4%, derived) are in buckets above 2%")
fig.text(0.01,-0.04,FOOT+" Cross slope is blank on 12 records.",fontsize=7,ha="left")
save(fig,"chart_cross_slope.png")
# 3 type split: poor share by type
fig,ax=plt.subplots(figsize=(8,4.2))
cats=["Transverse\n(237 records)","Longitudinal\n(1,563 records)"]
poor=[50.6,35.6]
ax.barh(cats, poor, color=[AMBER,TEAL])
for i,v in enumerate(poor): ax.text(v+1.2,i,f"{v}% Poor",va="center",fontsize=10)
ax.set_xlim(0,62); ax.set_xlabel("Share of the type recorded Poor")
ax.set_title("Poor paint share is higher on transverse crosswalks\n120 of 237 transverse (50.6%) vs 557 of 1,563 longitudinal (35.6%)")
ax.invert_yaxis()
fig.text(0.01,-0.04,FOOT,fontsize=7,ha="left")
save(fig,"chart_type_poor.png")
# 4 width distribution on positive widths
labels4=["Under 6","6 to under 10","10 to under 15","15 plus"]
vals4=[23,179,1568,17]
fig,ax=plt.subplots(figsize=(8,4.4)); ax.bar(labels4, vals4, color=TEAL)
for i,v in enumerate(vals4): ax.text(i,v+40,str(v),ha="center",fontsize=10)
ax.set_ylabel("Crosswalk records"); ax.set_ylim(0,1800); ax.set_xlabel("Width value as recorded (unit not stated in the layer metadata)")
ax.set_title("Width values cluster at 10 to under 15 (1,568 of 1,787 positive widths)\nMedian positive width is 10; Width 0 (35 records) is treated as unknown and excluded")
fig.text(0.01,-0.04,FOOT+" Width is blank on 1 record.",fontsize=7,ha="left")
save(fig,"chart_width_distribution.png")
# 5 paint x slope crosstab (grouped)
import numpy as np
groups=["Poor (683)","Fair (389)","Good (734)"]
le=[238,129,246]; mid=[373,219,425]; hi=[66,39,59]
x=np.arange(len(groups)); wdt=0.27
fig,ax=plt.subplots(figsize=(8,4.4))
ax.bar(x-wdt, le, wdt, color=TEAL, label="<= 2%")
ax.bar(x, mid, wdt, color=AMBER, label="2% - 5%")
ax.bar(x+wdt, hi, wdt, color=CHAR, label="> 5%")
for xi,arr in [(0,le),(1,mid),(2,hi)]:
    pass
for i in range(3):
    for off,v in [(-wdt,le[i]),(0,mid[i]),(wdt,hi[i])]:
        ax.text(i+off, v+10, str(v), ha="center", fontsize=8)
ax.set_xticks(x); ax.set_xticklabels(groups); ax.set_ylabel("Crosswalk records"); ax.set_ylim(0,500); ax.legend(fontsize=8)
ax.set_title("Paint condition by recorded cross slope bucket\nSlope is blank on 12 records; the off-codebook NA group (16) is not plotted")
fig.text(0.01,-0.04,FOOT,fontsize=7,ha="left")
save(fig,"chart_paint_by_slope.png")
