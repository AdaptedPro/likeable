import json
import requests

class couchdb():
    url     = 'https://adaptedpro.iriscouch.com/user_images/'
    payload = '';
    
    def create_db_document(self):
        payload = self.payload
        url     = self.url
        headers = {'content-type': 'application/json'}
        r       = requests.post(url, data=json.dumps(payload), headers=headers)
        if (r.status_code == 200):
            theJSON = json.loads(r.text)
            id      = theJSON['id']
            self.get_doc_image_by_id(id)
        else:
            return False    
            
    def get_doc_image_by_id(self,id):
        r = requests.get(self.url + id)
        if (r.status_code == 200):
            theJSON = json.loads(r.text)
            for key in theJSON['_attachments'].keys(): 
                image = key
            image_url = image
        else:
            return False
        
    def put_doc_attachment(self,id):
        url   = self.url
        files = {'file':open('test.jpg', 'rb')}
        r     = requests.post(url, files=files)
   
import requests    
url = 'https://adaptedpro.iriscouch.com/user_images/8908b0e8af1393872669f924d9001e70'
files = {'file': open('logo11w.png', 'rb')}
r = requests.post(url, files=files)
print(r.text)        