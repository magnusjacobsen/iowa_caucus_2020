import json
from urllib.request import urlopen

file = urlopen('https://int.nyt.com/applications/elections/2020/data/api/2020-02-03/precincts/IowaDemPrecinctsSFTP-latest.json')
data = json.load(file)
weird = []

# checks if any precincts have fewer first than final alignments
# the final parenthis value is the index in the NYTimes json
for i, precinct in enumerate(data['precincts']):
    pname = precinct['precinct']
    lname = precinct['locality_name']
    id = precinct['precinct_id']
    first = sum(precinct['results_align1'].values())
    final = sum(precinct['results_alignfinal'].values())
    if first < final:
        s = f'{pname} ({lname}, {id}), first: {first}, final: {final} --> ({i})'
        weird.append(s)

print(f'fewer first than final alignments (amount: {len(weird)}):')
for s in weird:
    print(s)
