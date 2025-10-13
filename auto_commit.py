import os
import datetime
import subprocess

# تاریخ کے مطابق ایک لائن فائل میں لکھے گا
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# فائل بنائیں یا اپڈیٹ کریں
with open("daily_log.txt", "a") as file:
    file.write(f"Auto commit for {today}\n")

# Git commands چلائیں
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Auto commit on {today}"])
subprocess.run(["git", "push"])
