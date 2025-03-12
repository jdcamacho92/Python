from collections import Counter
from collections import OrderedDict
cdrs = [
    {"caller": "1001", "callee": "2001", "duration": 120, "status": "completed"},
    {"caller": "1002", "callee": "2002", "duration": 45, "status": "failed"},
    {"caller": "1003", "callee": "2003", "duration": 75, "status": "completed"},
    {"caller": "1002", "callee": "2004", "duration": 10, "status": "failed"},
    {"caller": "1001", "callee": "2005", "duration": 50, "status": "failed"},
    {"caller": "1003", "callee": "2006", "duration": 5, "status": "failed"},
    {"caller": "1001", "callee": "2007", "duration": 30, "status": "failed"},
]

failedcalls = Counter(cdr["caller"] for cdr in cdrs if cdr["status"]=="failed")
print (failedcalls)

failedcallsordered = OrderedDict(dict(sorted(failedcalls.items(), key=lambda item: item[1], reverse=True,)))
print (failedcallsordered)

print (max(failedcalls, key=failedcalls.get))