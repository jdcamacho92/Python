# 🔍 Reto: Encuentra la Extensión Más Activa en un Intervalo de Tiempo
# 1️⃣ Filtra las llamadas dentro de un rango de tiempo específico (por ejemplo, entre las 10:00 y las 14:00).
# 2️⃣ Cuenta cuántas llamadas realizó cada extensión en ese intervalo.
# 3️⃣ Determina cuál fue la extensión más activa en ese período.

# Extra 🔥
# 📊 Grafica el número de llamadas por extensión en el intervalo en un gráfico de barras.

cdrs = [
    {"caller": "1001", "callee": "1002", "timestamp": "09:45:30", "duration": 120, "status": "completed"},
    {"caller": "1003", "callee": "1004", "timestamp": "10:15:45", "duration": 300, "status": "completed"},
    {"caller": "1002", "callee": "1005", "timestamp": "10:30:00", "duration": 60, "status": "failed"},
    {"caller": "1001", "callee": "1006", "timestamp": "11:00:15", "duration": 180, "status": "completed"},
    {"caller": "1004", "callee": "1003", "timestamp": "11:45:50", "duration": 240, "status": "completed"},
    {"caller": "1002", "callee": "1007", "timestamp": "12:10:05", "duration": 90, "status": "completed"},
    {"caller": "1005", "callee": "1006", "timestamp": "12:30:30", "duration": 150, "status": "failed"},
    {"caller": "1007", "callee": "1008", "timestamp": "13:05:20", "duration": 200, "status": "completed"},
    {"caller": "1001", "callee": "1003", "timestamp": "13:40:00", "duration": 360, "status": "completed"},
    {"caller": "1006", "callee": "1005", "timestamp": "14:10:10", "duration": 120, "status": "completed"},
]

from collections import Counter
from collections import defaultdict
# 1️⃣ Filtra las llamadas dentro de un rango de tiempo específico
# (por ejemplo, entre las 10:00 y las 14:00).

calls10to14 = []

for cdr in cdrs:
    hour=int(cdr["timestamp"].split(':')[0])
    
    if hour >= 10 and hour <= 14 :
        #print (hour)
        calls10to14.append(cdr)

#print (calls10to14)


# 2️⃣ Cuenta cuántas llamadas realizó cada extensión en ese intervalo.

callsperextension = defaultdict(int)
for x in calls10to14:
    callsperextension[x["callee"]] += 1
    callsperextension[x["caller"]] += 1
#print (callsperextension)
# 3️⃣ Determina cuál fue la extensión más activa en ese período.
mostactiveext= max(callsperextension, key=callsperextension.get)
print (f"la extension mas activa fue {mostactiveext} con {callsperextension[mostactiveext]} llamadas ")

