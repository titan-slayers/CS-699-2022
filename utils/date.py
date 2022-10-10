from datetime import datetime
today = datetime.today()
day = today.strftime("%d_%m_%Y")
set = today.strftime("%p")
print(day,set)

print(datetime.today().strftime("%H:%M %p"))
