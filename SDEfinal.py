import json
from urllib.request import urlopen

file = urlopen('https://int.nyt.com/applications/elections/2020/data/api/2020-02-03/precincts/IowaDemPrecinctsSFTP-latest.json')
data = json.load(file)
weird = []

# checks if any candidate who received less final votes than another candidate received more SDEs than that candidate
# the final parenthis value is the index in the NYTimes json
for i, precinct in enumerate(data['precincts']):
    pname = precinct['precinct']
    lname = precinct['locality_name']
    id = precinct['precinct_id']
    # first = sum(precinct['results_align1'].values())
    final = [(key, val) for (key, val) in precinct['results_alignfinal'].items()]
    result = [(key, val) for (key, val) in precinct['results'].items()]
    #final.sort(key=lambda tup: tup[1])
    #result.sort(key=lambda tup: tup[1])
    incorrect = set()
    for j in range(len(final)):
        for k in range(len(final)):
            if final[j][1] < final[k][1] and result[j][1] > result[k][1]:
                incorrect.add(f'{result[j][0]} (f: {final[j][1]}, sde: {result[j][1]})')
                incorrect.add(f'{result[k][0]} (f: {final[k][1]}, sde: {result[k][1]})')
    if len(incorrect) > 0:
        s = f'{pname} ({lname}, {id}), incorrect: {incorrect} --> ({i})'
        weird.append(s)

print(f'SDE and final aligment discrepancy (amount: {len(weird)}):')
for s in weird:
    print(s)