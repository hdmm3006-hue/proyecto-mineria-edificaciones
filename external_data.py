"""Consumo reproducible de fuente oficial. Autor: Henry David Muñoz Molina.
Sin --refresh utiliza la respuesta archivada; --refresh consulta el servicio.
La consulta agrega conteos por pisos: no descarga datos personales ni inventa uniones.
"""
from pathlib import Path
import argparse, urllib.request, urllib.parse, json, hashlib
from datetime import datetime, timezone
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'data/external';OUT.mkdir(exist_ok=True)
URL='https://sig.catastrobogota.gov.co/arcgis/rest/services/catastro/construccion/MapServer/0/query'
PARAMS={'where':'1=1','groupByFieldsForStatistics':'CONNPISOS','outStatistics':json.dumps([{'statisticType':'count','onStatisticField':'OBJECTID','outStatisticFieldName':'n'}]),'orderByFields':'CONNPISOS ASC','returnGeometry':'false','f':'json'}
def run(refresh=False):
    target=OUT/'catastro_pisos_response.json'
    if refresh or not target.exists():
        req=urllib.request.Request(URL+'?'+urllib.parse.urlencode(PARAMS),headers={'User-Agent':'AcademicDataMining/1.0'})
        with urllib.request.urlopen(req,timeout=45) as res:
            body=res.read(); status=res.status
        obj=json.loads(body)
        if 'error' in obj: raise RuntimeError(obj['error'])
        if obj.get('exceededTransferLimit'): raise RuntimeError('Respuesta truncada: no analizar como completa.')
        assert 'features' in obj and len(obj['features'])>0
        target.write_bytes(body)
        meta={'source':'Unidad Administrativa Especial de Catastro Distrital, Construcción Bogotá','url':URL,'parameters':PARAMS,'retrieved_at_utc':datetime.now(timezone.utc).isoformat(),'http_status':status,'sha256':hashlib.sha256(body).hexdigest(),'unit':'construction feature in cadastral layer; not necessarily one independent building','scope':'all records returned as grouped counts by floor count','license_note':'Official public service; cite owner. No open license invented.'}
        (OUT/'provenance.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
    body=target.read_bytes();meta=json.loads((OUT/'provenance.json').read_text())
    assert hashlib.sha256(body).hexdigest()==meta['sha256']
    obj=json.loads(body);assert not obj.get('exceededTransferLimit') and 'error' not in obj
    frame=pd.DataFrame([f['attributes'] for f in obj['features']])
    frame=frame.rename(columns={c:'n' for c in frame.columns if c.lower()=='n'})
    assert set(['CONNPISOS','n']).issubset(frame.columns)
    frame['n']=pd.to_numeric(frame['n']);assert (frame.n>=0).all()
    frame.to_csv(OUT/'catastro_frecuencia_pisos.csv',index=False)
    numeric=pd.to_numeric(frame.CONNPISOS,errors='coerce')
    good=numeric.notna()&(numeric>0)&(numeric%1==0)
    valid=frame.loc[good].copy();valid['CONNPISOS']=numeric[good]
    own=pd.read_csv(ROOT/'data/08_dataset_limpio.csv');own=own[own.ciudad=='Bogotá']
    bins=[0,4,10,20,50,float('inf')];labs=['1–4','5–10','11–20','21–50','51+']
    ext=valid.groupby(pd.cut(valid.CONNPISOS,bins,labels=labs),observed=False).n.sum()
    local=own.groupby(pd.cut(own.numero_pisos,bins,labels=labs),observed=False).size()
    comp=pd.DataFrame({'catastro_count':ext,'constructed_count':local})
    comp['catastro_pct']=100*comp.catastro_count/comp.catastro_count.sum()
    comp['constructed_pct']=100*comp.constructed_count/comp.constructed_count.sum()
    comp.to_csv(ROOT/'results/comparacion_fuente_externa.csv')
    stats={'external_total':int(frame.n.sum()),'external_valid_positive_integer_floor_records':int(valid.n.sum()),'external_missing_or_invalid_floor_records':int(frame.loc[~good,'n'].sum()),'external_mean_floors_valid':float((valid.CONNPISOS*valid.n).sum()/valid.n.sum()),'constructed_bogota_n':int(len(own)),'constructed_bogota_mean_floors':float(own.numero_pisos.mean()),'source_sha256':meta['sha256'],'retrieved_at_utc':meta['retrieved_at_utc']}
    (ROOT/'results/external_summary.json').write_text(json.dumps(stats,indent=2))
    ax=comp[['catastro_pct','constructed_pct']].plot.bar(figsize=(8,4),color=['#176B87','#C67A3A'])
    ax.set(xlabel='Floor-count band',ylabel='Within-source share (%)',title='Bogotá: descriptive contrast, different coverage and units')
    ax.legend(['Official cadastral features','Constructed project records']);ax.tick_params(axis='x',rotation=0)
    plt.tight_layout();plt.savefig(ROOT/'figures/08_external_comparison.png',dpi=180);plt.close()
    print(json.dumps(stats,indent=2));print(comp.round(3).to_string())
    return stats
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--refresh',action='store_true');args=parser.parse_args();run(args.refresh)
