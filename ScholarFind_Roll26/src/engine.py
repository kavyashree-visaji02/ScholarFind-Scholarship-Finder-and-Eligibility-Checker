"""Deterministic scholarship eligibility rules; no LLM decides eligibility."""
def evaluate(scholarship, student):
    reasons=[]
    for field in ('min_marks','max_income'):
        if field not in student or student[field] is None:
            reasons.append(f'Missing student value: {field}')
    if reasons: return {'status':'Needs review','reasons':reasons}
    if float(student['min_marks']) < scholarship['min_marks']:
        reasons.append('Marks below minimum')
    if float(student['max_income']) > scholarship['max_income']:
        reasons.append('Income above maximum')
    if scholarship['category'] != 'Any' and student.get('category') != scholarship['category']:
        reasons.append('Category requirement not met')
    return {'status':'Not eligible' if reasons else 'Eligible','reasons':reasons or ['All listed rules satisfied']}

def checklist(scholarship):
    return ['Identity proof','Marks card','Income certificate'] + (['Category certificate'] if scholarship['category'] != 'Any' else [])
