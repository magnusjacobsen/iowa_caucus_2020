import json
from urllib.request import urlopen

file = urlopen('https://int.nyt.com/applications/elections/2020/data/api/2020-02-03/precincts/IowaDemPrecinctsSFTP-latest.json')
data = json.load(file)
weird = []

# checks if any two precincts have the exact same first and final alignment results
# if the total first alignments are larger than 10
# the final parenthis value is the index in the NYTimes json
for i, precinct1 in enumerate(data['precincts']):
    pname1 = precinct1['precinct']
    lname1 = precinct1['locality_name']
    id1 = precinct1['precinct_id']
    first1 = precinct1['results_align1']
    final1 = precinct1['results_alignfinal']
    for j, precinct2 in enumerate(data['precincts']):
        pname2 = precinct2['precinct']
        lname2 = precinct2['locality_name']
        id2 = precinct2['precinct_id']
        first2 = precinct2['results_align1']
        final2 = precinct2['results_alignfinal']
        if lname2 is not lname1 and id1 is not id2 and int(precinct2['votes_align1']) > 10:
            if first1 == first2 and final1 == final2:
                s = f'{pname1} ({lname1}, {id1}) AND {pname2} ({lname2}, {id2}) --> ({i}, {j})'
                sr = f'{pname2} ({lname2}, {id2}) AND {pname1} ({lname1}, {id1}) --> ({j}, {i})'
                if s not in weird and sr not in weird:
                    weird.append(s)

print(f'equal first and final alignments, with more than 10 caucus attendees (amount: {len(weird)}):')
for s in weird:
    print(s)
