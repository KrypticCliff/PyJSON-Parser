# Written by Maxfield Gordon and Clifton Rawlings
# Last updated May 21, 2019
import json

with open("irb_data.json", "r") as read_file:
    data = json.load(read_file);

print(len(data))

results = {'Term': {} }

for i in range(0, len(data)):
    term = data[i]['TERM']
    results['Term'][term]= {'Course': {}}

'''
for term in results:
    results[term]['Course'] = {}
'''
for obj in data:
    term = obj['TERM']
    prefix = obj['COURSE_PREFIX']
    results['Term'][term]['Course'][prefix] = {'Course_Num': {} }

for obj in data:
    year = obj['YEAR']
    term = obj['TERM']
    college = obj['COLLEGE']
    dept = obj['DEPARTMENT']
    crsLevel = obj['COURSE_LEVEL']
    crsLab = obj['D_CRS_LAB']
    prefix = obj['COURSE_PREFIX']
    cnum = obj['COURSE_NUMBER']
    ge = obj['GE_COURSE']
    enrolled = obj['ENROLLED']
    enrFirst = obj['ENROLLED_FIRST_TIME']
    repeat = obj['ENROLLED_REPEATERS']
    repeatPer = obj['PERCENT_REPEATERS']

    results['Term'][term]['Course'][prefix]['Course_Num'][cnum] = {"Year": year, "Term": term, "College": college, "Department": dept, "Course_Level": crsLevel, "D_CRS_LAB": crsLab, "Course_Prefix": prefix, "Course_Num": cnum, "GE_Course": ge, "Enrolled": enrolled, "Enrolled_First_Time": enrFirst, "Repeaters": repeat, "Percent_Repeaters": repeatPer}

#for obj_num in course:


print(results)

#results = {'Term': {f'{variablename}': }}

json_pretty = json.dumps(results, indent = 4)
with open('classOut.json', 'w') as outfilePretty:
    outfilePretty.writelines(json_pretty)


#print(data[1]);
