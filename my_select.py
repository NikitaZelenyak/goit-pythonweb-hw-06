from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from entity.models import Student, Grade, Subject, Teacher, Group
from conf.db import SessionLocal

def select_1():
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    with SessionLocal() as session:
        result = session.query(Student.name, func.avg(Grade.grade).label("avg_grade")) \
            .join(Grade) \
            .group_by(Student.id) \
            .order_by(desc("avg_grade")) \
            .limit(5).all()
    print("Топ 5 студентів із найвищим середнім балом:", result)
    return result


def select_2(subject_id: int):
    """Знайти студента із найвищим середнім балом з певного предмета."""
    with SessionLocal() as session:
        result = session.query(Student.name, func.avg(Grade.grade).label("avg_grade")) \
            .join(Grade) \
            .filter(Grade.subject_id == subject_id) \
            .group_by(Student.id) \
            .order_by(desc("avg_grade")) \
            .first()
    print(f"Студент із найвищим середнім балом з предмета {subject_id}:", result)
    return result


def select_3(subject_id: int):
    """Знайти середній бал у групах з певного предмета."""
    with SessionLocal() as session:
        result = session.query(Group.name, func.avg(Grade.grade).label("avg_grade")) \
            .join(Student).join(Grade) \
            .filter(Grade.subject_id == subject_id) \
            .group_by(Group.id).all()
    print(f"Середній бал у групах з предмета {subject_id}:", result)
    return result


def select_4():
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""
    with SessionLocal() as session:
        result = session.query(func.avg(Grade.grade)).scalar()
    print("Середній бал на потоці:", result)
    return result


def select_5(teacher_id: int):
    """Знайти які курси читає певний викладач."""
    with SessionLocal() as session:
        result = session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()
    print(f"Курси, які читає викладач {teacher_id}:", result)
    return result


def select_6(group_id: int):
    """Знайти список студентів у певній групі."""
    with SessionLocal() as session:
        result = session.query(Student.name, Student.last_name) \
            .filter(Student.group_id == group_id).all()
    print(f"Список студентів у групі {group_id}:", result)
    return result


def select_7(group_id: int, subject_id: int):
    """Знайти оцінки студентів у окремій групі з певного предмета."""
    with SessionLocal() as session:
        result = session.query(Student.name, Grade.grade, Grade.date_received) \
            .join(Grade) \
            .filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()
    print(f"Оцінки студентів у групі {group_id} з предмета {subject_id}:", result)
    return result


def select_8(teacher_id: int):
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    with SessionLocal() as session:
        result = session.query(func.avg(Grade.grade)) \
            .join(Subject) \
            .filter(Subject.teacher_id == teacher_id).scalar()
    print(f"Середній бал, який ставить викладач {teacher_id}:", result)
    return result


def select_9(student_id: int):
    """Знайти список курсів, які відвідує певний студент."""
    with SessionLocal() as session:
        result = session.query(Subject.name).join(Grade) \
            .filter(Grade.student_id == student_id).distinct().all()
    print(f"Курси, які відвідує студент {student_id}:", result)
    return result


def select_10(student_id: int, teacher_id: int):
    """Список курсів, які певному студенту читає певний викладач."""
    with SessionLocal() as session:
        result = session.query(Subject.name).join(Grade) \
            .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).distinct().all()
    print(f"Курси, які читає студенту {student_id} викладач {teacher_id}:", result)
    return result


# Виконання функцій та вивід результатів у консоль
if __name__ == "__main__":
    print("\n--- Виконання SQL-запитів ---\n")

    select_1()
    select_2(subject_id=1)
    select_3(subject_id=1)
    select_4()
    select_5(teacher_id=1)
    select_6(group_id=1)
    select_7(group_id=1, subject_id=1)
    select_8(teacher_id=1)
    select_9(student_id=1)
    select_10(student_id=1, teacher_id=1)

    print("\n--- Завершення виконання ---")