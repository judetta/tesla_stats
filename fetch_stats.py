import requests
import json

def get_tesla_stats():
    """Get the count of Teslas registered and in use in Finland and in Jyväskylä
    
    Data source: https://trafi2.stat.fi/PXWeb/pxweb/fi/TraFi/TraFi__Liikennekaytossa_olevat_ajoneuvot/010_kanta_tau_101.px/
    """

    url = 'https://trafi2.stat.fi:443/PXWeb/api/v1/fi/TraFi/Liikennekaytossa_olevat_ajoneuvot/010_kanta_tau_101.px'
    with open('query.json', encoding='utf-8') as qfile:
        query = qfile.read()

    query = json.loads(query)
    response = requests.post(url, json=query)
    if response.status_code != 200:
        return response.status_code
    else:
        response = response.json()
        finland = response['value'][0]
        jyvaskyla = response['value'][1]
        updated = response['updated'].split('T')[0]
        return {'finland': finland, 'jyvaskyla': jyvaskyla, 'updated': updated}
