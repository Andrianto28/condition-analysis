import requests

url = 'http://127.0.0.1:5000/api'

r = requests.post(url, json={'income': 0.91, 'credit limit':0.91, 'operating expenses':0.92, 'revenue':1.05, 'regional conditions individual':1.00, 'road type business': 0.00, 'criminal records':3.00, 'health records': 1.00, 'market share category':0.00, 'market growth':2.00, 'market trends':1.00, 'cash flow from operations category': 1.00, 'cash flow from investing category': 1.00, 'cash flow from financing category':1.00, 'gross profit margin category':1.00, 'net profit margin category':1.00, 'return on assets category': 0.00, 'credit history':1.00, 'management experience':0.00, 'customer acquisition costs category':2.00, 'customer retention rates category':0.00, 'collateral category':1.00, 'obsolescence rates category':1.00, 'account receiveable category':2.00, 'debt category':1.00, 'interest rates category':0.00, 'regulatory environment':2.00, 'marketing strategy': 2.00, 'geographic location':1.00})
print(r.json())