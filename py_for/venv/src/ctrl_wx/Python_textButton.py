import wx


# 自定义窗口MyFrame类
class MyFrame(wx.Frame):
    def __init__(self):
#        绝对布局
        super().__init__(parent=None, title='一对一事件处理', size=(300, 180))
        self.Center()
        panel = wx.Panel(parent=self)
        # 创建垂直方向的BOX布局管理器对象
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.statictext = wx.StaticText(parent=panel, label='StaticText1', style=wx.ALIGN_CENTER_HORIZONTAL)
        b1 = wx.Button(parent=panel, label='OK')
        self.Bind(wx.EVT_BUTTON, self.on_click, b1)
        b2 = wx.ToggleButton(panel, -1, 'ToggleButton')
        self.Bind(wx.EVT_BUTTON, self.on_click, b2)
        bmp = wx.Bitmap('F:\\Python_project\\py_for\\venv\\src\\ctrl_wx\\ic_collection.png', wx.BITMAP_TYPE_PNG)
        b3 = wx.BitmapButton(panel, -1, bmp)
        self.Bind(wx.EVT_BUTTON, self.on_click, b3)

        # 添加静态文本和按钮到box布局管理器中
        vbox.Add(100, 10, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
        vbox.Add(self.statictext, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
        vbox.Add(b1, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
        vbox.Add(b2, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
        vbox.Add(b3, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
        panel.SetSizer(vbox)

    def on_click(self, event):
        self.statictext.SetLabelText('Hello.World')
        print('ok')


class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
