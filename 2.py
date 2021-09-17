import requests
resp = requests.get("https://xmn.tuit.uz/education/tasks",params = {"id":"424"})
print(resp.url)
