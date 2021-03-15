from datetime import datetime
from model import Podcast, Song

poddata={
    "name": "hello",
    "host": "hello",
    "Participants": ["heoo","hi"],
    "duration":"10",
    "upload_time":datetime.now()
}

correct_songdata={
    "name": "hello",
    "duration":"10",
    "upload_time":"2022-03-15 17:47:55.170771"
}

incorrect_songdata={
    "name": "hellooooooooooooooooooooo",
    "duration":"10",
    "upload_time":"2021-03-15 17:47:55.170771"
}


