"""ScholarFind educational prototype with synthetic scholarship records."""
from flask import Flask, jsonify, request, render_template_string
from engine import evaluate, checklist
app=Flask(__name__)
SCHOLARSHIPS=[
 {'id':1,'name':'Merit Excellence (Demo)','min_marks':80,'max_income':600000,'category':'Any','source':'Demo record — verify with scholarship provider'},
 {'id':2,'name':'Community Support (Demo)','min_marks':60,'max_income':300000,'category':'Reserved','source':'Demo record — verify with scholarship provider'},
 {'id':3,'name':'Education Access (Demo)','min_marks':50,'max_income':250000,'category':'Any','source':'Demo record — verify with scholarship provider'}]
HTML='''<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>ScholarFind</title><style>body{font-family:Arial;background:#f3f6fa;color:#15304b;margin:0}header{background:#12395c;color:white;padding:24px}main{max-width:920px;margin:30px auto;padding:20px}.panel{background:white;padding:24px;border-radius:12px;box-shadow:0 2px 10px #ccd}input,select,button{padding:10px;margin:6px;border:1px solid #b6c3d2;border-radius:5px}button{background:#1672a5;color:white;cursor:pointer}.item{padding:14px;border-bottom:1px solid #ddd}.small{color:#666}</style></head><body><header><h1>ScholarFind</h1><p>Scholarship finder and eligibility checker | Educational prototype</p></header><main><div class="panel"><h2>Check your eligibility</h2><form id="f"><label>Marks % <input name="min_marks" type="number" min="0" max="100" required value="85"></label><label>Annual income (INR) <input name="max_income" type="number" min="0" required value="200000"></label><label>Category <select name="category"><option>General</option><option>Reserved</option></select></label><button>Find scholarships</button></form><p class="small">Sample scholarships only. Final eligibility must be confirmed by the scholarship officer and official source.</p><div id="results"></div></div></main><script>document.getElementById('f').onsubmit=async e=>{e.preventDefault();const d=Object.fromEntries(new FormData(e.target));const r=await fetch('/api/match',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});const j=await r.json();document.getElementById('results').innerHTML=j.map(x=>`<div class="item"><h3>${x.name}</h3><b>${x.result.status}</b><p>${x.result.reasons.join('; ')}</p><p>Checklist: ${x.checklist.join(', ')}</p><small>${x.source}</small></div>`).join('')};</script></body></html>'''
@app.get('/')
def home(): return render_template_string(HTML)
@app.get('/health')
def health(): return jsonify(status='ok')
@app.get('/api/scholarships')
def scholarships(): return jsonify(SCHOLARSHIPS)
@app.post('/api/match')
def match():
    data=request.get_json(silent=True)
    if not isinstance(data,dict): return jsonify(error='JSON object required'),400
    try:
        marks=float(data['min_marks']); income=float(data['max_income'])
        if not 0<=marks<=100 or income<0 or data.get('category') not in ('General','Reserved'):
            raise ValueError()
    except (ValueError,TypeError,KeyError): return jsonify(error='Valid marks, income and category required'),400
    return jsonify([{**s,'result':evaluate(s,data),'checklist':checklist(s)} for s in SCHOLARSHIPS])
if __name__=='__main__': app.run(host='0.0.0.0',port=5000)
