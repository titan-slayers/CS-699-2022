import re
que = "iphone 13 "
check = "APPLE iPhone 13 (Midnight, 128 GB)"
if re.search(que,check,re.IGNORECASE):
    print("yes")

