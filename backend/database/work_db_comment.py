# # Use with database Comment
# def create_comment(db: Session, create_comment: Comment):
#     comment = Comment(
#         user_id  = create_comment.user_id,
#         track_id = create_comment.track_id,
#         comment = create_comment.comment
#     )
#     db.add(comment)
#     db.commit()
#     db.refresh(comment)
#     return comment
#
# def get_all_comments(db: Session):
#     all_data = db.query(Comment).all()
#     return all_data
# def get_comments_for_user(db: Session, user_id: int):
#     get_comment = db.query(Comment).filter(Comment.user_id == user_id).all()
#     return get_comment
# def delete_all_comments_user(db: Session, user_id: int):
#     delete_tracks = db.query(Comment).filter(Comment.user_id == user_id).all()
#     db.delete(delete_tracks)
#     db.commit()
# def delete_comment(db: Session, user_id: int, track_id: int, comment_text: str):
#     all_comment = get_comments_for_user(db, user_id)
#     for comment in all_comment:
#         if comment.track_id == track_id and comment.comment == comment_text:
#             db.delete(comment)
#             db.commit()
#             break
# def update_comment(db: Session, user_id: int, track_id: int, comment_text: str, up_text: str):
#     all_comment = get_comments_for_user(db, user_id)
#     for comment in all_comment:
#         if comment.track_id == track_id and comment.comment == comment_text:
#             db.execute(update(Comment).where(Comment.id == comment.id).values(comment = up_text))
#             db.commit()
#             up_comment = db.query(Comment).filter(Comment.id == comment.id).all()
#             db.refresh(up_comment)
#             return up_comment