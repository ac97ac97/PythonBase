import wx


# 自定义MyFrame类
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='静态图片控件', size=(300, 300))
        self.bmps = [wx.Bitmap('F:\\Python_project\\py_for\\venv\\src\\ctrl_wx\\imgs\\1.gif', wx.BITMAP_TYPE_GIF),
                     wx.Bitmap('F:\\Python_project\\py_for\\venv\\src\\ctrl_wx\\imgs\\2.gif', wx.BITMAP_TYPE_GIF),
                     wx.Bitmap('F:\\Python_project\\py_for\\venv\\src\\ctrl_wx\\imgs\\1.gif', wx.BITMAP_TYPE_GIF)
                     ]
        self.Center()  # 设置窗口垂直
        self.panel = wx.Panel(parent=self)
        # 创建垂直方向上的box布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)

        b1 = wx.Button(parent=self.panel, id=1, label='Button1')
        b2 = wx.Button(self.panel, id=2, label='Button2')
        self.Bind(wx.EVT_BUTTON, self.on_click, id=1, id2=2)

        self.image = wx.StaticBitmap(self.panel, -1, self.bmps[0])

        # 添加标控件1到布局管理器中

        vbox.Add(b1, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(b2, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(self.image,proportion=3,flag=wx.CENTER)

        self.panel.SetSizer(vbox)

    def on_click(self, event):

        event_id = event.GetId()
        if event_id == 1:
            self.image.SetBitmap(self.bmps[1])
        else:
            self.image.SetBitmap(self.bmps[2])
            #切换图片需要重新绘制窗口 否则会发生混乱
            self.panel.Layout()


class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
