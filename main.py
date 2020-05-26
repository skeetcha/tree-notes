import wx

class TNFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(TNFrame, self).__init__(*args, **kw)
        pnl = wx.Panel(self)
        
        boxSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.treeCtrl = wx.TreeCtrl(self, -1, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)
        self.treeRoot = self.treeCtrl.AddRoot('No notebooks loaded')
        self.treeCtrl.Expand(self.treeRoot)
        boxSizer.Add(self.treeCtrl, 1, wx.ALL | wx.EXPAND, 5)

        self.noteBook = wx.Notebook(self, -1, wx.DefaultPosition, wx.DefaultSize, 0)
        boxSizer.Add(self.noteBook, 3, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(boxSizer)
        self.Layout()
        self.Centre(wx.BOTH)
        self.makeMenuBar()

    def makeMenuBar(self):
        fileMenu = wx.Menu()
        newItem = fileMenu.Append(-1, '&New...\tCtrl-N', 'Create a new notebook file')
        openItem = fileMenu.Append(-1, '&Open...\tCtrl-O', 'Open a notebook file')
        saveItem = fileMenu.Append(-1, '&Save...\tCtrl-S', 'Save the notebook file')
        saveAsItem = fileMenu.Append(-1, 'Save &As...\tCtrl-Shift-S', 'Save the notebook file somewhere else')
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        editMenu = wx.Menu()
        cutItem = editMenu.Append(wx.ID_CUT)
        copyItem = editMenu.Append(wx.ID_COPY)
        pasteItem = editMenu.Append(wx.ID_PASTE)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, '&File')
        menuBar.Append(editMenu, '&Edit')
        menuBar.Append(helpMenu, '&Help')

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnNew, newItem)
        self.Bind(wx.EVT_MENU, self.OnOpen, openItem)
        self.Bind(wx.EVT_MENU, self.OnSave, saveItem)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, saveAsItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)

        self.Bind(wx.EVT_MENU, self.OnCut, cutItem)
        self.Bind(wx.EVT_MENU, self.OnCopy, copyItem)
        self.Bind(wx.EVT_MENU, self.OnPaste, pasteItem)

        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
    
    def OnNew(self, event):
        wx.MessageBox('Not implemented yet')
    
    def OnExit(self, event):
        self.Close(True)
    
    def OnAbout(self, event):
        wx.MessageBox('This is a wxPython Hello World sample', 'About Tree Notes', wx.OK | wx.ICON_INFORMATION)
    
    def OnOpen(self, event):
        wx.MessageBox('Not implemented yet')
    
    def OnSave(self, event):
        wx.MessageBox('Not implemented yet')
    
    def OnSaveAs(self, event):
        wx.MessageBox('Not implemented yet')
    
    def OnCut(self, event):
        wx.MessageBox('Not implemented yet')
    
    def OnCopy(self, event):
        wx.MessageBox('Not implemented yet')
    
    def OnPaste(self, event):
        wx.MessageBox('Not implemented yet')

def main():
    app = wx.App()
    frm = TNFrame(None, title='Tree Notes', size=(1200, 720))
    frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()