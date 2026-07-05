from datetime import datetime


def get_current_time_slot() -> str:
    now = datetime.now()

    start_minute = 0 if now.minute < 30 else 30
    end_hour = now.hour
    end_minute = 30 if start_minute == 0 else 0

    if start_minute == 30:
        end_hour += 1

    return (
        f"{now.hour:02}:{start_minute:02}"
        f"-"
        f"{end_hour:02}:{end_minute:02}"
    )