import requests

url = 'https://randomuser.me/api/?results=100&nat=US'
response = requests.get(url)

with open(f'users.txt', 'w') as f:
    if response.status_code == 200:
        data = response.json()

        for item in data['results']:
            nombres = item['name']['first'] + " " + item['name']['last']
            f.write(f'insert into personas values(\'{nombres}\')\n')
            
            
    else:
        print('Error al obtener los datos')