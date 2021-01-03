import re
txt="""
<html><head><a href='fsjfaj-fsdf'>Hamza Ansari</a>
</head></html>
"""
print(
     re.findall(re.compile('.+'),txt))