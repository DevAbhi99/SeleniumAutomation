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

def testupdateData():
    payload={"id":2, "name":"Mohan", "age":24}
    client.post('/sendData', json=payload)

    updatedPayload={"id":2, "name":"Rajesh", "age":24}
        
    response=client.put('/updateData/1', json=updatedPayload)

    body1=response.json()

    assert response.status_code==200

    response2=client.get('/getData')

    body2=response2.json()

    assert response2.status_code==200

    assert body1["message"]=="Data updated Successfully"

    assert body2[1]["id"]==2
    assert body2[1]["name"]=="Rajesh"
    assert body2[1]["age"]==24


def testDeleteData():

     payload={"id":2, "name":"Mohan", "age":24}
     client.post('/sendData', json=payload)

     response=client.request("DELETE", "/deleteData", json=payload)

     assert response.status_code==200

     body=response.json()

     assert body["message"]=='Data deleted successfully'

    
def testClearData():

    response=client.delete('/clearData')

    body=response.json()

    assert response.status_code==200

    assert body["message"]=="Data cleared successfully"






