CREATE TABLE grades (
	stu_CWID	INTEGER(5)	UNSIGNED NOT NULL,
    course		TEXT	NOT NULL,
    grade		TEXT	NOT NULL,
    ins_CWID	TEXT	NOT NULL
);
CREATE TABLE instructors (
    CWID    INTEGER(5)  UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
    Name      TEXT    NOT NULL,
    Dept       TEXT    NOT NULL
);
CREATE TABLE students (
    CWID    INTEGER(5)  UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
    Name      TEXT    NOT NULL,
    Major       TEXT    NOT NULL
);
CREATE TABLE majors (
    Major       TEXT    NOT NULL,
    Course      TEXT    NOT NULL
);

-- prat 2
SELECT Name FROM students WHERE CWID='11461';
SELECT Major, COUNT(*) AS MajorCNT FROM students GROUP BY Major;
SELECT grade, MAX(GradeCNT) as maxGrade FROM (SELECT grade, COUNT(*) AS GradeCNT FROM grades GROUP BY grade) AS GradeCNTable;
SELECT students.Name, students.CWID, students.Major, grades.course, grades.grade FROM students, grades WHERE grades.stu_CWID = students.CWID;
SELECT students.Name, grades.course FROM students, grades WHERE grades.stu_CWID = students.CWID and grades.course LIKE 'SSW %';

CREATE TABLE instructors_re (
    CWID    INTEGER(5)  UNSIGNED NOT NULL,
    Name	TEXT    NOT NULL,
    Dept	TEXT    NOT NULL,
    course	TEXT	NOT NULL,
    stuNum	INTEGER(2)	NOT NULL
);