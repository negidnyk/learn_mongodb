from fastapi import APIRouter, Depends, HTTPException
from mongo_config import users_collection
from users.schemas import UserOut
import datetime
from fastapi import HTTPException


def create_user(new_user):
    new_user_ = new_user.dict()
    checkpoint = True
    counter = 1
    while checkpoint is True:
        if users_collection.count_documents({"_id": counter}) == 0:
            new_user_["_id"] = counter
            new_user_["registered_at"] = datetime.datetime.now(tz=datetime.timezone.utc)
            users_collection.insert_one(new_user_)
            return new_user_

        else:
            counter += 1


def get_users(skip, limit, sort_by, sorting_direction):
    users_list = users_collection.find().limit(limit).skip(skip).sort(sort_by, sorting_direction)
    result = [user for user in users_list]
    result.append({"total_count": users_collection.count_documents({})})
    return result


def update_user(user_id, user):
    if users_collection.count_documents({"_id": user_id}) == 0:
        raise HTTPException(status_code=400, detail="Document with submitted id does not exist")

    else:
        user_ = user.dict()
        users_collection.update_one({"_id": user_id}, {"$set": user_})
        return [user for user in users_collection.find({"_id": user_id})]


def delete_user(user_id):
    if users_collection.count_documents({"_id": user_id}) == 0:
        raise HTTPException(status_code=400, detail="Document with submitted id does not exist")

    else:
        users_collection.delete_one({"_id": user_id})
