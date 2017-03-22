use of api as follows
url = "http://192.168.33.10/api/test"
res = requests.get(url)
res.json()
output:
{u'num_results': 47,
 u'objects': [{u'data': u'2017-03-21 16:42:12', u'id': 1},
  {u'data': u'2017-03-21 16:43:23', u'id': 2},
  {u'data': u'2017-03-21 16:43:24', u'id': 3},
  {u'data': u'2017-03-21 16:43:25', u'id': 4},
  {u'data': u'2017-03-21 16:43:26', u'id': 5},
  {u'data': u'2017-03-21 16:43:28', u'id': 6},
  {u'data': u'2017-03-21 16:43:28', u'id': 7},
  {u'data': u'2017-03-21 16:43:37', u'id': 8},
  {u'data': u'2017-03-21 16:43:40', u'id': 9},
  {u'data': u'2017-03-21 16:44:03', u'id': 10}],
 u'page': 1,
 u'total_pages': 5}


d = {'data': {'real':'1'}}

res = requests.post(url, data=json.dumps(d),headers={'Content-Type': 'application/json'})
res.json()
output:
{u'data': {u'real': u'1'}, u'id': 48}

