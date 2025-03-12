from collections import Counter
import matplotlib.pyplot as plt
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

failedcallstotal = (sum(1 for cdr in cdrs if cdr["status"]== "failed"))
failedcallsperc = failedcallstotal*100/len(cdrs)
failedcallsordered = Counter(cdr["callee"] for cdr in cdrs if cdr["status"]=="failed")
failedcallsperextpect = {key: (int(value)*100/failedcallstotal) for key, value in failedcallsordered.items()}
print (failedcallsperextpect)

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
