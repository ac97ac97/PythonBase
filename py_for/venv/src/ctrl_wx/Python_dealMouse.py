import wx


#自定义窗口类MyFrame

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title='鼠标点击事件',size=(400,300))
        self.Center()  #设置窗口居中
        self.Bind(wx.EVT_LEFT_DOWN,self.on_left_down) #鼠标按下事件
        self.Bind(wx.EVT_LEFT_UP,self.on_left_up)    #鼠标释放事件
        self.Bind(wx.EVT_MOTION,self.on_mouse_move)

    def on_left_down(self,evt):
        print('鼠标按下')
    def on_left_up(self,evt):
        print('鼠标释放')
    def on_mouse_move(self,event):
        if event.Dragging() and event.LeftIsDown():  #判断鼠标是否右键拖拽
            pos=event.GetPosition()  #获得鼠标的位置
            print(pos)

class App(wx.App):
    def OnInit(self):
        #创建窗口对象
        frame=MyFrame()
        frame.Show()
        return True

if __name__ == '__main__':
    app=App()
    app.MainLoop()  #进入主事件循环