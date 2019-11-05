import  json

#json数据编码  dumps() 结果以字符串形式进行返回  dump 结果以对象的形式进行返回

# py_dict={'name':'Tony','age':12,'sex':True} #创建字典对象
# py_list=[1,3]  #创建列表对象
# py_tuple=('A','B','C')#创建元祖对象
#
# py_dict['a'] = py_list #添加列表到字典中
# py_dict['b'] =py_tuple #添加元祖到字典中
#
# print(py_dict)
# print(type(py_dict))
#
# #编码过程(返回字符串)
# json_obj=json.dumps(py_dict)
# print(json_obj)
# print(type(json_obj))
#
# #编码过程
# json_obj=json.dumps(py_dict,indent=4)
#
# #输出格式化后的字符串
# print(json_obj)
#
# #将json文件写到data1.json文件中
# with open('F:\\Python_project\\py_for\\venv\\src\\ctrl_dataChangeFormat\\data\\data1.json','w') as f:
#     json.dump(py_dict,f)
#
# #将json文件写到data2.json文件中
#
# with open('F:\\Python_project\\py_for\\venv\\src\\ctrl_dataChangeFormat\\data\\data2.json','w') as f:
#     json.dump(py_dict,f,indent=4)


#json 数据解码 loads()将json数据的字符串尽行解码load()读取文件和流对其中的json数据进行解析 二者最终都是返回Python数据   如果json数据中含有多个数组还需要使用for循环进行逐层剥离进行解析

#准备数据
json_obj=r'{"name": "Tony", "age": 12, "sex": true, "a": [1, 3], "b": ["A", "B", "C"]}'
py_dict=json.loads(json_obj)
print(type(py_dict))
print(py_dict['name'])
print(py_dict['age'])
print(py_dict['sex'])

py_lista=py_dict['a'] #获取列表
print(py_lista)

py_listb=py_dict['b'] #获取列表
print(py_listb)

#读取json数据从data2.json文件
with open('F:\\Python_project\\py_for\\venv\\src\\ctrl_dataChangeFormat\\data\\data2.json','r') as f:
    data=json.load(f)
    print(data)
    print(type(data))


