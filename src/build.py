import json
from data import D
import bullets
import transitions
PLAN=[
(1,'Welcome',0,0,'fade'),(2,'Welcome',0,0,'fade'),(101,'Welcome',0,0,'fade'),(130,'Welcome · AI tip',0,0,'scan'),(132,'Welcome · AI tip',0,0,'fade'),(3,'Welcome',0,0,'pixel'),
(102,'The divide',0,0,'pixel'),(7,'The divide',0,0,'fade'),(103,'The divide',0,0,'fade'),(104,'The divide',0,0,'fade'),(6,'The divide',0,0,'blinds'),(9,'The divide',0,0,'scan'),
(105,'Before · Concerns',1,2,'pixel'),(107,'Before · Concerns',1,4,'scan'),
(15,'Before · Goals',2,2,'pixel'),(17,'Before · Goals',2,2,'fade'),
(18,'Phase 1 · Play',3,6,'pixel'),(19,'Phase 1 · Play',3,2,'fade'),(109,'Phase 1 · Play',3,3,'blinds'),(110,'Phase 1 · Play',3,4,'scan'),
(22,'Phase 2 · Build',4,6,'pixel'),(38,'Phase 2 · Build',4,2,'fade'),(39,'Phase 2 · Build',4,2,'fade'),(12,'Phase 2 · Build',4,3,'blinds'),(111,'Phase 2 · Build',4,5,'fade'),
(25,'Phase 3 · Design',5,6,'pixel'),(40,'Phase 3 · Design',5,2,'fade'),(126,'Phase 3 · Design',5,2,'fade'),(27,'Phase 3 · Design',5,3,'blinds'),
(24,'After · Result',6,4,'scan'),
(43,'After · Lessons',7,6,'pixel'),(31,'After · Lessons',7,4,'fade'),
(114,'After · Lessons',7,2,'pixel'),(115,'After · Lessons',7,2,'fade'),(116,'After · Lessons',7,2,'fade'),(120,'After · Lessons',7,2,'blinds'),(117,'After · Lessons',7,2,'fade'),(119,'After · Lessons',7,2,'scan'),
(37,'Closing',-1,0,'scan'),(36,'Q&A',-1,0,'fade')]
import os,collections
def mv(st,cnt):
    if st<=0: return None
    if st==8: return [4]*7
    return [4 if i<st-1 else (cnt if i==st-1 else 0) for i in range(7)]
for k,v in bullets.BUL.items():
    D[k]=(D[k][0],D[k][1],v)
tot=collections.Counter(p[2] for p in PLAN); seen=collections.Counter()
KIND={1:'Overview',2:'Example',3:'Pitfall',4:'Cool thing',5:'The fix',6:'Overview'}
th=json.load(open('thumbs.json')) if os.path.exists('thumbs.json') else {}
meta=[]
TX=transitions.auto_tx([x[1] for x in PLAN],[x[0] for x in PLAN])
for pos,(n,s,st,p,_tx) in enumerate(PLAN,1):
    tx=TX[pos-1]
    seen[st]+=1
    c=-(-4*seen[st]//tot[st]) if st in range(1,8) else 0
    d={"o":n,"m":n,"s":s,"mv":mv(st,c),"t":D[n][0],"tx":tx,"d":D[n][2]}
    if 1<=st<=7:
        d["h"]=1; d["k"]='Principle' if (st in (1,2) and p==2) else ('Takeaway' if (st==7 and p not in (1,6)) else KIND[p])
    if str(pos) in th: d["th"]=th[str(pos)]
    meta.append(d)
t=open('template.html').read().replace('/*META*/[]',json.dumps(meta,ensure_ascii=False))
import base64
for _n in ['walkthrough-3','walkthrough-2','walkthrough-1','walkthrough-4']:
    _u='data:video/mp4;base64,'+base64.b64encode(open(f'vid/{_n}.mp4','rb').read()).decode()
    t=t.replace(f"videos/{_n}.mp4",_u)
open('/mnt/user-data/outputs/ai-enabling-a-team.html','w').write(t.replace('__GATED__','false'))
open('/mnt/user-data/outputs/ai-native-team-deck-gated.html','w').write(t.replace('__GATED__','true'))
print(len(t))
