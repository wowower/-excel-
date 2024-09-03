import pandas as pd
class Student:
    math_grade=0
    chinese_grade=0
    english_grade=0
    geography_grade=0
    history_grade=0
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def set_math_grade(self,math_grade):
        self.math_grade=math_grade
    def set_chinese_grade(self,chinese_grade):
        self.chinese_grade=chinese_grade
    def set_english_grade(self,english_grade):
        self.english_grade=english_grade
    def set_geography_grade(self,geography_grade):
        self.geography_grade=geography_grade
    def set_history_grade(self,history_grade):
        self.history_grade=history_grade
    def get_total_grade(self):
        return self.math_grade+self.chinese_grade+self.english_grade+self.geography_grade+self.history_grade

    @staticmethod
    def read_students_from_excel(file_path):
        # 读取Excel文件
        df = pd.read_excel(file_path)

        students = []
        for index, row in df.iterrows():
            student = Student(row['name'], row['age'], row['gender'])
            student.set_math_grade(row['math'])
            student.set_chinese_grade(row['chinese'])
            student.set_english_grade(row['English'])
            student.set_geography_grade(row['geography'])
            student.set_history_grade(row['history'])
            students.append(student)

        return students
if __name__ == '__main__':
    file_path = 'grade.xls'
    students = Student.read_students_from_excel(file_path)
    while True:
        print('请输入你要查找的学生姓名：')

        name = input()
        if name == 'q':
            print("退出查找！")
            break
        for student in students:
            if student.get_name() == name:
                print(
                    f"Name: {student.get_name()}, Age: {student.get_age()}, Gender: {student.get_gender()}, Total Grade: {student.get_total_grade()}")
                break
        else:
            print("没有找到该学生！")

