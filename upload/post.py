import requests
import json
import sys


url='http://127.0.0.1:8000/upload/up/'


f=open('.report.json')
data=json.load(f)
Username=sys.argv[1]
Password=sys.argv[2]
created_at=sys.argv[3]
project_name=sys.argv[4]
print(data.keys())
datasend={'created_at':created_at,
          'plat_form':data['environment']['Platform'],
          'python':data['environment']["Python"],
          'project_name':project_name,
          'tests':[]}
for row in data['tests']:
    test_name=row['nodeid']
    duration=row['setup']['duration']+row['call']['duration']+row['teardown']['duration']
    test_outcome=row['outcome']
    longrep=''
    if test_outcome=='failed':
        longrep=row['call']['longrepr']
    entry={'test_name':test_name,'duration':duration,'test_outcome':test_outcome,'longrep':longrep}
    datasend['tests'].append(entry)
    

x=requests.post(url,json=datasend,headers={'Referer':url,'Username':str(Username),'Password':str(Password)})



print(x.text)
