import requests
import json

base_url = 'https://www.google.com/s'

# Working query examples to compare:
# https://www.google.com/s?gs_ri=psy-ab&xhr=t&q=the%20reason&es_nrs=true&pf=p&sclient=psy-ab&oq=&gs_l=&pbx=1&bav=on.2,or.r_qf.&tch=1
# https://www.google.com/s?gs_ri=psy-ab&xhr=t&q=the%20reason&pq=the%20reason&es_nrs=true&pf=p&sclient=psy-ab&oq=&gs_l=&pbx=1&bav=on.2,or.r_qf.&tch=1

static_params = {
    'gs_ri' : 'psy-ab',
    'xhr' : 't',
    'es_nrs' : 'true',
    'pf' : 'p',
    'sclient' : 'psy-ab',
    'oq' : '',
    'gs_l' : '',
    'pbx' : 1,
    'bav' : 'on.2,or.r_qf.',
    'tch' : 1,
}

optional_params = {
    'pq' : '', # google query string
}
suggest_params = {
    'q' : '', # google search prefix for auto-suggest, for ex: why%20is%20it
}


def get_query_params(query_terms):
    """format the search terms in to google get request parameters"""
    if isinstance(query_terms, list):
        query_terms = '%20'.join(query_terms)
    elif isinstance(query_terms, str):
        query_terms = query_terms.replace(' ', '%20')
    suggest_params['q'] = query_terms
    final_query_params = {}
    final_query_params.update(static_params)
    final_query_params.update(suggest_params)
    return final_query_params

def download_suggestions(query_terms):
    """access the google url and convert the response to json"""
    proxies = { "http": "proxy_server:proxy_port"}
    resp = requests.get(base_url, params=get_query_params(query_terms), proxies=proxies)
    content_text = resp.text[0:-6]
    return (json.loads(json.loads(content_text)['d']))[1]





