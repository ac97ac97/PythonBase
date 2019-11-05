import wx


# 自定义MyFrame类

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='树控件', size=(500, 400))
        self.Center()  # 设置窗口居中

        splitter = wx.SplitterWindow(self)
        leftpanel = wx.Panel(splitter)
        rightpanel = wx.Panel(splitter)
        splitter.SplitVertically(leftpanel, rightpanel, 200)
        splitter.SetMinimumPaneSize(80)

        self.tree = self.CreateTreeCtrl(leftpanel)
        self.Bind(wx.EVT_TREE_SEL_CHANGING, self.on_click, self.tree)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(self.tree, 1, flag=wx.ALL | wx.EXPAND, border=5)
        leftpanel.SetSizer(vbox1)

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        self.content = wx.StaticText(rightpanel, label='右侧面板')
        vbox2.Add(self.content, 1, flag=wx.ALL | wx.EXPAND, border=5)
        rightpanel.SetSizer(vbox2)

    def on_click(self, event):
        item = event.GetItem()
        self.content.SetLabel(self.tree.GetItemText(item))

    def CreateTreeCtrl(self, parent):
        tree = wx.TreeCtrl(parent)

        items = []
        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, size=wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, size=wx.Size(16, 16)))
        tree.AssignImageList(imglist)

        root = tree.AddRoot("TreeRoot", image=0)

        items.append(tree.AppendItem(root, 'Item 1', 0))
        items.append(tree.AppendItem(root, 'Item 2', 0))
        items.append(tree.AppendItem(root, 'Item 3', 0))
        items.append(tree.AppendItem(root, 'Item 4', 0))
        items.append(tree.AppendItem(root, 'Item 5', 0))

        for ii in range(len(items)):
            id = items[ii]
            tree.AppendItem(id, "Sumbitem 1", 1)
            tree.AppendItem(id, "Sumbitem 2", 1)
            tree.AppendItem(id, "Sumbitem 3", 1)
            tree.AppendItem(id, "Sumbitem 4", 1)
            tree.AppendItem(id, "Sumbitem 5", 1)

        tree.Expand(root) #展开根下子节点
        tree.Expand(items[0]) #展开Item 1下子节点
        tree.Expand(items[3]) #展开Item 4下子节点
        tree.SelectItem(root)#选中根节点tree.Expand(root)
        return tree


class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
