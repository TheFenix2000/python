from docx import Document
from docx.enum.section import WD_SECTION_START


document = Document()

#dostęp do sekcji
sections = document.sections
section = sections[0]
for section in sections:
    print(section.start_type)

#dodawanie sekcji
    #current_section = document.sections[-1]  # last section in document
    #print(current_section.start_type)
new_section = document.add_section(WD_SECTION_START.ODD_PAGE)#nazwa next sekcji
print(new_section.start_type)


document.save('sections_document.docx')