import wx


# 自定义窗口MyFrame类
class MyFrame(wx.Frame):
    def __init__(self):
        #        绝对布局
        super().__init__(parent=None, title='一对一事件处理', size=(400, 200))
        self.Center()
        panel = wx.Panel(parent=self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(3, 2, 10, 10)
        useid = wx.StaticText(panel, label='用户ID:')
        pwd = wx.StaticText(panel, label='用户密码：')
        content = wx.StaticText(panel, label='多行文本：')
        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        #设置tc1的初始值
        tc1.SetValue('Tony')
        #获取tc1的值
        print('读取用户名:{0}'.format(tc1.GetValue()))
        fgs.AddMany([
            useid,(tc1,1,wx.EXPAND),
            pwd,(tc2,1,wx.EXPAND),
            content,(tc3,wx.EXPAND)
        ])
        fgs.AddGrowableRow(0, 1)
        fgs.AddGrowableRow(1, 1)
        fgs.AddGrowableRow(2, 3)
        fgs.AddGrowableCol(0, 1)
        fgs.AddGrowableCol(1, 2)
        hbox.Add(fgs,proportion=1,flag=wx.ALL | wx.EXPAND,border=15)
        panel.SetSizer(hbox)

class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
