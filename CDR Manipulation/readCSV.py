import csv
import statistics

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

# Mostrar resultados
print(f"Llamadas largas: {llamadas_largas}")
print(f"Total de llamadas fallidas: {llamadas_fallidas}")
print(f"Promedio de duración de llamadas exitosas: {promedio} segundos")