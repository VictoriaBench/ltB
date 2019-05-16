

import sys
import re


def getCourse(line):
    """Returns a learner name and course name from a specific line.

    arguments:
    line -- line in the .csv doc
    """
    l_name,c_name = line.rstrip().split("/")    ##EE1 fix -- "," --> "/"
    return l_name, c_name   #EE2 fix -- c_name, l_name --> l_name, c_name

def getCoursesForLects(lectsfn):
    """
    Returns a dictionary of courses that each lecturer is involved in in the format {'Lecturer': ['course', ...]}
        
    arguments:
    lectsfn -- lecture list file name
    """
    courses = {}  # dictionary: for each lect returns list of courses
    lf = open(lectsfn)
    for line in lf:
        lect, course = getCourse(line)
        if lect in courses: # is the lecturer in the dictionary
            courses[lect].append(course)  # add course to the list ##EE3 fix -- ...append(lect) --> ...append(course)
        else:
            courses[lect] = [course]  
    lf.close()
    return courses

def getExams(examfname):
    """returns a dictionary of exams and their corresponding dates and venues in alphabetical order. 
        
    arguments:
    examfname -- exam list file name
    """
    exams = {}
    for line in open(examfname):
        data = line.rstrip().split(",")
        exams[data[0]]=(data[1],data[2])
    return exams

def getTimeTable(courses,exams):
    """returns a list of lecturers with the names, dates and venues of each exam they have to invigilate 
    (in alphabetical order) 
        
    arguments:
    courses -- list of courses
    exams -- list of exams 
    """
    ttable = []  # nested list -- for each lect a list of exams
    for lect in sorted(courses.keys()):
        l_exams   = [] # build list of lecturer's exams
        l_courses = courses[lect] # get their courses
        for c in l_courses:
            if c not in exams:
                the_exam=("TBD","TBD")
            else:
                the_exam = exams[c]
            l_exams.append((c,the_exam))
        ttable.append((lect,l_exams)) # now we know the exams add it list
    return ttable

def showTimeTable(ttable):
    """Prints a timetable
        
    arguments:
    ttable -- timetable (returned by getTimeTable()).
    """
    for (lect, l_exams) in ttable:
        print(lect)
        for c,ex in l_exams:
            print("   ",c,ex[0],ex[1])
        

if __name__ == "__main__":
    examfn    = sys.argv[1]
    lectsfn     = sys.argv[2]
    courses    = getCoursesForLects(lectsfn)
    exams     = getExams(examfn)
    tt = getTimeTable(courses,exams)
    showTimeTable(tt)
