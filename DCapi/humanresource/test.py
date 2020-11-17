import json,os
datadir=r'G:/Users/36357/PycharmProjects/DCapi/DCapi/humanresource/data/'

def get():
    with open(datadir+r'bt.json','r') as f:
        d=json.load(f)
        return d
def post(l):
    res=[]
    with open(datadir+r'bt.json','r') as f:
        try:
            content=json.load(f)
        except Exception:
            content=[]
        if isinstance(content,list):
            content.extend(l)
            res=content
        elif isinstance(content,dict):
            res.append(content)
            res.extend(l)
    with open(datadir+r'bt.json','w') as f1:
        json.dump(res,f1,sort_keys=True)
if __name__=='__main__':

    l=[{"id":2,"name":"test","password":"123","a":"23"},]
    print(len(l))
    post(l)
    print(get())