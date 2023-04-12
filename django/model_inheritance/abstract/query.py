from .models import Student, Teacher


# tables create:
#     - Student
#     - Teacher


Student.objects.create(name="s1", score=80)
# id  | name | score
# 1   | s1   | 80

Teacher.objects.create(name="t1", score=1000)
# id  | name | salary
# 1   | t1   | 1000
