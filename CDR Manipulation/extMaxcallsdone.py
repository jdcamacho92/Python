#Tienes el mismo dataset cdrs, pero ahora debes enfocarte en la duración de las llamadas.
#2️⃣ Encuentra el promedio de duración de llamadas por estado ("completed" vs "failed").
#3️⃣ Grafica un histograma con la distribución de duración de llamadas.
#Extra: Si quieres más dificultad, agrupa las duraciones en intervalos (bins) de 30 segundos en el histograma.



#Tienes el mismo dataset cdrs, pero ahora debes enfocarte en la duración de las llamadas.
#2️⃣ Encuentra el promedio de duración de llamadas por estado ("completed" vs "failed").
#3️⃣ Grafica un histograma con la distribución de duración de llamadas.
#Extra: Si quieres más dificultad, agrupa las duraciones en intervalos (bins) de 30 segundos en el histograma.
from collections import defaultdict
import matplotlib.pyplot as plt
from collections import Counter

cdrs = [
    {"caller": "1001", "callee": "2001", "duration": 120, "status": "completed", "timestamp": "14:23:45"},
    {"caller": "1001", "callee": "2002", "duration": 45, "status": "failed", "timestamp": "14:45:12"},
    {"caller": "1002", "callee": "2004", "duration": 75, "status": "failed", "timestamp": "15:10:33"},
    {"caller": "1002", "callee": "1001", "duration": 120, "status": "failed", "timestamp": "15:50:22"},
    {"caller": "1002", "callee": "2007", "duration": 50, "status": "failed", "timestamp": "16:05:17"},
    {"caller": "1001", "callee": "2007", "duration": 50, "status": "failed", "timestamp": "16:05:17"},
    {"caller": "2002", "callee": "2007", "duration": 50, "status": "failed", "timestamp": "16:05:17"},
    {"caller": "2002", "callee": "2007", "duration": 50, "status": "failed", "timestamp": "16:05:17"},
    {"caller": "1002", "callee": "2007", "duration": 50, "status": "failed", "timestamp": "16:05:17"},
]
# 📊 Cantidad de llamadas por cada caller
callsperextension = defaultdict(int)
for x in cdrs:
    callsperextension[x["callee"]] += 1
    callsperextension[x["caller"]] += 1
max_calls = max(callsperextension.values())
print(callsperextension.items() )
top_extensions = [ext for ext, count in callsperextension.items() if count == max_calls]
print(f"Extensiones con más llamadas ({max_calls} llamadas): {', '.join(top_extensions)}")
print (top_extensions)

topextensions=dict(sorted(callsperextension.items(), key=lambda x: x[1], reverse=True)[:3])
print (topextensions)

print ("Top 3 de extensiones con mas llamadas")
for ext, calls in topextensions.items():
    print (f"extension: {ext} -  Llamadas {calls}")

# top 3 de extensiones con mas llamadas
extensiones = list(topextensions.keys()) # Asegurar que las horas estén en orden
print (extensiones)
cantidad_llamadas = [topextensions[h] for h in topextensions]

plt.bar(extensiones, cantidad_llamadas, color="red", edgecolor="black")

plt.xlabel("Extensión")
plt.ylabel("Cantidad de llamadas")
plt.title("top 3 extensiones con mas llamadas")


plt.show()