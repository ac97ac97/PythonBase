import csv
#reader pdf��encoding='gbk' ���лᱨ��֧�ָø�ʽ ��Ϊutf-8�������гɹ�
# with open('F:\\Python_project\\py_for\\venv\src\\ctrl_dataChangeFormat\\data\\book.csv','r',encoding='utf-8') as rf:
#     reader=csv.reader(rf,dialect=csv.excel)
#     for row in reader:
#         print('|'.join(row))

#writer pdf��encoding='gbk' ���лᱨ��֧�ָø�ʽ ��Ϊutf-8�������гɹ�
with open('F:\\Python_project\\py_for\\venv\src\\ctrl_dataChangeFormat\\data\\book.csv','r',encoding='utf-8') as rf:
    reader=csv.reader(rf)
    with open('F:\\Python_project\\py_for\\venv\src\\ctrl_dataChangeFormat\\data\\book2.csv', 'w', newline='',encoding='utf-8') as wf:
        writer=csv.writer(wf,delimiter='\t')
        for row in reader:
          print('|'.join(row))
          writer.writerow(row)