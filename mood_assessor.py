import datetime
import os

def assess_mood():
    dict = {'happy': 2, 'relaxed': 1, 'apathetic': 0, 'sad': -1, 'angry': -2}

    date_today = datetime.date.today() # get the date today as a date object
    date_today = str(date_today) # convert it to a string

    f = open('data/mood_diary.txt', 'r')
    lies = file.readlines()
    last_entry = lines[-1].split()
    if last_entry[0] == date_today:
                print("Sorry, you have already entered your mood today.")
                return

    while True:
        mood = input("Please enter your current mood (happy, relaxed, apathetic, sad, angry): ")
        if mood in dict:
            break
        else:
            print("Please enter a valid mood.")

    moods = dict[mood]

    f = open('data/mood_diary.txt', 'a')
    file.write(f"{current_date} {mood_value}\n")

    if len(lines) >= 7:
        entries = lines[-7:]
        mood_sum = sum(int(entry.split()[1]) for entry in entries)
        average = round(mood_sum / 7)
        
        if average_mood >= 5:
            print("Your diagnosis: manic!")
        elif average_mood <= -4:
            print("Your diagnosis: depressive!")
        elif average_mood == 0:
            print("Your diagnosis: schizoid!")
        else:
            the_moods = {2: 'happy', 1: 'relaxed', 0: 'apathetic', -1: 'sad', -2: 'angry'}
            print(f"Your diagnosis: {the_moods[average]}")