import matplotlib.pyplot as plt
from collections import Counter

cdrs = [
    {"caller": "1001", "callee": "2001", "duration": 120, "status": "completed", "timestamp": "14:23:45"},
    {"caller": "1001", "callee": "2002", "duration": 45, "status": "failed", "timestamp": "14:45:12"},
    {"caller": "1003", "callee": "2004", "duration": 75, "status": "failed", "timestamp": "15:10:33"},
    {"caller": "1002", "callee": "2004", "duration": 10, "status": "failed", "timestamp": "15:50:22"},
    {"caller": "1001", "callee": "2007", "duration": 50, "status": "failed", "timestamp": "16:05:17"},
]

#  Encuentra la hora con más llamadas realizadas
hours = Counter(cdr["timestamp"].split(':')[0] for cdr in cdrs)
maxhours = max(hours, key=hours.get)
print(f"Hora con mayor número de llamadas: {maxhours}:00")

# 1️⃣ Encuentra la hora con más llamadas fallidas
hours2 = Counter(cdr["timestamp"].split(':')[0] for cdr in cdrs if cdr["status"] == "failed")
maxhours2 = max(hours2, key=hours2.get, default="No data")  # Manejo si no hay fallidas
print(f"Hora con mayor número de llamadas fallidas: {maxhours2}:00")

# 2️⃣ Gráfica de cantidad de llamadas por hora
horas = sorted(hours.keys())  # Asegurar que las horas estén en orden
cantidad_llamadas = [hours[h] for h in horas]

plt.bar(horas, cantidad_llamadas, color="red", edgecolor="black")

plt.xlabel("Hora")
plt.ylabel("Cantidad de llamadas")
plt.title("Cantidad de llamadas por hora")

plt.xticks(rotation=50)
plt.show()