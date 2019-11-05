# import wx
# import wx.grid
#
# data = [
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
#     ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1']
#
# ]
# column_names=['书籍编号','书籍名称','作者','出版社','出版日期','库存数量']
#
# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(parent=None, title='树控件', size=(500, 400))
#         self.Center()  # 设置窗口居中
#         self.grid=self.CreateGrid(self)
#         self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK,self.OnLabelLeftClick)
#
#     def OnLabelLeftClick(self,event):
#         print('RowIdx: {0}'.format(event.GetRow()))
#         print('ColIdx: {0}'.format(event.GetCol()))
#         print(data[event.GetRow()])
#         event.Skip()
#
#     def CreateGrid(self,parent):
#         grid=wx.grid.Grid(parent)
#         grid.CreateGrid(len(data),len(data[0]))
#
#         for row in range(len(data)):
#             for col in range(len(data[row])):
#                 grid.SetColLabelValue(col,column_names[col])
#                 grid.SetCellValue(row,col,data[row][col])
#         #设置行列自定调整
#
#         grid.AutoSize()
#         return grid
#
#
# class App(wx.App):
#     def OnInit(self):
#         # 创建窗口对象
#         frame = MyFrame()
#         frame.Show()
#         return True
#
#
# if __name__ == '__main__':
#     app = App()
#     app.MainLoop()  # 进入主事件循环


# 使用 gridTableBase类


import wx
import wx.grid

data = [
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
    ['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1']

]
column_names = ['书籍编号', '书籍名称', '作者', '出版社', '出版日期', '库存数量']


class MyGridTable(wx.grid.GridTableBase):
    def __init__(self):
        super().__init__()
        self.colLables = column_names

    def GetNumberCols(self):
        return len(data[0])

    def GetNumberRows(self):
        return len(data)

    def GetValue(self, row, col):
        return data[row][col]

    def GetColLabelValue(self, col):
        return self.colLables[col]


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='树控件', size=(500, 400))
        self.Center()  # 设置窗口居中
        self.grid = self.CreateGrid(self)
        self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.OnLabelLeftClick)

    def OnLabelLeftClick(self, event):
        print('RowIdx: {0}'.format(event.GetRow()))
        print('ColIdx: {0}'.format(event.GetCol()))
        print(data[event.GetRow()])
        event.Skip()

    def CreateGrid(self, parent):
        grid = wx.grid.Grid(parent)
        table=MyGridTable()
        grid.SetTable(table,True)



        # 设置行列自定调整

        grid.AutoSize()
        return grid


class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
