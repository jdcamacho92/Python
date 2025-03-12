from collections import Counter
import matplotlib.pyplot as plt
import collections, functools, operator
from collections import defaultdict
cdrs = [
    {"caller": "1001", "callee": "2001", "duration": 120, "status": "completed"},
    {"caller": "1001", "callee": "2002", "duration": 45, "status": "failed"},
    {"caller": "1003", "callee": "2004", "duration": 75, "status": "completed"},
    {"caller": "1002", "callee": "2004", "duration": 10, "status": "failed"},
    {"caller": "1001", "callee": "2007", "duration": 50, "status": "failed"},
    {"caller": "1003", "callee": "2006", "duration": 5, "status": "failed"},
    {"caller": "1001", "callee": "2007", "duration": 30, "status": "failed"},
    {"caller": "1002", "callee": "2007", "duration": 15, "status": "failed"},
    {"caller": "1003", "callee": "2007", "duration": 90, "status": "completed"},
]

#obtener  total de llamadas fallidas
failedcallstotal = (sum(1 for cdr in cdrs if cdr["status"]== "failed"))
#obtener % de llamadas fallidasd
failedcallsperc = failedcallstotal*100/len(cdrs)
#obtener cuantas llamadas fallidas hay por extension 
failedcallsordered = Counter(cdr["callee"] for cdr in cdrs if cdr["status"]=="failed")
#obtener % cuantas llamadas fallidas hay por extension 
failedcallsperextpect = {key: (int(value)*100/failedcallstotal) for key, value in failedcallsordered.items()}


##### calcular el promedio de duracion de llamadas fallidas ####
failedcallstotalduration = (sum(cdr["duration"] for cdr in cdrs if cdr["status"]== "failed"))
failedcallsavg = failedcallstotalduration/failedcallstotal if failedcallstotal > 0 else 0





#obtener la extension con la mayor duración total en llamadas fallidas.
failedcalls = [cdr for cdr in cdrs if cdr["status"]=="failed"]

failed_duration_per_callee = defaultdict(int)
for x in failedcalls:
    failed_duration_per_callee[x["callee"]] += x["duration"]


print (failed_duration_per_callee)
#failedcallsdict = {failedcalls["caller"]: failedcalls["duration"] for key, value in failedcalls}
#print (failedcallsdict)
#result = dict(functools.reduce(operator.add,map(collections.Counter, failedcalls)))
#print (result)



#datos
extensiones = list(failedcallsperextpect.keys())  # Extensiones
porcentajes = list(failedcallsperextpect.values())  # porcentaje de llamadas

# Crear gráfico de barras
plt.bar(extensiones, porcentajes, color="red", edgecolor="black")

# Etiquetas y título
plt.xlabel("Extensión")
plt.ylabel("porcentaje de llamadas")
plt.title("porcentaje de llamadas fallidas por extensión")

# Rotar etiquetas del eje X para mejor visualización
plt.xticks(rotation=50)

# Mostrar gráfico
plt.show()
