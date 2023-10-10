import xml.etree.ElementTree as ET

tree = ET.parse("class.xml")
root = tree.getroot()
for level in root:
    title = level.find('title').text
    print('Title: ', title)
    professors = level.find('professors')
    for p in professors:
        print('Prof: ', p.text)

    students = level.find('students')
    print('Students:')
    for s in students:
        print(s.find('name').text)
        print(s.find('surname').text)
        print()
