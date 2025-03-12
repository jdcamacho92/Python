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
    {"caller": "1002", "callee": "2007", "duration": 15, "status": "completed"},
    {"caller": "1003", "callee": "2007", "duration": 90, "status": "completed"},
]

topcallee = Counter(cdr["callee"] for cdr in cdrs)
maxcallee = (dict(sorted(topcallee.items(), key=lambda item: item[1], reverse=True)))
top1calle = max(maxcallee, key=maxcallee.get)

calleeswithmore1call = {key: value for key, value in maxcallee.items() if value > 1}
print(calleeswithmore1call)

#datos
extensiones = list(calleeswithmore1call.keys())  # Extensiones
cantidades = list(calleeswithmore1call.values())  # Cantidad de llamadas

# Crear gráfico de barras
plt.bar(extensiones, cantidades, color="skyblue", edgecolor="black")

# Etiquetas y título
plt.xlabel("Extensión")
plt.ylabel("Cantidad de llamadas")
plt.title("Cantidad de llamadas recibidas por extensión")

# Rotar etiquetas del eje X para mejor visualización
plt.xticks(rotation=45)

# Mostrar gráfico
plt.show()

#print (maxcallee)
#print (f"extension con mas llamadas: {top1calle}")
#print (f"numero de llamadas: {maxcallee[top1calle]}")
#print (f"Callee ordenados de mayor a menor: {calleeswithmore1call}")
