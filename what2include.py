import json
import os
from collections import defaultdict

if os.path.exists("schemes/status.json"):
    with open("schemes/status.json", encoding="utf-8") as f:
        current_status = json.load(f)
if os.path.exists("schemes/known/fmm_result.json"):
    with open("schemes/known/fmm_result.json", encoding="utf-8") as f:
         fmm_status = json.load(f)
        
for n1 in range(2, 32):
    for n2 in range(n1, 32):
        for n3 in range(n2, 32):
            if max(n1 * n2, n2 * n3, n1 * n3) <= 128:
                current_status[f"{n1}x{n2}x{n3}"] = current_status.get(f"{n1}x{n2}x{n3}", {"ranks": {}, "omegas": {}, "complexities": {}, "schemes": defaultdict(list)})
    
                if not current_status[f"{n1}x{n2}x{n3}"]["ranks"].__contains__("Q"):
                        continue
                fmm_status[f"{n1}x{n2}x{n3}"] = fmm_status.get(f"{n1}x{n2}x{n3}", {"rank": {}})
                minrank=n1*n2*n3
                minfield=""
                for field,decomposition in current_status[f"{n1}x{n2}x{n3}"]['schemes'].items():
                    if decomposition[0]['rank']<minrank and field!='Z2':
                        minrank=decomposition[0]['rank']
                        minfield=field

                if minrank<fmm_status[f"{n1}x{n2}x{n3}"]["rank"]:
                    print(current_status[f"{n1}x{n2}x{n3}"]['schemes'][minfield][0]['path'])
    
