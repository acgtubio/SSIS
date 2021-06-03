import sqlite3
from sqlite3.dbapi2 import connect
from typing import final

class DBHandling:
    __tableCreated = False

    @classmethod
    def getStudentData(cls, args = ""):
        #params are table columns, args are specific values from a column

        if not cls.__tableCreated:
            cls.__createTable()

        conn = sqlite3.connect("sis.db")
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        try:
            data = c.execute(f"""
                SELECT * FROM students {args}
            """).fetchall()
        except Exception as e:
            return -1
        finally:
            conn.close()

        return data

    @classmethod
    def updateStudentData(cls, info):
        if not cls.__tableCreated:
            cls.__createTable()

        conn = sqlite3.connect("sis.db")
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute(f"""
            UPDATE students 
            SET last_name = ?, 
                first_name = ?, 
                middle_name = ?,
                year = ?,
                gender = ?,
                course = ?
            WHERE id = ?
        """, info)

        conn.commit()
        conn.close()

    @classmethod
    def pushStudentData(cls, info):
        if not cls.__tableCreated:
            cls.__createTable()
        

        conn = sqlite3.connect("sis.db")
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute("INSERT INTO students VALUES(?, ?, ?, ?, ?, ?, ?)", info)

        conn.commit()
        conn.close()
        return 1

    @classmethod
    def __createTable(cls):
        #private method for creating tables in case tables do not exist in the database.
        conn = sqlite3.connect("sis.db")
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute("""
            CREATE TABLE IF NOT EXISTS courses(
                course_code CHAR(10),
                course_name VARCHAR(150),
                PRIMARY KEY(course_code)
            );
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id CHAR(9),
                last_name VARCHAR(50),
                first_name VARCHAR(50),
                middle_name VARCHAR(50),
                year CHAR(15),
                gender VARCHAR(50),
                course CHAR(10),
                PRIMARY KEY(id),
                FOREIGN KEY(course) REFERENCES courses(course_code)
            );
        """)
        conn.close()
        cls.__tableCreated = True

    @classmethod
    def getCourseData(cls, args = ""):
        if (not cls.__tableCreated):
            cls.__createTable()
        
        conn = sqlite3.connect("sis.db")
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        data = c.execute(f"SELECT * FROM courses {args}").fetchall()

        conn.close()

        return data

    @classmethod
    def pushCourseData(cls, info):
        if not cls.__tableCreated:
            cls.__createTable()

        conn = sqlite3.connect("sis.db")
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute("""
            INSERT INTO courses VALUES(?,?)
        """, info)

        conn.commit()
        conn.close()
    
    @classmethod
    def updateCourseData(cls, info):
        if not cls.__tableCreated:
            cls.__createTable()

        conn = sqlite3.connect("sis.db")
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute("""
            UPDATE courses
            SET course_name = ?
            WHERE course_code = ?
        """, info)

        conn.commit()
        conn.close()

    @classmethod
    def delCourseData(cls, info):
        if not cls.__tableCreated:
            cls.__createTable()

        conn = sqlite3.connect("sis.db")
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        try:
            c.execute(f"""
                DELETE FROM courses
                WHERE course_code = \'{info}\'
            """)
        except Exception as e:
            return -1
        else:
            conn.commit()
        finally:
            conn.close()
        

    @classmethod
    def delStudentData(cls, id):
        if not cls.__tableCreated:
            cls.__createTable()

        conn = sqlite3.connect("sis.db")
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute(f"""
            DELETE FROM students
            WHERE id = \'{id}\'
        """)

        conn.commit()
        conn.close()

    @classmethod
    def getStudentCourse(cls, cond = ""):
        if not cls.__tableCreated:
            cls.__createTable()

        conn = sqlite3.connect("sis.db")
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        data = c.execute(f"""
            SELECT * FROM 
            students INNER JOIN courses 
            ON students.course = courses.course_code 
            {cond}
        """).fetchall()
        
        conn.close()

        return data

    @staticmethod
    def testAdd():
        a = "BSCS"
        b = "BS in Computer Science"
        conn = sqlite3.connect("sis.db")
        c = conn.cursor()
        c.execute("INSERT INTO courses(course_code, course_name) VALUES (?, ?)", (a,b))
        conn.commit()
        conn.close()
        
