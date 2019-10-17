import requests
import json
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=f18e09a0d563463e895b71796f23ea69')
response = requests.get(url).json()
content = json.dumps(response,indent = 4)
new2 = json.loads(content)

xyz=[]
newspaper=['author','title','description','url','content']
if new2["status"] == "ok":
        for x in new2['articles']:
                l =[]
                for key,values in x.items():

                    if key in newspaper:
                            l.append(values)
                xyz.append(l)            

