import matplotlib.pyplot as plt
from collections import Counter
from collections import defaultdict
cdrs = [
    {"caller": "1001", "callee": "2001", "duration": 120, "status": "completed", "timestamp": "14:23:45"},
    {"caller": "1001", "callee": "2002", "duration": 45, "status": "failed", "timestamp": "14:45:12"},
    {"caller": "1003", "callee": "2004", "duration": 75, "status": "failed", "timestamp": "15:10:33"},
    {"caller": "1002", "callee": "2004", "duration": 10, "status": "failed", "timestamp": "15:50:22"},
    {"caller": "1001", "callee": "2007", "duration": 50, "status": "failed", "timestamp": "16:05:17"},
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