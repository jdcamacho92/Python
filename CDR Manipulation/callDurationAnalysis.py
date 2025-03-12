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
    {"caller": "1003", "callee": "2004", "duration": 75, "status": "failed", "timestamp": "15:10:33"},
    {"caller": "1002", "callee": "2004", "duration": 120, "status": "failed", "timestamp": "15:50:22"},
    {"caller": "1001", "callee": "2007", "duration": 50, "status": "failed", "timestamp": "16:05:17"},
]

#1️⃣ Encuentra la extensión (caller o callee) con la mayor duración total de llamadas (sumando todas sus llamadas).
durationperextension = defaultdict(int)
for x in cdrs:
    durationperextension[x["callee"]] += x["duration"]
    durationperextension[x["caller"]] += x["duration"]
max_extension = max(durationperextension, key=durationperextension.get)

print(f"La extensión con mayor duración total es {max_extension} con {durationperextension[max_extension]} segundos.")

#2️⃣ Encuentra el promedio de duración de llamadas por estado ("completed" vs "failed").
#obtener  total de llamadas fallidas
failedcallstotal = (sum(1 for cdr in cdrs if cdr["status"]== "failed"))
##### calcular el promedio de duracion de llamadas fallidas ####
failedcallstotalduration = (sum(cdr["duration"] for cdr in cdrs if cdr["status"]== "failed"))
failedcallsavg = failedcallstotalduration/failedcallstotal if failedcallstotal > 0 else 0


#obtener  total de llamadas completadas
completedcallstotal2 = (sum(1 for cdr in cdrs if cdr["status"]== "completed"))
##### calcular el promedio de duracion de llamadas fallidas ####
completedcallstotalduration2 = (sum(cdr["duration"] for cdr in cdrs if cdr["status"]== "completed"))

completedcallsavg2 = completedcallstotalduration2 /completedcallstotal2 if completedcallstotal2 > 0 else 0

print ("Promedio de duración de llamadas por estado:")
print (f"Failed: {failedcallsavg}")
print (f"Completed: {completedcallsavg2}")



#3️⃣ Grafica un histograma con la distribución de duración de llamadas.
#Extra: Si quieres más dificultad, agrupa las duraciones en intervalos (bins) de 30 segundos en el histograma.

# Separar duraciones por estado
durations_completed = [cdr["duration"] for cdr in cdrs if cdr["status"] == "completed"]
durations_failed = [cdr["duration"] for cdr in cdrs if cdr["status"] == "failed"]


# Crear histograma con colores diferentes
plt.hist(durations_completed, bins=range(0, max(durations_completed + durations_failed) + 30, 30),
         color="green", edgecolor="black", alpha=0.7, label="Completadas")
plt.hist(durations_failed, bins=range(0, max(durations_completed + durations_failed) + 30, 30),
         color="red", edgecolor="black", alpha=0.7, label="Fallidas")

# Etiquetas y título
plt.xlabel("Duración de llamadas (segundos)")
plt.ylabel("Cantidad de llamadas")
plt.title("Distribución de duración de llamadas")
plt.legend()  # Muestra la leyenda

# Mostrar gráfico
plt.show()