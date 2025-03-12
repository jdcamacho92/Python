# Datos de llamadas simulados
cdrs = [
    {"caller": "1001", "callee": "2001", "duration": 120, "status": "completed"},
    {"caller": "1002", "callee": "2002", "duration": 45, "status": "failed"},
    {"caller": "1003", "callee": "2003", "duration": 75, "status": "completed"},
    {"caller": "1004", "callee": "2004", "duration": 10, "status": "failed"},
]

llamadas_largas = []
for x in cdrs:
    if x["duration"]>60:
        llamadas_largas.append(x)
       # print(llamadas_largas)

 # Contar llamadas fallidas
llamadas_fallidas = 0
#sum(1 for cdr in cdrs if cdr["status"] == "failed")   
for y in cdrs:
    if y["status"]=="failed":
        llamadas_fallidas+=1

print(f"Llamadas largas: {llamadas_largas}")
print(f"Total de llamadas fallidas: {llamadas_fallidas}")


####Calcula el promedio de duración de las llamadas exitosas (status == "completed").
import statistics
numcompleted=[]
for x in cdrs:
    if x["status"]=="completed":
        numcompleted.append(x["duration"])
print(statistics.mean(numcompleted)) if numcompleted else 0
