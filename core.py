from pathlib import Path
import pandas as pd,numpy as np,math
ROOT=Path(__file__).parent

def attribute(touches,conversions,model='linear',lookback=30,half_life=7):
 if model not in ['first','last','linear','time-decay']:raise ValueError('Unknown model')
 if not math.isfinite(lookback) or not 1<=lookback<=90 or not math.isfinite(half_life) or half_life<=0:raise ValueError('Lookback must be 1–90 days and half-life positive')
 if touches.touch_id.duplicated().any() or conversions.conversion_id.duplicated().any():raise ValueError('Duplicate source IDs')
 if (conversions.revenue_cents<0).any():raise ValueError('Conversion value must be nonnegative')
 t=touches.copy();c=conversions.copy();t.timestamp=pd.to_datetime(t.timestamp,utc=True);c.timestamp=pd.to_datetime(c.timestamp,utc=True);out=[];previous={}
 for row in c.sort_values(['timestamp','conversion_id']).itertuples():
  lower=max(row.timestamp-pd.Timedelta(days=lookback),previous.get(row.customer,pd.Timestamp.min.tz_localize('UTC')))
  path=t[(t.customer==row.customer)&(t.timestamp>lower)&(t.timestamp<=row.timestamp)].sort_values(['timestamp','touch_id']);previous[row.customer]=row.timestamp
  if path.empty:out.append(dict(conversion=row.conversion_id,channel='Unattributed',credit=1.,revenue_cents=float(row.revenue_cents)));continue
  weights=np.zeros(len(path))
  if model=='first':weights[0]=1
  elif model=='last':weights[-1]=1
  elif model=='linear':weights[:]=1/len(path)
  else:
   weights=np.exp2(-(row.timestamp-path.timestamp).dt.total_seconds().to_numpy()/86400/half_life);weights/=weights.sum()
  for channel,w in zip(path.channel,weights):out.append(dict(conversion=row.conversion_id,channel=channel,credit=float(w),revenue_cents=float(row.revenue_cents*w)))
 return pd.DataFrame(out)
def analyze(p):
 t=pd.read_csv(ROOT/'data/touches.csv');c=pd.read_csv(ROOT/'data/conversions.csv');s=pd.read_csv(ROOT/'data/spend.csv');model=p.get('model','linear');credits=attribute(t,c,model,float(p.get('lookback',30)),float(p.get('half_life',7)))
 g=credits.groupby('channel')[['credit','revenue_cents']].sum().reset_index().merge(s,on='channel',how='outer').fillna(0);g['attributed_revenue_usd']=g.revenue_cents/100;g['attributed_roas']=g.attributed_revenue_usd/g.spend_usd.replace(0,np.nan);g=g.drop(columns='revenue_cents').round(3).replace({np.nan:None})
 return dict(metrics={'Conversions':len(c),'Allocated credit':round(credits.credit.sum(),4),'Revenue':f'${c.revenue_cents.sum()/100:,.2f}','Model':model},bars=[dict(label=r['channel'],value=r['attributed_revenue_usd']) for r in g.to_dict('records')],rows=g.to_dict('records'),details={'credit_total':float(credits.credit.sum()),'revenue_cents_total':float(credits.revenue_cents.sum()),'conversion_revenue_cents':int(c.revenue_cents.sum()),'window':'(max(previous conversion, lookback start), conversion time]','unattributed':'No eligible touch receives explicit unattributed credit'},notice='Model choice can change channel rankings. ROAS uses assigned credit, not causal lift; channel spend covers the synthetic example period.')
