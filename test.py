from datetime import datetime

dt = datetime.fromtimestamp(1599680317)

now = datetime.now()
date_time = dt.strftime("%d-%m-%Y, %H:%M")
dictionary = {
    'dt': date_time,
}
print(dictionary)

l1 = [1, 2, 3]
print(max(l1))
