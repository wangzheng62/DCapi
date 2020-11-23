import json,os
datadir=r'G:/Users/36357/PycharmProjects/DCapi/DCapi/humanresource/data/'
#查询

def __open(file,conditions=None,**kw):
    table=[]
    res=[]
    with open(datadir+file,'r') as f:
        try:
            table=json.load(f)
        except Exception as e:
            print("json格式不对")

        if isinstance(table,list):
            if conditions is None:
                res=table
            else:
                for d in table:
                    if conditions.items() <= d.items():
                        res.append(d)
        else:
            print('json格式不对')
        return res
def query(file,conditions=None,**kw):
    table=[]
    res=[]
    with open(datadir+file,'r') as f:
        try:
            table=json.load(f)
        except Exception as e:
            print("json格式不对")

        if isinstance(table,list):
            if conditions is None:
                res=table
            else:
                for d in table:
                    if conditions.items() <= d.items():
                        res.append(d)
        else:
            print('json格式不对')
        return res

def insert(file,l,**kw):
    table=[]
    with open(datadir+file,'r') as f:
        try:
            table=json.load(f)
        except Exception as e:
            print("json格式不对")

        if isinstance(table,list):
            table.extend(l)
        else:
            print('json格式不对')
            return False
    with open(datadir+file,'w') as f1:
        json.dump(table,f1)
    return True
def update(file,conditions=None,**kw):
    table=[]
    res=[]
    with open(datadir+file,'r') as f:
        try:
            table=json.load(f)
        except Exception as e:
            print("json格式不对")

        if isinstance(table,list):
            if conditions is None:
                res=table
            else:
                for d in table:
                    if conditions.items() <= d.items():
                        res.append(d)
        else:
            print('json格式不对')
        return res

def delete(file,conditions=None,**kw):
    table=[]
    res=[]
    with open(datadir+file,'r') as f:
        try:
            table=json.load(f)
        except Exception as e:
            print("json格式不对")

        if isinstance(table,list):
            if conditions is None:
                res=table
            else:
                print(table)
                for index,d in enumerate(table):
                    if conditions.items() <= d.items():
                        pass
                    else:
                        res.append(d)
        else:
            print('json格式不对')
    with open(datadir+file,'w') as f1:
        json.dump(res,f1)
    return True


if __name__=='__main__':

    l=[{"id":3,"name":"test","password":"123","a":"23"},]
    delete('test.json',conditions={"id":"2"})
    insert('test.json',l)