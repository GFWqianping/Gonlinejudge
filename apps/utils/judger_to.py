import requests, ranged_response

from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf

base_url = 'http://127.0.0.1'
submission_url = base_url+'/api/submission'
profile_url = base_url+'/api/profile'
login_url = base_url+'/api/login'
status_url = submission_url+'s?myself=0&result=&username=&page=1&limit=5&offset=0'
user = 'qqq'
password = '123456'


def get_csrftoken():
    resp = requests.get(profile_url)
    cookie = resp.headers.get('Set-Cookie')
    return cookie[10:74]


def set_csrftoken():
    session = requests.session()
    session.get(profile_url)
    session.headers['x-csrftoken'] = session.cookies['csrftoken']
    return session


header = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Cookie': 'ga=GA1.1.1699501325.1557720391; gid=GA1.1.418151590.1557843854; sessionid=912ng3gwmxiccvzdnv93ujsdezlk517a;',
}


def login_judge(user=user, password=password):
    data = {"username": user, "password": password}
    s = set_csrftoken()
    res = s.post('http://127.0.0.1/api/login', json=data)
    set_cookie = res.headers.get('Set-Cookie')
    session_id = find_session_id(set_cookie)
    session = set_csrftoken()
    session.cookies['sessionid'] = session_id
    return session


def find_session_id(set_cookie):
    index = set_cookie.find('sessionid')
    sc = set_cookie[index:]
    cookie_list = sc.split(';')
    s_id = cookie_list[0].split('=')[1]
    return s_id


def code_to_judger(problem_id, language, code):

    data = {
        "problem_id": problem_id,
        "language": language,
        "code": code
    }
    session = login_judge()
    resp = session.post(url=submission_url, data=data, json=True)
    return resp


def get_results(id):
    session = login_judge()
    re = session.get(status_url)
    all_submittions = re.json().get('data').get('results')
    for sub in all_submittions:
        if id == sub.get('id'):
            return sub
    return {'error': '没有找到此提交记录'}

