import datetime

moods = {
    "happy": 2,
    "relaxed": 1,
    "apathetic": 0,
    "sad": -1,
    "angry": -2
}

def user_input(mood):
    return moods[mood]

def mood_entries():
    date_today = datetime.date.today() # get the date today as a date object
    date_today = str(date_today) # convert it to a string
    file = open("data/mood_diary.txt", "r")
    for line in file:
        if date_today in line:
            print("You've already input your mood today.")
            return
    file.close()
    complete = False
    while not complete:
        mood = input("Please enter your current mood (can be happy, relaxed, apathetic, sad, or angry): ")
        if mood in ['happy', 'relaxed', 'apathetic', 'sad', 'angry']:
            file = open("data/mood_diary.txt", "a")
            file.write(f"{date_today} {(user_input(mood))}\n")
            file.close()
            complete = True

def assess_mood():
    mood_entries()
    file = open("data/mood_diary.txt", "r")
    entries = file.readlines()
    file.close()

    if len(entries) < 7:
        return

    entries7 = entries[-7:]
    values = [int(entry.split(' ')[1]) for entry in entries7]
    count = {user_input(mood): 0 for mood in moods}

    for value in values:
        count[value] += 1

    if count[user_input("happy")] >= 5:
        diagnosis = "manic"
    elif count[user_input("sad")] >= 4:
        diagnosis = "depression"
    elif count[user_input("apathetic")] >= 6:
        diagnosis = "schizoid"
    else:
        average = sum(values) / len(values)
        average = round(average)
        diagnosis = [mood for mood, value in moods.items() if value == average][0]

    print(f"Your diagnosis: {diagnosis}!")

 # for lines in file:
    #     lines = len(file.readlines())
    #     if lines != 7:
    #         break
    #     else:
    #         average = round(statistics.mean(file))
    #         average = int(average)
    #         if len(2) >= 5:
    #             print("Your diagnosis: manic!")
    #         elif len(-1) >= 4:
    #             print("Your diagnosis: depressive!")
    #         elif len(0) >= 6:
    #             print("Your diagnosis: schizoid!")
    #         else:
    #             print(f"Your diagnosis: {average}.")