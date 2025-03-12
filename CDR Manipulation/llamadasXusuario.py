import csv
import statistics
from collections import Counter
from collections import OrderedDict
 

# Leer el archivo CSV
with open("cdrs.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    cdrs = [row for row in reader]

# Convertir 'duration' a enteros
for cdr in cdrs:
    cdr["duration"] = int(cdr["duration"])



# 📊 Cantidad de llamadas por cada caller
caller_counts = Counter(cdr["caller"] for cdr in cdrs)

print (caller_counts)
ordered=(dict(sorted(caller_counts.items(), key=lambda item: item[1], reverse=True,)))
print(ordered)
