import datetime
import time
from pygame import mixer

water_mp3 = 'water.mp3'
eye_mp3 = 'eye.mp3'
finish_mp3 = 'finish.mp3'
exercise_mp3 = 'exercise.mp3'
name = str(input("Enter Your Name: "))
water = 'Drank water 375 ml'
water_done = 'Drank water at'
exercise = 'Do Exercise'
exercise_done = 'Done Exercise at'
eye = 'Do Eye Exercise'
eye_done = 'Done Eye Exercise at'
finish = 'Finish For Today'
global_time = datetime.datetime.now()
print(f"Hello {name}, Let's Begin Our Mission")
print(f"You Started at {global_time}")
"""
375ml water = 8 times
4 times eye exe
4 time eye exercise
"""
while True:
    current_time = datetime.datetime.now()
    time_hr = datetime.datetime.now().hour
    time_min = datetime.datetime.now().minute

    if time_hr == 9 and time_min == 30:
        mixer.init()
        mixer.music.load(water_mp3)
        mixer.music.play()
        print(water)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {water_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    elif time_hr == 10 and time_min == 30:
        mixer.init()
        mixer.music.load(water_mp3)
        mixer.music.play()
        print(water)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {water_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    elif time_hr == 11 and time_min == 30:
        mixer.init()
        mixer.music.load(water_mp3)
        mixer.music.play()
        print(water)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {water_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    elif time_hr == 12 and time_min == 30:
        mixer.init()
        mixer.music.load(water_mp3)
        mixer.music.play()
        print(water)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {water_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    elif time_hr == 13 and time_min == 30:
        mixer.init()
        mixer.music.load(water_mp3)
        mixer.music.play()
        print(water)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {water_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    elif time_hr == 14 and time_min == 30:
        mixer.init()
        mixer.music.load(water_mp3)
        mixer.music.play()
        print(water)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {water_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    elif time_hr == 15 and time_min == 30:
        mixer.init()
        mixer.music.load(water_mp3)
        mixer.music.play()
        print(water)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {water_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    elif time_hr == 16 and time_min == 30:
        mixer.init()
        mixer.music.load(water_mp3)
        mixer.music.play()
        print(water)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {water_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    # from here eye exercise start

    elif time_hr == 10 and time_min == 00:
        mixer.init()
        mixer.music.load(eye_mp3)
        mixer.music.play()
        print(eye)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {eye_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    elif time_hr == 12 and time_min == 00:
        mixer.init()
        mixer.music.load(eye_mp3)
        mixer.music.play()
        print(eye)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {eye_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    elif time_hr == 14 and time_min == 00:
        mixer.init()
        mixer.music.load(eye_mp3)
        mixer.music.play()
        print(eye)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {eye_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    elif time_hr == 16 and time_min == 00:
        mixer.init()
        mixer.music.load(eye_mp3)
        mixer.music.play()
        print(eye)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {eye_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    # from here exercise start

    elif time_hr == 11 and time_min == 00:
        mixer.init()
        mixer.music.load(eye_mp3)
        mixer.music.play()
        print(eye)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {eye_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    elif time_hr == 13 and time_min == 00:
        mixer.init()
        mixer.music.load(eye_mp3)
        mixer.music.play()
        print(eye)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {eye_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    elif time_hr == 15 and time_min == 00:
        mixer.init()
        mixer.music.load(eye_mp3)
        mixer.music.play()
        print(eye)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {eye_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    elif time_hr == 16 and time_min == 45:
        mixer.init()
        mixer.music.load(eye_mp3)
        mixer.music.play()
        print(eye)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {eye_done} {current_time}\n"))
                data1.close()
                time.sleep(1 * 60)

    elif time_hr == 17 and time_min == 0:
        mixer.init()
        mixer.music.load(finish_mp3)
        mixer.music.play()
        print(finish)
        status = str(input("Press S To Stop Sound: "))
        if status == "s":
            mixer.music.stop()
            with open("log.txt", 'a') as data1:
                data1.write(str(f"{name} {finish} {current_time}\n"))
                data1.close()
                break
