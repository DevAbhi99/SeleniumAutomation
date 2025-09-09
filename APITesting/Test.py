from fastapi.testclient import TestClient
from Main import api

client=TestClient(api)


#Testing get method
def testgetData():
    response=client.get('/getData')

    assert response.status_code==200

    body=response.json()

    assert body[0]["id"]==1
    assert body[0]["name"]=='Subhayan'


#testing post method

def testsentData():

    payload={"id":2, "name":"Mohan", "age":24}

    response=client.post('/sendData', json=payload)

    assert response.status_code==200

    body=response.json()

    assert body["message"]=="Successfully inserted the data"

    response2=client.get('/getData')

    body2=response2.json()

    assert body2[1]['id']==2
    assert body2[1]['name']=='Mohan'
    assert body2[1]['age']==24