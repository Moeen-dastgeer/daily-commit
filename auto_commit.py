import os
import datetime
import subprocess

today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("daily_log.txt", "a") as file:
    file.write(f"Auto commit for {today}\n")

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Auto commit on {today}"])
subprocess.run(["git", "push"])
