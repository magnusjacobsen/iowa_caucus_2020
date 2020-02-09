import json
from urllib.request import urlopen

file = urlopen('https://int.nyt.com/applications/elections/2020/data/api/2020-02-03/precincts/IowaDemPrecinctsSFTP-latest.json')
data = json.load(file)
weird = []

# checks if any candidate have more first than final alignments, which are not 0 (ie. if viable candidates lost votes somehow)
# and the candidate still received SDEs (note: I'm not checking other viability indicators)
# the final parenthis value is the index in the NYTimes json
for i, precinct in enumerate(data['precincts']):
    pname = precinct['precinct']
    lname = precinct['locality_name']
    id = precinct['precinct_id']
    first = [(k,v) for (k,v) in precinct['results_align1'].items()]
    final = [(k,v) for (k,v) in precinct['results_alignfinal'].items()]
    result = [(k,v) for (k,v) in precinct['results'].items()]
    incorrect = []

    for j in range(len(final)):
        if first[j][1] > final[j][1] and result[j][1] > 0:
            incorrect.append(f'{first[j][0]} (fst: {first[j][1]}, fin: {final[j][1]}, sde: {result[j][1]})')
    if len(incorrect) > 0:
        s = f'{pname} ({lname}, {id}), incorrect: {incorrect} --> ({i})'
        weird.append(s)

print(f'fewer final than first alignments for a candidate receiving SDEs (amount: {len(weird)}):')
for s in weird:
    print(s)
