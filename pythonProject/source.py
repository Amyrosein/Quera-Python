class Grade:
    def __init__(self, stu_id, crc_code, score):
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score


class CourseUtil:
    def __init__(self):
        self.__lines = None
        self.__f = None
        self.__address = None
        self.__file = None

    def set_file(self, address):
        self.__address = address
        self.__f = open(address, 'r+')
        self.__file = self.__f.read()
        lines = self.__file.splitlines()
        for k in range(len(lines)):
            lines[k] = lines[k].split()
            for i in range(3):
                if i == 2:
                    lines[k][i] = float(lines[k][i])
                else:
                    lines[k][i] = int(lines[k][i])
        self.__lines = lines
        self.__f.close()
        return self.__lines

    def load(self, line_number):
        if line_number > len(self.__lines):
            return None
        else:
            new_line = self.__lines[line_number - 1]
            return Grade(int(new_line[0]), int(new_line[1]), float(new_line[2]))

    def calc_student_average(self, student_id):
        c = 0
        s = 0.0
        for line in self.__lines:
            if line[0] == student_id:
                s += line[2]
                c += 1
        return s/c

    def calc_course_average(self, course_code):
        c = 0
        s = 0.0
        for line in self.__lines:
            if line[1] == course_code:
                s += line[2]
                c += 1
        return s/c

    def count(self):
        return len(self.set_file(self.__address))

    def save(self, grade):
        in_line = True
        new = f"\n{grade.student_id} {grade.course_code} {grade.score}"
        for line in self.__lines:
            if line[0] == grade.student_id and line[1] == grade.course_code:
                old = f'{line[0]} {line[1]} {line[2]}'
                n = f"{grade.student_id} {grade.course_code} {grade.score}"
                new_file = self.__file.replace(old, n)
                in_line = False
                with open(self.__address, "w") as f:
                    f.write(new_file)
        if in_line:
            with open(self.__address, "a") as f:
                f.write(new)