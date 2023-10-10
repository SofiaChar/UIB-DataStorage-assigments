import xml.etree.ElementTree as ET

root = ET.Element("group")
subject = ET.SubElement(root, "subject")
title = ET.SubElement(subject, "title")
title.text = "ERD"

# Create the professors element
professors = ET.SubElement(subject, "professors")
professor_names = ["Jaume", "Belen"]
for n in professor_names:
    professor = ET.SubElement(professors, "name")
    professor.text = n

# Create the students element
students = ET.SubElement(subject, "students")

# Create and add student elements
student_names = ["Ikram","Sofiia","Amelia","Javi",]

for data in student_names:
    student = ET.SubElement(students, "student")
    student_name = ET.SubElement(student, "name")
    student_name.text = data

# Create an ElementTree object and write to a file
tree = ET.ElementTree(root)
with open("output.xml", "wb") as file:
    tree.write(file, encoding="utf-8")

print("XML file 'output.xml' has been generated.")