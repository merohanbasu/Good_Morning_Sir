import time
current_time = time.strftime('%I:%M:%S:%p')
print("Current time is:",current_time)
print("So")

hour = int(time.strftime('%H'))

if(hour >= 3 and hour < 12):
    print("Good Morning Sir")
elif(hour >= 12 and hour < 18):
    print("Good Afternoon Sir")
elif(hour >= 18 and hour < 21):
    print("Good Evening Sir")
elif(hour >= 21 and hour <= 24):
    print("Good Night Sir")
elif(hour >= 0 and hour < 3):
    print("Good Night Sir")



