import re

patron="(.549)?(.0)?(345)(.\s)?([0-9]{2})?([0-9]{7})$"
numeros=["(0345) 154123456",
         "+5493454123456",
         "3454123456",
         "+54011123456",
         "34564123456"
]

for n in numeros:
    match=re.findall(patron,n,flags=re.IGNORECASE)
    if match:
        print(n,"numero válido")
    else:
        print(n,"numero no válido")