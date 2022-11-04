#!/usr/bin/python3

import requests
import json

def get_tesla_stats():
    """Get the count of Teslas registered and in use in Finland and in Jyväskylä
    
    Data source: https://trafi2.stat.fi/PXWeb/pxweb/fi/TraFi/TraFi__Liikennekaytossa_olevat_ajoneuvot/010_kanta_tau_101.px/
    """

    url = 'https://trafi2.stat.fi:443/PXWeb/api/v1/fi/TraFi/Liikennekaytossa_olevat_ajoneuvot/010_kanta_tau_101.px'
    query = '{"query": [{"code": "Alue", "selection": {"filter": "item", "values": ["MA1", "KU179"]}}, {"code": "Merkki", "selection": {"filter": "item", "values": ["2055"]}}, {"code": "Käyttöönottovuosi", "selection": {"filter": "item", "values": ["YH"]}}, {"code": "Käyttövoima", "selection": {"filter": "item", "values": ["YH"]}}], "response": {"format": "json-stat2"}}'

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

stats = get_tesla_stats()
success = isinstance(stats, dict)

### Actual HTML page content starts here ###
print("Content-type: text/html;charset=utf-8")
print("")
print('<html>')
print('<head>')
print('<title>Tesla Stats</title>')
print('<meta charset="utf-8">')
print('<meta name="robots" content="noindex">')
print('<meta name="author" content="Jutta Hänninen">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="styles/style.css">')
print('<link rel="shortcut icon" href="favicon.ico">')
print('</head>')
print('<body class="snippet">')
print('<p>Count of registered Teslas</p>')
if success:
    print('<ul>')
    print('<li>')
    print('in Finland:', stats['finland'])
    print('</li>')
    print('<li>')
    print('in Jyväskylä:', stats['jyvaskyla'])
    print('</li>')
    print('</ul>')
    print('<p style="font-size: small;">')
    print('Source: Traficom Passenger cars in traffic by area, updated on', stats['updated'])
    print('</p>')
else:
    print('<p>')
    print('Could not get data - error', stats)
    print('</p>')
print('</body>')
print('</html>')