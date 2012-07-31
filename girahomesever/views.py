import os
import json
from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project':'GiraHomesever'}

@view_config(route_name='getData', renderer='json')
def getData(request):

    import csvreader
    result = dict()
    filename = os.path.join(os.path.dirname(__file__), 'waerme.csv')
    for d in csvreader.parseCSV(filename):
        for k,v in d.items():
            try:
                v = float(v)
            except ValueError:
                continue
            if not k in result:
                result[k] = list()
            result[k].append(float(v))

    return result
