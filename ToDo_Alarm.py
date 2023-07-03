import datetime
import time
import threading
from Speak import speak_hindi
from Speak import speak_english
from Listen import takecommand
from playsound import playsound

tasks = []

def add_task():
    print(" ")
    speak_hindi('आप खुद टाइप करना चाहेंगे या बोलना चाहेंगे')
    print(" ")
    print('Would you like to type or speak yourself?')

    query = takecommand()
    query = str(query).lower()

    if 'type' in query or 'write' in query:
        task = input("Enter a new task: ")
        tasks.append(task)
        with open('C:\\Users\\neera\\PycharmProjects\\Projects\\To-Do-Alarm\\remind.text', 'a') as file:
            file.write(task + '\n')  # Add a new line after each task
        print("Task added successfully!")
        speak_hindi('कार्य सफलता पूर्वक जोड़ दिया गया है।')

    elif 'speak' in query or 'talk' in query or 'say' in query:
        speak_hindi('क्या याद दिलाना है आपको।')
        query = takecommand().lower()
        remembermsg = query.replace("remind me", "")
        speak_english('You told me to remind you: ' + remembermsg)
        with open('C:\\Users\\neera\\PycharmProjects\\Projects\\To-Do-Alarm\\remind.text', 'a') as file:
            file.write(remembermsg + '\n')  # Add a new line after each task
        print("Task added successfully!")
        speak_hindi('कार्य सफलता पूर्वक जोड़ दिया गया है।')

    else:
        speak_hindi('माफ़ कीजिए, कोई भी कार्य नहीं जोड़ा गया है।')




def remove_task():
    with open('C:\\Users\\neera\\PycharmProjects\\Projects\\To-Do-Alarm\\remind.text', 'r') as file:
        tasks = file.read().strip().split('\n')

    if len(tasks) == 1:
        print(" ")
        speak_english("No tasks to remove.")
        print("No tasks to remove.")
        print(" ")

    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

        speak_english("Please specify the task number to remove or say 'first', 'second', 'third', 'fourth', 'fifth', 'six', 'seven' up to fifteen or 'last'.")

        query = takecommand().lower()
        if 'first' in query:
            removed_task = tasks.pop(0)
        elif 'second' in query:
            removed_task = tasks.pop(1)
        elif 'third' in query:
            removed_task = tasks.pop(2)
        elif 'fourth' in query:
            removed_task = tasks.pop(3)
        elif 'fifth' in query:
            removed_task = tasks.pop(4)
        elif 'six' in query:
            removed_task = tasks.pop(5)
        elif 'seven' in query:
            removed_task = tasks.pop(6)
        elif 'eight' in query:
            removed_task = tasks.pop(7)
        elif 'nine' in query:
            removed_task = tasks.pop(8)
        elif 'ten' in query:
            removed_task = tasks.pop(9)
        elif 'eleven' in query:
            removed_task = tasks.pop(10)
        elif 'twelve' in query:
            removed_task = tasks.pop(11)
        elif 'thirteen' in query:
            removed_task = tasks.pop(12)
        elif 'fourteen' in query:
            removed_task = tasks.pop(13)
        elif 'fifteen' in query:
            removed_task = tasks.pop(14)
        elif 'last' in query:
            removed_task = tasks.pop()
        else:
            try:
                task_number = int(query)
                if task_number < 1 or task_number > len(tasks):
                    print("Invalid task number!")
                    return
                removed_task = tasks.pop(task_number - 1)
            except ValueError:
                print("Invalid input!")
                return

        with open('C:\\Users\\neera\\PycharmProjects\\Projects\\To-Do-Alarm\\remind.text', 'w') as file:
            file.write('\n'.join(tasks))

        print(f"Task '{removed_task}' removed successfully!")
        speak_english(f"The task {removed_task} has been removed successfully.")


def view_tasks():
    with open('C:\\Users\\neera\\PycharmProjects\\Projects\\To-Do-Alarm\\remind.text', 'r') as file:
        tasks = file.read().strip().split('\n')

    if len(tasks) == 1:
        speak_english("No tasks found.")
        print("No tasks found.")
        print(" ")
    else:
        print(" ")
        print("Current tasks:")
        ordinal_numbers = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
        for index, task in enumerate(tasks):
            ordinal = ordinal_numbers[index] if index < len(ordinal_numbers) else str(index + 1) + "th"
            speak_english(f"The {ordinal} task is: {task}")
            print(f"The {ordinal} task is: {task}")

            # Check if the task contains a time
            if "at" in task:
                time_index = task.index("at") + 2
                time_str = task[time_index:].strip()

                # Parse the time from the task
                try:
                    task_time = datetime.datetime.strptime(time_str, "%I:%M %p")

                    # Get the current time
                    current_time = datetime.datetime.now().strftime("%I:%M %p")
                    current_time = datetime.datetime.strptime(current_time, "%I:%M %p")

                    # Check if it's time to remind
                    if current_time >= task_time:
                        speak_english(f"It's time to {task}")
                        # You can add any code or function call here to handle the reminder
                except ValueError:
                    pass


def set_alarm():
    alarmHour = int(input("Enter Hours: "))
    alarmMinute = int(input("Enter Minute: "))
    alarmAmPm = input("am / pm : ")
    if alarmAmPm == "pm":
        alarmHour += 12

    while True:
        if alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute:
            print(".............  Its Wake Up Alarm .............")
            print(" ")
            # Give the path of the music or mp3 file you want to set the alarm.
            # playsound("C:\\Users\\neera\\PycharmProjects\\ADatabase\\SupermanRising.mp3")

            for _ in range(5):  # 5 times loop
                speak_english("Wake up Neeraj, It's time to awake.")
                speak_english("If you are currently awake, kindly respond with a yes to indicate your wakefulness.")
                speak_english("Otherwise, please reply with a no to indicate that you are not currently awake.")

                choice = takecommand().lower()
                if 'yes' in choice or 'got up' in choice:
                    exit()
                else:
                    speak_english("Wake up Neeraj, It's time to awake.")
                    time.sleep(5)  # Wait for 5 seconds between each "Wake up, Neeraj" message

            speak_english("Alarm Snoozed. Repeating after 5 minutes...")

            while True:
                time.sleep(300)     # Sleep for 5 minutes 300 seconds
                speak_english("If you are currently awake, kindly respond with a yes to indicate your wakefulness.")
                speak_english("Otherwise, please reply with a no to indicate that you are not currently awake.")
                choice = takecommand().lower()
                if 'yes' in choice or 'got up' in choice:
                    break
                else:
                    # time.sleep(30)  # Sleep for 5 minutes 300 seconds
                    for _ in range(5):
                        speak_english("Wake up, Neeraj, It's time to awake.")
                        time.sleep(5)  # Wait for 5 seconds between each "Wake up, Neeraj" message
                    speak_english("Alarm Snoozed. Repeating after 5 minutes...")

            break
        else:
            time.sleep(10)  # Check every 10 seconds


def remind_alarm():
    alarms = []
    with open('C:\\Users\\neera\\PycharmProjects\\Projects\\To-Do-Alarm\\remind.text', 'r') as file:
        tasks = file.read().strip().split('\n')

    for task in tasks:
        if "at" in task:
            time_index = task.index("at") + 2
            time_str = task[time_index:].strip()

            try:
                task_time = datetime.datetime.strptime(time_str, "%I:%M %p")
                alarms.append(task_time)
            except ValueError:
                pass

    while True:
        now = datetime.datetime.now()
        for alarm in alarms:
            if now.hour == alarm.hour and now.minute == alarm.minute:
                speak_english(f"It's time to {tasks[alarms.index(alarm)]}")
                # Add your desired functionality for handling the alarm here

        # Check if the current time exceeds the limit
        limit = datetime.time(20, 0)  # Specify your desired limit here (e.g., 20:00 or 8:00 PM)
        if now.time() > limit:
            break

        time.sleep(10)  # Check every 10 seconds

def todo_list_with_alarm():
    print("Welcome to the To-Do List with Alarm!")
    speak_english("Welcome to the To-Do List with Alarm!")
    print(" ")

    def input_thread():
        while True:
            print(" ")
            speak_english("Choose the below options.")
            print(" ")

            print("\nSelect an option:")
            print("1. Add a Task")
            print("2. Remove a Task")
            print("3. View Tasks")
            print("4. Set Alarm")
            print("0. Exit")

            print(" ")
            speak_english("Enter your choice")
            print(" ")

            choice = input("Enter your choice: ")

            if choice == '0':
                print("Thank you for using the To-Do List with Alarm. Goodbye!")
                break

            try:
                choice = int(choice)
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if choice < 1 or choice > 4:
                print("Invalid choice! Please select a valid option.")
                continue

            if choice == 1:
                add_task()
            elif choice == 2:
                remove_task()
            elif choice == 3:
                view_tasks()
            elif choice == 4:
                set_alarm()

    input_thread = threading.Thread(target=input_thread)
    alarm_thread = threading.Thread(target=remind_alarm)

    input_thread.start()
    alarm_thread.start()

    input_thread.join()
    alarm_thread.join()

todo_list_with_alarm()