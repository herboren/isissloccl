import json, requests, re

class IssLocation():    
    def GetIssLocation():
        isslocurl = 'http://api.open-notify.org/iss-now.json'
        response = requests.get(isslocurl)
        issjson = json.loads(response.text)
        for key, value in issjson.items():
            if key in 'iss_position':                
                rgx_longlat = re.sub('[A-Za-z]|[^\w+\.\,\-]','', str(value))                 
                issloc = (rgx_longlat.split(',')[0], rgx_longlat.split(',')[1])   
                
        return issloc