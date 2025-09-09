from fastapi.testclient import TestClient
from Main import api


client=TestClient(api)

def testGetData():
    response=client.get('/getData')

    assert response.status_code==200

    body=response.json()

    assert body[0]['id']==1
    assert body[0]['name']=='Subhayan'


def testSendData():

    payload={"id":3, "name":"Mohit", "age":24, "priority": 2}

    response=client.post('/sendData', json=payload)

    assert response.status_code==200

    body=response.json()

    assert body["message"]=="successfully inserted"

    response2=client.get('/getData')

    body2=response.json()

    assert body2[0]['id']==3
    assert body2[0]['name']=='Mohit'
    assert body2[0]['age']==24



