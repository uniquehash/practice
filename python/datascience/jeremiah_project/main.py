# python

import pymysql.cursors
import csv

connection = pymysql.connect(host='localhost',
                             user='oliverbelanger',
                             # password='defaultword',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)




def create_jobs(connection):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            create_table = """CREATE TABLE jobs (
                `id` int(11) NOT NULL AUTO_INCREMENT,
                `employed` int(15) NOT NULL,
                `agriculture` int(1) NOT NULL,
                `race` char(50) NOT NULL,
                `year`  int(4)  NOT NULL,                
                PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;"""
            cursor.execute(create_table)
        connection.commit()
    finally:
        print "jobs table created"        

def fill_jobs_table(connection):
    with open('jobs.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:        
            try:
                with connection.cursor() as cursor:
                    insert = "INSERT INTO jobs (`employed`, `race`, `year`, `agriculture`) VALUES (%s, %s, %s, %s)"
                    cursor.execute(insert, (int(row['employed'].replace(",", "") if "," in row['employed'] else row['employed']), row['race'], int( row['year'] if "," in row['year'] else row['year']), int( row['agriculture'].replace(",", "") if "," in row['agriculture'] else row['agriculture'])))
                    connection.commit()                
            finally: 
                print "jobs table filled"




setup = 1;
if setup == 0:
    create_jobs(connection)
    fill_jobs_table(connection)

print "\nWhat was the change in employment in the agriculture sector between 2014 and 2015 for each race?"
try:
    with connection.cursor() as cursor:
        select = "SELECT employed FROM jobs where year=%s and race=%s and agriculture=%s"
        cursor.execute(select, ('2014', 'black', '1'))
        black_emp_1_2014 = cursor.fetchone()[u'employed']
        select = "SELECT employed FROM jobs where year=%s and race=%s and agriculture=%s"
        cursor.execute(select, ('2015', 'black', '1'))
        black_emp_1_2015 = cursor.fetchone()[u'employed']
        perc_black = float(black_emp_1_2015 - black_emp_1_2014) / float(black_emp_1_2014)
        
        select = "SELECT employed FROM jobs where year=%s and race=%s and agriculture=%s"
        cursor.execute(select, ('2014', 'white', '1'))
        white_emp_1_2014 = cursor.fetchone()[u'employed']
        select = "SELECT employed FROM jobs where year=%s and race=%s and agriculture=%s"
        cursor.execute(select, ('2015', 'white', '1'))
        white_emp_1_2015 = cursor.fetchone()[u'employed']
        perc_white = float(white_emp_1_2015 - white_emp_1_2014) / float(white_emp_1_2014)

        select = "SELECT employed FROM jobs where year=%s and race=%s and agriculture=%s"
        cursor.execute(select, ('2014', 'asian', '1'))
        asian_emp_1_2014 = cursor.fetchone()[u'employed']
        select = "SELECT employed FROM jobs where year=%s and race=%s and agriculture=%s"
        cursor.execute(select, ('2015', 'asian', '1'))
        asian_emp_1_2015 = cursor.fetchone()[u'employed']
        perc_asian = float(asian_emp_1_2015 - asian_emp_1_2014) / float(asian_emp_1_2014)

        print "black -> 2014:", black_emp_1_2014, "\t2015:", black_emp_1_2015, "\tchange:", perc_black
        print "white -> 2014:", white_emp_1_2014, "\t2015:", white_emp_1_2015, "\tchange:", perc_white
        print "asian -> 2014:", asian_emp_1_2014, "\t2015:", asian_emp_1_2015, "\tchange:", perc_asian, "\n"
finally: 
    pass

print "What was the change in employment in the non-agriculture sector between 2014 and 2015 for each race?"
try:    
    with connection.cursor() as cursor:
        select = "SELECT employed FROM jobs where year=%s and race=%s and agriculture=%s"
        cursor.execute(select, ('2014', 'black', '0'))
        nonblack_emp_1_2014 = cursor.fetchone()[u'employed']
        select = "SELECT employed FROM jobs where year=%s and race=%s and agriculture=%s"
        cursor.execute(select, ('2015', 'black', '0'))
        nonblack_emp_1_2015 = cursor.fetchone()[u'employed']
        nonperc_black = float(nonblack_emp_1_2015 - nonblack_emp_1_2014) / float(nonblack_emp_1_2014)
        
        select = "SELECT employed FROM jobs where year=%s and race=%s and agriculture=%s"
        cursor.execute(select, ('2014', 'white', '0'))
        nonwhite_emp_1_2014 = cursor.fetchone()[u'employed']
        select = "SELECT employed FROM jobs where year=%s and race=%s and agriculture=%s"
        cursor.execute(select, ('2015', 'white', '0'))
        nonwhite_emp_1_2015 = cursor.fetchone()[u'employed']
        nonperc_white = float(nonwhite_emp_1_2015 - nonwhite_emp_1_2014) / float(nonwhite_emp_1_2014)

        select = "SELECT employed FROM jobs where year=%s and race=%s and agriculture=%s"
        cursor.execute(select, ('2014', 'asian', '0'))
        nonasian_emp_1_2014 = cursor.fetchone()[u'employed']
        select = "SELECT employed FROM jobs where year=%s and race=%s and agriculture=%s"
        cursor.execute(select, ('2015', 'asian', '0'))
        nonasian_emp_1_2015 = cursor.fetchone()[u'employed']
        nonperc_asian = float(nonasian_emp_1_2015 - nonasian_emp_1_2014) / float(nonasian_emp_1_2014)

        print "black -> 2014:", nonblack_emp_1_2014, "\t2015:", nonblack_emp_1_2015, "\t\tchange:", nonperc_black
        print "white -> 2014:", nonwhite_emp_1_2014, "\t2015:", nonwhite_emp_1_2015, "\tchange:", nonperc_white
        print "asian -> 2014:", nonasian_emp_1_2014, "\t2015:", nonasian_emp_1_2015, "\t\tchange:", nonperc_asian, "\n"
finally: 
    pass

print "What was the change in employment in all sectors between 2014 and 2015 for each race?"

a = float((nonblack_emp_1_2015 + black_emp_1_2014) - (nonblack_emp_1_2014 + black_emp_1_2014)) / float(nonblack_emp_1_2014 + black_emp_1_2014)
b = float((nonwhite_emp_1_2015 + white_emp_1_2014) - (nonwhite_emp_1_2014 + white_emp_1_2014)) / float(nonwhite_emp_1_2014 + white_emp_1_2014)
c = float((nonasian_emp_1_2015 + asian_emp_1_2014) - (nonasian_emp_1_2014 + asian_emp_1_2014)) / float(nonasian_emp_1_2014 + asian_emp_1_2014)

print "black -> 2014:", nonblack_emp_1_2014 + black_emp_1_2014, "\t2015:", nonblack_emp_1_2015 + black_emp_1_2014, "\t\tchange:", a
print "white -> 2014:", nonwhite_emp_1_2014 + white_emp_1_2014, "\t2015:", nonwhite_emp_1_2015 + white_emp_1_2014, "\tchange:", b
print "asian -> 2014:", nonasian_emp_1_2014 + asian_emp_1_2014, "\t2015:", nonasian_emp_1_2015 + asian_emp_1_2014, "\t\tchange:", c, "\n"



# with connection.cursor() as cursor:
# # Read a single record
# sql = "SELECT `*` FROM `aggricultural`"
# cursor.execute(sql)
# result = cursor.fetchone()
# print(result)        


connection.close()
