import csv
import statistics
from collections import Counter


#📌 Objetivo: Análisis Avanzado de CDRs
#Ahora agregaremos:
#✅ Cantidad de llamadas por cada caller.
#✅ Caller con más llamadas fallidas.
#✅ Distribución de duración de llamadas (mínimo, máximo, mediana).


# Leer el archivo CSV
with open("cdrs.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    cdrs = [row for row in reader]

# Convertir 'duration' a enteros
for cdr in cdrs:
    cdr["duration"] = int(cdr["duration"])

# Filtrar llamadas largas (>60s)
llamadas_largas = [cdr for cdr in cdrs if cdr["duration"] > 60]

# Contar llamadas fallidas
llamadas_fallidas = sum(1 for cdr in cdrs if cdr["status"] == "failed")

# Calcular promedio de duración de llamadas exitosas
numcompleted = [cdr["duration"] for cdr in cdrs if cdr["status"] == "completed"]
promedio = statistics.mean(numcompleted) if numcompleted else 0

# 📊 Cantidad de llamadas por cada caller
caller_counts = Counter(cdr["caller"] for cdr in cdrs)

# ❌ Caller con más llamadas fallidas
failed_callers = [cdr["caller"] for cdr in cdrs if cdr["status"] == "failed"]
caller_mas_fallidas = Counter(failed_callers).most_common(1)

# 📈 Estadísticas de duración de llamadas
durations = [cdr["duration"] for cdr in cdrs]
min_duracion = min(durations)
max_duracion = max(durations)
mediana_duracion = statistics.median(durations)

print (durations)

# 📢 Mostrar resultados
print(f"Llamadas largas: {llamadas_largas}")
print(f"Total de llamadas fallidas: {llamadas_fallidas}")
print(f"Promedio de duración de llamadas exitosas: {promedio:.2f} segundos")
print(f"Llamadas por caller: {caller_counts}")
print(f"Caller con más llamadas fallidas: {caller_mas_fallidas}")
print(f"Duración - Mínima: {min_duracion}s, Máxima: {max_duracion}s, Mediana: {mediana_duracion}s")



import matplotlib.pyplot as plt

# Separar duraciones por estado
durations_completed = [cdr["duration"] for cdr in cdrs if cdr["status"] == "completed"]
durations_failed = [cdr["duration"] for cdr in cdrs if cdr["status"] == "failed"]


# Crear histograma con colores diferentes
plt.hist(durations_completed, bins=5, color="green", edgecolor="black", alpha=0.7, label="Completadas")
plt.hist(durations_failed, bins=5, color="red", edgecolor="black", alpha=0.7, label="Fallidas")

# Etiquetas y título
plt.xlabel("Duración de llamadas (segundos)")
plt.ylabel("Cantidad de llamadas")
plt.title("Distribución de duración de llamadas")
plt.legend()  # Muestra la leyenda

# Mostrar gráfico
plt.show()

