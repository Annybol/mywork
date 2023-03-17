#grades stores a student name and a list of her grades in a dict
# Author Anne Boland



student = {
"name":"Mary",
    "modules":[{"courseName":"Programming",
    "grade": 45},
    {"courseName":"History",
    "grade": 99}]
}
print ("Student:{}".format(student["name"]))
for module in student ["modules"]:
    print ("\t:{}\t{}".format(module["courseName"],module["grade"]))