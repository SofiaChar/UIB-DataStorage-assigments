import xml.etree.ElementTree as ET

root = ET.Element("emails")

email = ET.SubElement(root, "email")

# element
title = ET.SubElement(email, "title")
title.text = "Work contract"

#sender
sender = ET.SubElement(email, "sender")
sender_name = ET.SubElement(sender, "name")
sender_name.text = "Carlos Dou"
sender_email = ET.SubElement(sender, "email")
sender_email.text = "Carlos.Dou@apple.com"

# receivers
receivers = ET.SubElement(email, "receivers")
receiver = ET.SubElement(receivers, "receiver")
receiver_name = ET.SubElement(receiver, "name")
receiver_name.text = "Sofiia Charnota"
receiver_email = ET.SubElement(receiver, "email")
receiver_email.text = "Sofiia.Charnota@gmail.com"

# cc
cc = ET.SubElement(email, "cc")
cc_recipient = ET.SubElement(cc, "recipient")
cc_name = ET.SubElement(cc_recipient, "name")
cc_name.text = "Rob Joshua"
cc_email = ET.SubElement(cc_recipient, "email")
cc_email.text = "rob@apple.com"

# bcc
bcc = ET.SubElement(email, "bcc")
bcc_recipient = ET.SubElement(bcc, "recipient")
bcc_name = ET.SubElement(bcc_recipient, "name")
bcc_name.text = "Lana Parilla"
bcc_email = ET.SubElement(bcc_recipient, "email")
bcc_email.text = "lana@disney.com"

# daytime
daytime = ET.SubElement(email, "daytime")
daytime.text = "12.09.2023 10:20"

# content
content = ET.SubElement(email, "content")
content.text = "Hello! I wanted to tell you that you are hired for the position."

# links
links = ET.SubElement(email, "links")
link = ET.SubElement(links, "link")
link.text = "www.docs.com"

#  files
files = ET.SubElement(email, "files")
file = ET.SubElement(files, "file")
file.text = "Contract.pdf"

#  write
tree = ET.ElementTree(root)
with open("class_output.xml", "wb") as file:
    tree.write(file, encoding="utf-8")

