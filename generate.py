from pathlib import Path
import csv,random
from datetime import datetime,timedelta
r=random.Random(22);root=Path(__file__).parent;(root/'data').mkdir(exist_ok=True)
with (root/'data/touches.csv').open('w') as f,(root/'data/conversions.csv').open('w') as g:
 t=csv.writer(f);c=csv.writer(g);t.writerow(['touch_id','customer','timestamp','channel']);c.writerow(['conversion_id','customer','timestamp','revenue_cents']);counter=0
 for customer in range(200):
  end=datetime(2026,7,1)+timedelta(days=r.randint(0,27));uid=f'C{customer:03}'
  for _ in range(r.randint(0,7)):
   counter+=1;t.writerow([counter,uid,(end-timedelta(hours=r.randint(1,1000))).isoformat(),r.choice(['Search','Social','Email','Referral'])])
  if r.random()<.6:c.writerow([f'V{customer}',uid,end.isoformat(),r.randint(2500,20000)])
with (root/'data/spend.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['channel','spend_usd']);w.writerows([['Search',3000],['Social',2200],['Email',350],['Referral',500]])
