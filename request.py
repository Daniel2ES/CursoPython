import requests
r = requests.get('https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d', auth=('user', 'pass'))
r.status_code