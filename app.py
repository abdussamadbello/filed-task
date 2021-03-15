
from bson.errors import BSONError
from fastapi import FastAPI, HTTPException
from fastapi.params import Body
from pydantic import ValidationError
from pymongo.errors import PyMongoError
from repository import(
    create_file,
    deleteById,
    getAll,
    getById,
    update_file,
)
from model import(
    AudioBook,
    Song,
    Podcast
)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/{audioFileType}/{audioFileID}")
async def get_item(audioFileType: str, audioFileID: str):
    try:
        if is_field_valid(audioFileID) and is_route_exist(audioFileType):
            result = getById(audioFileType, audioFileID)
            return result
        elif is_route_exist(audioFileType):
            result = getAll(audioFileType)
            return result
        else:
            raise HTTPException(status_code=400, detail="path doesn't exists")

    except BSONError as e:
            error = e.json()
            raise HTTPException(
                   status_code=400,
                   detail=error
                   )
    except PyMongoError as e:
               error = str(e)
               raise HTTPException(
                   status_code=400,
                   detail=error
                   )

@app.post("/{audioFileType}")
async def create_item(audioFileType, req: dict = Body(...)):
        try:
            if (audioFileType == "song"):
                song = Song(**req)
                return{create_file(audioFileType, song)}
            elif (audioFileType == "podcast"):
                podcast = Podcast(**req)
                return{create_file(audioFileType, podcast)}
            elif (audioFileType == "audiobook"):
               audiobook = AudioBook(**req)
               return{create_file(audioFileType, audiobook)}
            else:
               raise HTTPException(
                   status_code=400,
                   detail="path "+audioFileType+" not found"
                   )

        except ValidationError as e:
            error = e.json()
            raise HTTPException(
                   status_code=400,
                   detail=error
                   )
        except PyMongoError as e:
               error = str(e)
               raise HTTPException(
                   status_code=400,
                   detail=error
                   )


@app.put("/{audioFileType}/{audioFileID}")
async def update_item(audioFileType, audioFileID, req: dict = Body(...)):

    try:
        if is_field_valid(audioFileID) and is_route_exist(audioFileType):
            if (audioFileType == "song"):
                song = Song(**req)
                return{update_file(audioFileType, song, audioFileID)}
            elif (audioFileType == "podcast"):
                podcast = Podcast(**req)
                return{update_file(audioFileType, podcast)}
            elif audioFileType == "audiobook":
                audiobook = AudioBook(**req)
                return{update_file(audioFileType, audiobook)}
            else:
                raise HTTPException(
                    status_code=400,
                    detail="path "+audioFileType+" not found"
                )
        else:
            raise HTTPException(
                status_code=400,
                detail="AudioID or Audiotype path missing"
            )
    except ValidationError as e:
            error = e.json()
            raise HTTPException(
                   status_code=400,
                   detail=error
                   )
    except PyMongoError as e:
            error = str(e)
            raise HTTPException(
                   status_code=400,
                   detail=error
                   )


@app.delete("/{audioFileType}/{audioFileID}")
async def delete_item(audioFileType: str, audioFileID: str):
    try:
        if is_field_valid(audioFileID) and is_route_exist(audioFileType):
            result = deleteById(audioFileType, audioFileID)
            print(audioFileType)
            return result
        else:
             raise HTTPException(
                status_code=400,
                detail="AudioID or Audiotype path missing"
            )
    except (BSONError,PyMongoError) as e:
           e=str(e)
           print(e)
           raise HTTPException(
                   status_code=400,
                   detail=e
                   )


def is_route_exist(audioFileType):
    if audioFileType in ("song", "podcast", "audiobook"):
          return True
    return False


def is_field_valid(audioFileID: str):
    if not audioFileID.strip():
        return False
    return True
