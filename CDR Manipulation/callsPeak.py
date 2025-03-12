import matplotlib.pyplot as plt
from collections import Counter
from collections import defaultdict
import matplotlib.pyplot as plt

cdrs = [
    {"caller": "1001", "callee": "2001", "duration": 120, "status": "completed", "timestamp": "14:23:45"},
    {"caller": "1001", "callee": "2002", "duration": 45, "status": "failed", "timestamp": "14:45:12"},
    {"caller": "1003", "callee": "2004", "duration": 75, "status": "failed", "timestamp": "15:10:33"},
    {"caller": "1002", "callee": "2004", "duration": 10, "status": "failed", "timestamp": "15:50:22"},
    {"caller": "1001", "callee": "2007", "duration": 50, "status": "failed", "timestamp": "16:05:17"},
]


# 1️⃣ Encuentra la duración total de llamadas por cada hora.
# 2️⃣ Determina la hora con la mayor duración total de llamadas.
# 3️⃣ Grafica un histograma mostrando la distribución de la duración total de llamadas por hora.

# 💡 Extra: Agrupa las horas en intervalos de 2 horas para ver tendencias más generales.
#  Encuentra la hora con más llamadas realizadas


# 1️⃣ Encuentra la hora con más llamadas fallidas
duration_per_hour = defaultdict(int)
for cdr in cdrs:
    hour = cdr["timestamp"].split(':')[0]
    duration_per_hour[hour] += cdr["duration"]
print(f"Duración total de llamadas por hora: {duration_per_hour}")

# 2️⃣ Determina la hora con la mayor duración total de llamadas.
peakhour = max(duration_per_hour, key=duration_per_hour.get)
print(f"La hora con mayor duracion de llamadas fue: {peakhour} con {duration_per_hour[peakhour]} segundos")

# 3️⃣ Grafica un histograma mostrando la distribución de la duración total de llamadas por hora.

plt.hist(
    list(duration_per_hour.keys()),  # Lista de horas como categorías
    weights=list(duration_per_hour.values()),  # Duración total de llamadas
    bins=range(0, 24, 1),  # Intervalos de 1 hora
    color="red",
    edgecolor="black",
    alpha=0.7
)

plt.xlabel("Hora del día")
plt.ylabel("Duración total de llamadas (segundos)")
plt.title("Distribución de duración total de llamadas por hora")

plt.xticks(range(0, 24, 1))  # Mostrar todas las horas en el eje X
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()
