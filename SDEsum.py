import json
from urllib.request import urlopen

file = urlopen('https://int.nyt.com/applications/elections/2020/data/api/2020-02-03/precincts/IowaDemPrecinctsSFTP-latest.json')
data = json.load(file)
weird = []

# checks if precinct SDE sum does not equal the distributed SDEs
# the final parenthis value is the index in the NYTimes json
for i, precinct in enumerate(data['precincts']):
    pname = precinct['precinct']
    lname = precinct['locality_name']
    id = precinct['precinct_id']
    result_sum = sum(precinct['results'].values())
    votes = float(precinct['votes'])
    if not result_sum == votes:
        s = f'{pname} ({lname}, {id}), result_sum: {result_sum}, votes: {votes} --> ({i})'
        weird.append(s)

print(f'SDE and final aligment discrepancy (amount: {len(weird)}):')
for s in weird:
    print(s)