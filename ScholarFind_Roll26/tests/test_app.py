import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from app import app, SCHOLARSHIPS
from engine import evaluate,checklist

def test_eligible(): assert evaluate(SCHOLARSHIPS[0],{'min_marks':85,'max_income':200000,'category':'General'})['status']=='Eligible'
def test_low_marks(): assert evaluate(SCHOLARSHIPS[0],{'min_marks':40,'max_income':200000,'category':'General'})['status']=='Not eligible'
def test_high_income(): assert evaluate(SCHOLARSHIPS[0],{'min_marks':90,'max_income':900000,'category':'General'})['status']=='Not eligible'
def test_category(): assert evaluate(SCHOLARSHIPS[1],{'min_marks':90,'max_income':100000,'category':'General'})['status']=='Not eligible'
def test_missing(): assert evaluate(SCHOLARSHIPS[0],{'min_marks':90})['status']=='Needs review'
def test_checklist(): assert 'Category certificate' in checklist(SCHOLARSHIPS[1])
def test_health(): assert app.test_client().get('/health').json['status']=='ok'
def test_scholarships(): assert len(app.test_client().get('/api/scholarships').json)==3
def test_match():
 r=app.test_client().post('/api/match',json={'min_marks':90,'max_income':100000,'category':'Reserved'})
 assert r.status_code==200 and len(r.json)==3
def test_invalid(): assert app.test_client().post('/api/match',json={'min_marks':110,'max_income':-1,'category':'General'}).status_code==400
