# from sqlalchemy import select, func, desc
# from sqlalchemy.orm import Session
#
# from conf.db import SessionLocal
# from entity.models import Student, Grade, Subject, Teacher, Group
#
#
# # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
# def select_01(session: Session):
#     query = (
#         select(Student, func.avg(Grade.grade).label("avg_grade"))
#         .join(Grade)
#         .group_by(Student.id)
#         .order_by(desc("avg_grade"))
#         .limit(5)
#     )
#
#     return session.execute(query).all()
#
#
# # Знайти студента із найвищим середнім балом з певного предмета.
# def select_02(session: Session, subject_id: int):
#     stmt = (
#         select(Student, func.avg(Grade.grade).label("avg_grade"))
#         .join(Grade)
#         .where(Grade.subject_id == subject_id)
#         .group_by(Student.id)
#         .order_by(desc("avg_grade"))
#         .limit(1)
#     )
#     return session.execute(stmt).first()
#
#
# # Знайти оцінки студентів у окремій групі з певного предмета
# def select_07(session: Session, group_id: int, subject_id: int):
#     stmt = (
#         select(Student.name, Grade.grade, Grade.date_received)
#         .join(Grade)
#         .where(Grade.subject_id == subject_id, Student.group_id == group_id)
#     )
#     return session.execute(stmt).all()
#
#
# # Оцінки студентів у певній групі з певного предмета на останньому занятті
#
#
# if __name__ == "__main__":
#     session: Session = SessionLocal()
#
#     result_01 = select_01(session)
#     result_02 = select_02(session, 2)
#     result_07 = select_07(session, 3, 1)
#     print("Знайти 5 студентів із найбільшим середнім балом з усіх предметів:", result_01)
#     print("Знайти студента із найвищим середнім балом з певного предмета:", result_02)
#     print("Знайти оцінки студентів у окремій групі з певного предмета:", result_07)
