from playsound import playsound
import time

#ANSI ESCAPE CHARACTER
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minute_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minute_left:02d}:{seconds_left:02d}")

    playsound("alarm_sound.mp3")

minutes = int(input("Set how many minutes to wait: "))
seconds = int(input("Set how many seconds to wait: "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)        
