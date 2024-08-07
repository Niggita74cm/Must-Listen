from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends, Request
from sqlalchemy.orm import Session
from backend.model.models_admin import NameDB
from backend.services.LoadTrackDB import LoadTrackDB

#from backend.database.work_db_track import delete_all_track_users
#from backend.database.work_db_track import get_all_comments,  delete_comment, delete_all_comments_user

router = APIRouter()
user_db = [None]
comments = [None]
# @router.get("/app/LK/admin")
# async def get_admin_menu(request: Request):
#     print("Get_admin_menu")
#     return {"admin_menu": "List menu"}
# @router.get("/app/LK/admin/create_user")
# async def get_admin_create_user(request: Request):
#     print("get_admin_create_user")
#     return {"admin_user": "List create user"}
# @router.get("/app/LK/admin/delete_comment")
# async def get_admin_delete_comment(request: Request, db: Session = Depends(get_db)):
#     if comments[0] == None:
#         comments[0] = get_all_comments(db)
#     print("get_admin_delete_comment")
#     return {"admin_comment": "List delete comment"}
# @router.get("/app/LK/admin/delete_user")
# async def get_admin_delete_user(request: Request, db: Session = Depends(get_db)):
#     if user_db[0] == None:
#         user_db[0] = get_all_user(db)
#     #отправку на лист надо будет сделать
#     print("get_admin_create_user")
#     return {"admin_comment": "List create user"}



@router.post("/app/LK/admin", response_model=NameDB)
async def choose_menu(request: Request, db_name: NameDB, db: Session = Depends(get_db)):
    print("LoadTrack")
    print(db_name.name_database)
    LoadTrackDB(db_name.name_database, db)
    return {"name_database": db_name.name_database}


# @router.post("/app/LK/admin/create_user", response_model=UserCreateAdmin)
# async def create_user(request: Request, current_user: UserCreateAdmin, db: Session = Depends(get_db)):
#     if current_user.close == False:
#         form = UserCreateForm(current_user)
#         await form.load_data()
#         if await form.is_valid():
#             user = UserCreate(
#         login=form.login,
#         email=form.email,
#         password=form.password
#         )
#             try:
#                 print("trying login")
#                 user_ = create_new_user(user_Create=user, db=db)
#             except IntegrityError:
#                 print("Error: create_new_user")
#     response = RedirectResponse(url="/app/LK/admin", status_code=HTTP_303_SEE_OTHER)
#     return response
# @router.delete("/app/LK/admin/delete_user", response_model=DataForDeleteUser)
# async def delete_user(request: Request, data: DataForDeleteUser, db: Session = Depends(get_db)):
#     ...
#     # if await (data.close == False):
#     #     try:
#     #         if data.email_ind == True or data.login_ind == True:
#     #             user_db[0] = get_all_user(db)
#     #             if data.login_ind == True:
#     #                 similar_strings = find_similar_strings(data.email_ind, user_db[0], "login")
#     #             else:
#     #                 similar_strings = find_similar_strings(data.email_ind, user_db[0], "email")
#     #             user_db[0] = similar_strings
#     #         else:
#     #             user_id = data.user_id
#     #             delete_user(db, user_id)
#     #             delete_all_track_users(db, user_id)
#     #             user_db[0] = None
#     #             print("trying delete")
#     #     except IntegrityError:
#     #         print("Error: delete_user")
#     #     response = RedirectResponse(url="/app/LK/admin/delete_user", status_code=HTTP_303_SEE_OTHER)
#     # else:
#     #     user_db[0] = None
#     #     response = RedirectResponse(url="/app/LK/admin", status_code=HTTP_303_SEE_OTHER)
#     # return response
#
# @router.delete("/app/LK/admin/delete_comment", response_model=DataForDeleteComment)
# async def delete_comment(request: Request, data: DataForDeleteComment, db: Session = Depends(get_db)):
#     ...
#     # if await (data.close == False):#доделать
#     #     try:
#     #         if data.login_ind == True:
#     #             comments[0] = get_all_comments(db)
#     #             user_db[0] = get_all_user(db)
#     #             similar_strings = find_similar_strings(data.login, user_db[0], "login")
#     #             result = []
#     #             for string in similar_strings:
#     #                 for comment in comments[0]:
#     #                     if comment["user_id"] == string["user_id"]:
#     #                       result.append(comment)
#     #             comments[0] = result
#     #             user_db[0] = None
#     #         else:
#     #             user_id = data.user_id
#     #             delete_user(db, user_id)
#     #             delete_all_track_users(db, user_id)
#     #             comments[0] = None
#     #             print("trying delete")
#     #     except IntegrityError:
#     #         print("Error: delete_user")
#     #     response = RedirectResponse(url="/app/LK/admin/delete_comment", status_code=HTTP_303_SEE_OTHER)
#     # else:
#     #     comments[0] = None
#     #     response = RedirectResponse(url="/app/LK/admin", status_code=HTTP_303_SEE_OTHER)
#     # return response
