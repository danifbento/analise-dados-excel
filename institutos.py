import openpyxl
import unidecode
wb = openpyxl.load_workbook("WCNeutras_respostas_full.xlsx")

ws = wb['Sheet1']

B = ws['B']

b_header = B[0].value

instituto = {}

for cell in B:
    if cell.value == b_header or cell.value == 'Outra':
        continue

    if cell.value in instituto.keys():
        continue

    instituto[cell.value] = True

for k in instituto.keys():
    print(k)

print("===")

C = ws['C']

c_header = C[0].value

other_instituto = {}

mapping = {}
mapping['up'] = 'universidade do porto'
mapping['ips'] = 'instituto politecnico setubal'
mapping['ufp'] = 'universidade fernando pessoa'
mapping['isel'] = 'instituto superior engenharia lisboa'
mapping['ispa'] = 'instituto superior psicologia aplicada'
mapping['faul'] = 'faculdade de artes universidade lisboa'
mapping['isep'] = 'instituto superior educacao personalizada'
mapping['fcup'] = 'faculdade de ciencias universidade porto'
mapping['university of lisbon'] = 'universidade lisboa'
mapping['imm'] = 'instituto medicina molecular'
mapping['escs'] = 'escola superior ciencias saude'
mapping['unl'] = 'universidade nova lisboa'
mapping['iscte'] = 'instituto universitario lisboa'
mapping['nova'] = 'universidade nova lisboa'
mapping['fpul'] = 'faculdade psicologia universidade lisboa'
mapping['ulisboa'] = 'universidade lisboa'
mapping['university'] = 'universidade'
mapping['lisbon'] = 'lisboa'
mapping['ubi'] = 'universidade beira interior'

count = 0
for cell in C:
    if cell.value == c_header or cell.value is None:
        continue

    s = str(cell.value).lower().strip()
    s = unidecode.unidecode(s)
    s = s.replace("  ", " ")
    s = s.replace(":", "")
    s = s.replace(" da ", " ")
    s = s.replace(" do ", " ")
    s = s.replace(" de ", " ")
    s = s.replace(" - ", " ")

    if s in mapping.keys():
        s = mapping[s]

    if s in other_instituto.keys():
        continue

    other_instituto[s] = cell.value
    count+=1

for k in other_instituto.keys():
    print(other_instituto[k], " -> ", k)

print("===")
print(count)