import wx
import daily_russian as dr

class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        # ensure the parent class's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)
        
        scraped_results = dr.return_image_information()

        english = scraped_results[1]
        russian = scraped_results[0]
        sign_image = scraped_results[2]

        # put some text with a larger bold font on it
        st = wx.StaticText(pnl, label=english+'\n'+russian)
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        pnl.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.App()
    frm = HelloFrame(None, title='Daily Russian Sign')
    frm.Show()
    app.MainLoop()