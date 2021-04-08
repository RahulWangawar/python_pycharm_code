# Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio
from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user== stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    # musiconloop("water.mp3","drank")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    # water_sec = 40*60
    # exercise_sec = 30*60
    # eyes_sec = 45*60
    water_sec = 25
    exercise_sec = 35
    eyes_sec = 45

    while True:
        if time() - init_water > water_sec:
            print("Water Drinking Time. Enter drank to stop Alarm")
            musiconloop("water.mp3", "drank")
            init_water = time()
            log_now("Drank Water at :")

        if time() - init_exercise > exercise_sec:
            print("Do Some physical Activity. Press 'done' to stop Alarm")
            musiconloop("exercise.mp3", "done")
            init_exercise = time()
            log_now("Physical Exercise at :")

        if time() - init_eyes > eyes_sec:
            print("Do Some Eyes exercise. Press 'done' to stop Alarm")
            musiconloop("eyes.mp3", "done")
            init_eyes = time()
            log_now("Eyes Relaxed at :")