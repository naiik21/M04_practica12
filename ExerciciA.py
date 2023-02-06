import xml.etree.ElementTree as ET

students = ET.Element("students")

s1 = ET.SubElement(students, "student")
s2 = ET.SubElement(students, "student")
s3 = ET.SubElement(students, "student")
s4 = ET.SubElement(students, "student")
s5 = ET.SubElement(students, "student")

n = ET.SubElement(s1, "name")
n.text = "Pedro"
sn = ET.SubElement(s1, "surname")
sn.text = "Abascal"
em = ET.SubElement(s1, "email")
em.text = "pedrito23@gmail.com"
dni = ET.SubElement(s1, "dni")
dni.text = "74648244V"

n2 = ET.SubElement(s2, "name")
n2.text = "Manolo"
sn2 = ET.SubElement(s2, "surname")
sn2.text = "Gutierrez"
em2 = ET.SubElement(s2, "email")
em2.text = "manolitoklk@gmail.com"
dni2 = ET.SubElement(s2, "dni")
dni2.text = "52918493L"

n3 = ET.SubElement(s3, "name")
n3.text = "Naiara"
sn3 = ET.SubElement(s3, "surname")
sn3.text = "Garcia"
em3 = ET.SubElement(s3, "email")
em3.text = "naigarcia@gmail.com"
dni3 = ET.SubElement(s3, "dni")
dni3.text = "67154298Y"

n4 = ET.SubElement(s4, "name")
n4.text = "Laura"
sn4 = ET.SubElement(s4, "surname")
sn4.text = "Martin"
em4 = ET.SubElement(s4, "email")
em4.text = "laura2003@gmail.com"
dni4 = ET.SubElement(s4, "dni")
dni4.text = "15258795M"

n5 = ET.SubElement(s5, "name")
n5.text = "Javi"
sn5 = ET.SubElement(s5, "surname")
sn5.text = "Lama"
em5 = ET.SubElement(s5, "email")
em5.text = "javito88@gmail.com"
dni5 = ET.SubElement(s5, "dni")
dni5.text = "46321865S"

tree = ET.ElementTree(students)
tree.write("xml-Raul.xml")

ET.indent(students)
def xml():
    ET.dump(students)
