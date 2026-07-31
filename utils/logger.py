from datetime import datetime

def write_log(option):
    with open("logs.txt", "a") as file:
        now = datetime.now()

        file.write(
            f"{now.strftime('%Y-%m-%d %H:%M:%S')} - {option}\n"
        )