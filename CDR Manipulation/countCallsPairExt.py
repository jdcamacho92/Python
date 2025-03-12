# Tareas
# 1️⃣ Cuenta cuántas veces ha ocurrido cada par de llamadas (independientemente de la dirección).
# 2️⃣ Encuentra el par con más llamadas.
# 3️⃣ Grafica un top 5 de los pares con más llamadas en un gráfico de barras.
# 🚀 Extra: Si hay empates, muestra todos los pares con la máxima cantidad de llamadas.
# Ejemplo de salida esperada:
# Par con más llamadas: ('1001', '2002') con 5 llamadas
# y un gráfico con los 5 pares más frecuentes.
from collections import Counter
from collections import OrderedDict
from collections import Counter
import matplotlib.pyplot as plt
cdrs = [
    {"caller": "1001", "callee": "2002", "duration": 120, "status": "completed", "timestamp": "14:23:45"},
    {"caller": "2002", "callee": "1001", "duration": 45, "status": "completed", "timestamp": "14:45:12"},
    {"caller": "1001", "callee": "2003", "duration": 75, "status": "failed", "timestamp": "15:10:33"},
    {"caller": "1003", "callee": "2001", "duration": 10, "status": "failed", "timestamp": "15:50:22"},
    {"caller": "1001", "callee": "2002", "duration": 50, "status": "completed", "timestamp": "16:05:17"},
    {"caller": "1002", "callee": "1001", "duration": 90, "status": "completed", "timestamp": "16:20:30"},
    {"caller": "1001", "callee": "2003", "duration": 30, "status": "completed", "timestamp": "16:40:10"},
    {"caller": "2003", "callee": "1001", "duration": 20, "status": "failed", "timestamp": "17:00:45"},
    {"caller": "1001", "callee": "2002", "duration": 60, "status": "completed", "timestamp": "17:15:25"},
    {"caller": "1003", "callee": "1001", "duration": 35, "status": "failed", "timestamp": "17:35:50"},
    {"caller": "1001", "callee": "1006", "duration": 40, "status": "completed", "timestamp": "17:50:05"},
]

# 1️⃣ Cuenta cuántas veces ha ocurrido cada par de llamadas (independientemente de la dirección).
dupladellamadas = Counter(tuple(sorted((cdr["caller"], cdr["callee"]))) for cdr in cdrs)
#print (dupladellamadas)
#print (dupladellamadas.get)
# 2️⃣ Encuentra el par con más llamadas.
duplawithmorecalls= max(dupladellamadas, key=dupladellamadas.get)
max_calls = dupladellamadas[duplawithmorecalls]
#print(f"El par con más llamadas es {duplawithmorecalls} con {max_calls} llamadas.")

# 3️⃣ Grafica un top 5 de los pares con más llamadas en un gráfico de barras.

topduplas=dict(sorted(dupladellamadas.items(), key=lambda x: x[1], reverse=True)[:3])
#print (f"las 3 duplas con mas llamadas son {topduplas}")
#datos

extensiones = [f"{par[0]} ↔ {par[1]}" for par in topduplas.keys()]
print (extensiones)
numllamadas = list(topduplas.values())  # porcentaje de llamadas
print (numllamadas)
# Crear gráfico de barras
plt.bar(extensiones, numllamadas, color="red", edgecolor="black")
# Rotar etiquetas del eje X para mejor visualización
plt.xticks(rotation=45, ha="right")
# Etiquetas y título
plt.xlabel("Extensión")
plt.ylabel("numero de llamadas")
plt.title("dupla de extensiones extensión")
# Mostrar gráfico
plt.show()
