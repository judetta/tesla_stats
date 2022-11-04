from fetch_stats import get_tesla_stats

stats = get_tesla_stats()
success = isinstance(stats, dict)

if success:
    print('Suomessa:', stats['finland'])
    print('Jyväskylässä:', stats['jyvaskyla'])
    print('Päivitetty:', stats['updated'])
else:
    print('Error', stats)
