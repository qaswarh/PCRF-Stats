import csv
import re
import tabulate
with open('bulkpcrf.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    table = list()
    for line in csv_reader:
        st1 = '0' or '0.0'                      #if you want to ignore null records
        st2 = 'AAR'                             #KPI, as per need change to other diameter cmds, cpu, memory etc.
        st3 = re.sub('.*f01-', '', line[1])     #re was imported to hide some info, otherwise st3 = line[1]
        st4 = line[2]
        st5 = line[3]
        tr = [st3, st4, st5]
        headers = ['Server','KPI','value']
        if st2 in line[2]:
            if st1 not in line[3]:
                table.append(tr)
    print(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
