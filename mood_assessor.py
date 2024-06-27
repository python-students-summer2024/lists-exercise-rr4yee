import datetime
import os

moods = {
    "happy": 2,
    "relaxed": 1,
    "apathetic": 0,
    "sad": -1,
    "angry": -2
}

def mood_input():
    while True:
        mood = input("Please enter your current mood (happy, relaxed, apathetic, sad, angry): ").strip().lower()
        if mood in moods:
            return mood
        else:
            print("Please enter a mood from the options.")

def today():
    date_today = str(datetime.date.today())
    if os.path.exists("data/mood_diary.txt"):
        f = open("data/mood_diary.txt")
        entries = f.readlines()
        for entry in entries:
            if entry.startswith(date_today):
                return True
    return False

def saving(mood):
    date_today = str(datetime.date.today())
    type = moods[mood]
    os.makedirs("data", exist_ok=True)
    f = open("data/mood_diary.txt", "a")
    f.write(f"{date_today},{type}\n")
    f.close()

def diagnose():
    f = open("data/mood_diary.txt", "r")
    entries = file.readlines()
    file.close()
    if len(entries) < 7:
        return

    entries7 = entries[-7:]
    type = [int(entry.split(',')[1]) for entry in entries7]
    count = {mood: 0 for mood in moods}

    for value in type:
        for mood, type in moods.items():
            if value == type:
                count[mood] += 1

    if count["happy"] >= 5:
        diagnosis = "manic"
    elif count["sad"] >= 4:
        diagnosis = "depressive"
    elif count["apathetic"] >= 6:
        diagnosis = "schizoid"
    else:
        average = round(sum(type) / 7)
        diagnosis = [mood for mood, value in moods.items() if value == average][0]

    print(f"Your diagnosis: {diagnosis}!")

def assess_mood():
    if today():
        print("Sorry, you have already entered your mood today.")
        return

    mood = mood_input()
    saving(mood)
    diagnoses()

