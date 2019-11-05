import xml.etree.ElementTree as ET
#ElementTree解析xml文件
# tree=ET.parse('F:\\Python_project\\py_for\\venv\\src\\ctrl_dataChangeFormat\\data\\Notes.xml') #通过parse方法创建xml文档树
# print(type(tree))
# root=tree.getroot()  #root是根元素
# print(type(root))
# print(root.tag)
# for index,child in enumerate(root):
#     print('第{0}个{1}个元素,属性{2}'.format(index,child.tag,child.attrib))  #遍历5个子元素
#     for i,child_child in enumerate(child):
#         print('   标签: {0}   内容: {1}'.format(child_child.tag,child_child.text)) #遍历每个子元素下的子标签


tree=ET.parse('F:\\Python_project\\py_for\\venv\\src\\ctrl_dataChangeFormat\\data\\Notes.xml') #通过parse方法创建xml文档树
root=tree.getroot()  #root是根元素

node=root.find('./Node')  #当前节点的下一个Note子节点
print(node.tag,node.attrib)
node=root.find('./Node/CDate')#Node节点下的CDate节点
print(node.text)

node=root.find('./Node/CDate/..')#Node节点
print(node.tag,node.attrib)
node=root.find('.//CDate') #当前节点查找所有后代中第一个CDate节点
print(node.text)

node=root.find('./Node[@id]')#具有id属性的node节点
print(node.tag,node.attrib)

node=root.find("./Node[@id='2']")#id属性等于2的node节点
print(node.tag,node.attrib)

node=root.find('./Node[2]')#第二个node节点
print(node.tag,node.attrib)

node=root.find('./Node[last()]')#最后一个node节点
print(node.tag,node.attrib)

node=root.find('./Node[last() -2]')# 倒数第二个node节点
print(node.tag,node.attrib)