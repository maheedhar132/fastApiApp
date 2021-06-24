from fastapi import FastAPI
import requests
import json

app=FastAPI()

@app.get('/groups')
def masterList(masterName):
    url = 'https://mobius-test.nat.bt.com/cjoc/job/'+masterName.lower()+'/groups/api/json'
    querystring = {"tree":"groups[name]"}

    headers = {
        'authorization': "Basic NjEzMzk0ODYyOjExMWRkODU3ZDk2ZDA0M2ZlZDYzY2RkN2Y2NGRmNjJlNWY=",
        'cache-control': "no-cache"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonList=json.loads(response.text)
    return jsonList["groups"]
#Add Users to groups
@app.post('/addMembers')
async def addUser(masterName,group,ein):
    url = "https://mobius-test.nat.bt.com/cjoc/job/"+masterName.lower()+"/groups/"+group.lower()+"/addMember"
    headers = {
    'authorization': "Basic NjEzNDI2MjI4OjExZjlkMzViMGY1Zjg2YWYxZmE0ODRkYWI4NWJkZTRmYjc=",
    'cache-control': "no-cache"}
    eins=ein.split(';')
    i=0
    for number in eins:
        querystring = {'name':number}
        response = requests.request("POST", url, headers=headers, params=querystring)
        i+=1
    if(i==len(eins)):
        return 200
    else:
        return 400
        
@app.post('/createGroup')
def createGroup(masterName,groupName):
    url="https://mobius-test.nat.bt.com/cjoc/job/"+masterName+"/groups/createGroup"
    headers = {
    'authorization': "Basic NjEzNDI2MjI4OjExZjlkMzViMGY1Zjg2YWYxZmE0ODRkYWI4NWJkZTRmYjc=",
    'cache-control': "no-cache"}
    querystring = {'name':groupName}
    response = requests.request("POST",url,headers=headers,params=querystring)
    return response.text
@app.delete('/removeMember')
async def removeUser(masterName,group,ein):
    url = "https://mobius-test.nat.bt.com/cjoc/job/"+masterName.lower()+"/groups/"+group.lower()+"/removeMember"
    headers = {
    'authorization': "Basic NjEzNDI2MjI4OjExZjlkMzViMGY1Zjg2YWYxZmE0ODRkYWI4NWJkZTRmYjc=",
    'cache-control': "no-cache"}
    eins=ein.split(';')
    i=0
    for number in eins:
        querystring = {'name':number}
        response = requests.request("POST", url, headers=headers, params=querystring)
        i+=1
    if(i==len(eins)):
        return 200
    else:
        return 400
@app.delete('/deleteGroup')
def deleteGroup(masterName,groupName):
    url="https://mobius-test.nat.bt.com/cjoc/job/"+masterName+"/groups/deleteGroup"
    headers = {
    'authorization': "Basic NjEzNDI2MjI4OjExZjlkMzViMGY1Zjg2YWYxZmE0ODRkYWI4NWJkZTRmYjc=",
    'cache-control': "no-cache"}
    querystring = {'name':groupName}
    response = requests.request("POST",url,headers=headers,params=querystring)
    return response.text
