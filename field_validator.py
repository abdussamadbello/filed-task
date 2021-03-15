from datetime import datetime

def check_upload_time(v):
    if v < datetime.now():
        raise ValueError('Time cannot be in the past')
    return v