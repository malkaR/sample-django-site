import urllib
import random
import json

base_url = 'https://www.google.com/s?'
static_params = {'gs_rn' : 47,
'gs_ri' : 'psy-ab',
 'tok' : '9vWVlgfBdMD1NDCOlxQP2Q',
 'xhr' : 't',
 'q' : '', # google query string
 'es_nrs' : 'true',
 'pf' : 'p',
 'sclient' : 'psy-ab',
 'oq' : '',
 'gs_l' : '',
 'pbx' : 1,
 'bav' : 'on.2,or.r_qf.',
 'bvm' : 'bv.69411363,d.cWc',
 'fp' : '57e63ef4dc36f453',
 'biw' : 1440,
 'bih' : 412,
 'tch' : 1,
 'psi' : 'k3SjU4SrEsHJsQSMnYDICg.1403221140124.1'
}
suggest_params = {'pq' : '', # google search prefix for auto-suggest, for ex: why%20is%20it
}
# variable_params = {'cp' : [6, 11],
#  'gs_id' : ['4ll', '5fy'], 
#  'ech' : [42, 47] 
#  }
variable_params = {'cp' : 6,
 'gs_id' : '4ll', 
 'ech' : 42,
 }

def encode_query(query_terms):
 	if isinstance(query_terms, list):
 		query_terms = '%20'.join(query_terms)
 	elif isinstance(query_terms, str):
 		query_terms = query_terms.replace(' ', '%20')
 	suggest_params['pq'] = query_terms
 	final_query_params = {}
 	final_query_params.update(static_params)
 	final_query_params.update(suggest_params)
 	final_query_params.update(variable_params)
 	# for key, val in variable_params.items():
 	# 	final_query_params[key] = random.choice(val)
 	# print final_query_params
 	return urllib.urlencode(final_query_params)

def download_suggestions(query_terms):
	print base_url + encode_query(query_terms)
 	file_handle = urllib.urlopen(base_url + encode_query(query_terms))
 	json_content = json.loads(file_handle.read()[0:-6])
 	# print json_content
 	return json_content

 
 
 
 
