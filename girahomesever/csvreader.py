import csv
import sys
from datetime import datetime
from bunch import Bunch

def parseCSV(filename):

    with file(filename) as fp:
        reader = csv.reader(fp, delimiter=';')
        rows = list()
        column_names = list()
        for rownum, line in enumerate(reader):
            if not line:
                continue
            if rownum == 0:
                column_names = line
            else:
                row_data = dict()
                for idx, value in enumerate(line):
                    row_data[column_names[idx]] = value
                row_data['date'] = datetime.strptime(row_data['Datum+Uhrzeit'], '%d.%m.%Y %H:%M:%S')                    
                print row_data
                rows.append(row_data)
        return rows
if __name__ == '__main__':
    result = parseCSV(sys.argv[1])
    import pdb; pdb.set_trace() 
