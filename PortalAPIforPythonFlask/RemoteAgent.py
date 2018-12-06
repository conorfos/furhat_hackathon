'''
    Author: Kyusong Lee
    email: kyusongl@cs.cmu.edu
    Date created: 09/21/2017
    Date last modified: 09/21/201
    Description: An Example code for DialPort Connection
    Python Version: 2.7
'''

import wolframalpha
import json

def resolveListOrDict(variable):
    if isinstance(variable, list):
        return variable[0]['plaintext']
    else:
        return variable['plaintext'] 

class API(object):
    def __init__(self):
        self.history = []
        self.wolfram_client = wolframalpha.Client("7WVQTR-9R6AG9UYGJ")   
    
    def GetResponse(self,text):
        res = self.wolfram_client.query(text)
        pod = res['pod'][1]
        result = resolveListOrDict(pod['subpod'])
        print(result)
        #print str(pod)
        slu = {"act":"dialog_act","slot":"named_entity"} 
        sysUtter = result
        imageurl = "imageurl"
        return {"slu":slu,"sys":sysUtter,"imageurl":imageurl} 
