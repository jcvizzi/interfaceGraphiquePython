import wx
import os


##############


class TestDialog(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE
            ):
        pre = wx.PreDialog()
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

        sizer = wx.BoxSizer(wx.VERTICAL)

        bmp = wx.Bitmap("Aeragroup.bmp", wx.BITMAP_TYPE_BMP)
        image=wx.StaticBitmap(self, -1, bmp, (80, 50), (bmp.GetWidth(), bmp.GetHeight()))
        


        textaprop=u"""
À propos de ce programme :


_____________________________

Créé par Aéra group.
Version 2.1.2 (La version 1.0 n'est pas disponible) ; Version avec Tkinter à venir

Remerciment : à N. Pourc. (cette personne se reconnaitra !) pour m'avoir aider sur WxPython."""



        

        label = wx.StaticText(self, -1, textaprop)
        sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(image, 0, wx.ALIGN_CENTRE|wx.ALL, 5)




        btnsizer = wx.StdDialogButtonSizer()
        
        if wx.Platform != "__WXMSW__":
            btn = wx.ContextHelpButton(self)
            self.box.Add(btn, 0, wx.ALL|wx.CENTER, 5)
            
        btn = wx.Button(self, wx.ID_OK,u"OK")
        btn.SetDefault()

        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)

        sizer.Add(btnsizer, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)

#########################################
class MyMiniFrame1(wx.MiniFrame):
    def __init__(
        self, parent, title,entree, pos=wx.DefaultPosition, size=wx.DefaultSize,
        style=wx.DEFAULT_FRAME_STYLE
        ):
        self.entree=entree

        wx.MiniFrame.__init__(self, parent, -1, title, pos, size, style)
        panel = wx.Panel(self, -1)




        button1 = wx.Button(panel, -1, u"É")
        button2 = wx.Button(panel, -1, u"È")
        button3 = wx.Button(panel, -1, u"À")
        button4 = wx.Button(panel, -1, u"€")
        button5 = wx.Button(panel, -1, u"@")
        button6 = wx.Button(panel, -1, u"Ç")
        button7 = wx.Button(panel, -1, u"æ")
        button8 = wx.Button(panel, -1, u"™")
        button9 = wx.Button(panel, -1, u"©")
        button10 = wx.Button(panel, -1, u"®")
        boutonqui= wx.Button(panel, -1, u"Fermer cette fenêtre")

        self.Bind(wx.EVT_BUTTON, self.pb1, button1)
        self.Bind(wx.EVT_BUTTON, self.pb2, button2)
        self.Bind(wx.EVT_BUTTON, self.pb3, button3)
        self.Bind(wx.EVT_BUTTON, self.pb4, button4)
        self.Bind(wx.EVT_BUTTON, self.pb5, button5)
        self.Bind(wx.EVT_BUTTON, self.pb6, button6)
        self.Bind(wx.EVT_BUTTON, self.pb7, button7)
        self.Bind(wx.EVT_BUTTON, self.pb8, button8)
        self.Bind(wx.EVT_BUTTON, self.pb9, button9)
        self.Bind(wx.EVT_BUTTON, self.pb10, button10)
        self.Bind(wx.EVT_BUTTON, self.qu, boutonqui)
        

        sizer = wx.BoxSizer(wx.VERTICAL)

        lign1 = wx.BoxSizer(wx.HORIZONTAL)
        lign1.Add(button1, 0, wx.ALL|wx.CENTER, 10)
        lign1.Add(button2, 0, wx.ALL|wx.CENTER, 10)
        lign1.Add(button3, 0, wx.ALL|wx.CENTER, 10)
        lign1.Add(button4, 0, wx.ALL|wx.CENTER, 10)
        lign1.Add(button5, 0, wx.ALL|wx.CENTER, 10)

        lign2 = wx.BoxSizer(wx.HORIZONTAL)
        lign2.Add(button6, 0, wx.ALL|wx.CENTER, 10)
        lign2.Add(button7, 0, wx.ALL|wx.CENTER, 10)
        lign2.Add(button8, 0, wx.ALL|wx.CENTER, 10)
        lign2.Add(button9, 0, wx.ALL|wx.CENTER, 10)
        lign2.Add(button10, 0, wx.ALL|wx.CENTER, 10)

        sizer.Add(lign1, 0, wx.ALL|wx.CENTER, 10)
        sizer.Add(lign2, 0, wx.ALL|wx.CENTER, 10)
        sizer.Add(boutonqui, 0, wx.ALL|wx.CENTER, 10)

        panel.SetSizer(sizer)
        panel.Layout()

    def pb1(self, evt):
        global carr
        carr=u"É"
        self.fonc()
    def pb2(self, evt):
        global carr
        carr=u"È"
        self.fonc()
    def pb3(self, evt):
        global carr
        carr=u"À"
        self.fonc()
    def pb4(self, evt):
        global carr
        carr=u"€"
        self.fonc()
    def pb5(self, evt):
        global carr
        carr=u"@"
        self.fonc()
    def pb6(self, evt):
        global carr
        carr=u"Ç"
        self.fonc()
    def pb7(self, evt):
        global carr
        carr=u"æ"
        self.fonc()
    def pb8(self, evt):
        global carr
        carr=u"™"
        self.fonc()
    def pb9(self, evt):
        global carr
        carr=u"©"
        self.fonc()
    def pb10(self, evt):
        global carr
        carr=u"®"
        self.fonc()

    def fonc(self):
        global carr
        tempore=self.entree.GetValue()
        self.entree.Clear()
        self.entree.WriteText(tempore+carr)

    def qu(self, evt):
        self.Destroy()
        



class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title,size=((500, 600)))
        global choix1,choix2,b11,b12,chso,chim,entree_1,entree_2,entree_3,fichier,fichier2
        self.SetIcon(wx.Icon("Icone1.ico", wx.BITMAP_TYPE_ICO ))

        



        menuBar = wx.MenuBar()

         
        menu = wx.Menu()

        
        menu.Append(1,u"Quitter\tAlt-F2", "Quitter le programme")

        self.Bind(wx.EVT_MENU, self.quiter, id=1)

        menuBar.Append(menu, u"Fichier")

        menu2 = wx.Menu()
        menu2.Append(2,u"Aide", "Obtenir de l'aide")
        menu2.AppendSeparator()
        menu2.Append(3,u"À propos de ...", u"Imformation générale")

        self.Bind(wx.EVT_MENU, self.aide, id=2)
        self.Bind(wx.EVT_MENU, self.propo, id=3)

        menuBar.Append(menu2, u"Aide")
        
        self.SetMenuBar(menuBar)


        self.CreateStatusBar()


        choix1=0
        choix2=0
        chso=0
        chim=0
        fichier=''
        fichier2=''


        
        panel = wx.Panel(self)

        
        texta=wx.StaticText(panel, -1, u"Voici un programme qui permet de créé une page html avec différant élements")
        texta.SetSize(texta.GetBestSize())

        box = wx.StaticBox(panel, -1, u"Son")
        bsizer = wx.StaticBoxSizer(box, wx.VERTICAL)
        texta1 = wx.StaticText(panel, -1, u"\nObtion n°1 : le son                             \n\n")
        c1 = wx.CheckBox(panel, -1, u"Insérer un son")
        textb1 = wx.StaticText(panel, -1, "\n")
        b11 = wx.Button(panel, -1, u"Choisir un son")
        b11.Enable(False)
        bsizer.Add(texta1, 0, wx.CENTER, 10)
        bsizer.Add(c1, 0,wx.CENTER, 10)
        bsizer.Add(textb1, 0,wx.CENTER, 10)
        bsizer.Add(b11, 0,wx.CENTER, 10)



        box1 = wx.StaticBox(panel, -1, u"Image")
        bsizer1 = wx.StaticBoxSizer(box1, wx.VERTICAL)
        texta2 = wx.StaticText(panel, -1, u"\nObtion n°2 : l'image                             \n\n")
        c2 = wx.CheckBox(panel, -1, u"Insérer une image")
        textb2 = wx.StaticText(panel, -1, "\n")
        b12 = wx.Button(panel, -1, u"Choisir une image")
        b12.Enable(False)
        bsizer1.Add(texta2, 0, wx.CENTER, 10)
        bsizer1.Add(c2, 0,wx.CENTER, 10)
        bsizer1.Add(textb2, 0,wx.CENTER, 10)
        bsizer1.Add(b12, 0,wx.CENTER, 10)

        box2 = wx.StaticBox(panel, -1, u"Titre et message")
        bsizer2 = wx.StaticBoxSizer(box2, wx.VERTICAL)
        texta3 = wx.StaticText(panel, -1, u"\nObtion n°3 : l'insertion du titre et de deux lignes d'information                                            \n\n                                                                         Titre :")
        entree_1= wx.TextCtrl(panel, -1, u"Titre", size=(200,-1))
        textb3 = wx.StaticText(panel, -1, u"\nLigne n°1 (en gras) :")
        sep1=wx.StaticText(panel, -1, u"   ")
        sep2=wx.StaticText(panel, -1, u"   ")
        sep3=wx.StaticText(panel, -1, u"   ")
        entree_2= wx.TextCtrl(panel, -1, u"Ligne 1", size=(200,-1))
        textc3 = wx.StaticText(panel, -1, u"\nLigne n°2 (normal) :")
        entree_3= wx.TextCtrl(panel, -1, u"Ligne 2", size=(200,-1))
        ben1=wx.Button(panel, -1, u"Insérer un carractère spécial")
        ben2=wx.Button(panel, -1, u"Insérer un carractère spécial")
        ben3=wx.Button(panel, -1, u"Insérer un carractère spécial")
        
        boit7 = wx.BoxSizer(wx.HORIZONTAL)
        boit7.Add(entree_1, 0,wx.CENTER, 10)
        boit7.Add(sep1, 0,wx.CENTER, 10)
        boit7.Add(ben1, 0,wx.CENTER, 10)

        boit8 = wx.BoxSizer(wx.HORIZONTAL)
        boit8.Add(entree_2, 0,wx.CENTER, 10)
        boit8.Add(sep2, 0,wx.CENTER, 10)
        boit8.Add(ben2, 0,wx.CENTER, 10)

        boit9 = wx.BoxSizer(wx.HORIZONTAL)
        boit9.Add(entree_3, 0,wx.CENTER, 10)
        boit9.Add(sep3, 0,wx.CENTER, 10)
        boit9.Add(ben3, 0,wx.CENTER, 10)

        
        bsizer2.Add(texta3, 0, wx.CENTER, 10)
        bsizer2.Add(boit7, 0,wx.CENTER, 10)
        bsizer2.Add(textb3, 0,wx.CENTER, 10)
        bsizer2.Add(boit8, 0,wx.CENTER, 10)
        bsizer2.Add(textc3, 0,wx.CENTER, 10)
        bsizer2.Add(boit9, 0,wx.CENTER, 10)

        
        b1 = wx.Button(panel, -1, u"Quitter le programme")
        b2 = wx.Button(panel, -1, u"Créé le fichier")
        



        
        self.Bind(wx.EVT_BUTTON, self.quiter, b1)
        self.Bind(wx.EVT_BUTTON, self.cree, b2)        
        self.Bind(wx.EVT_CHECKBOX, self.choi1, c1)
        self.Bind(wx.EVT_CHECKBOX, self.choi2, c2)
        self.Bind(wx.EVT_BUTTON, self.imson, b11)
        self.Bind(wx.EVT_BUTTON, self.imima, b12)
        self.Bind(wx.EVT_BUTTON, self.fonc1, ben1)
        self.Bind(wx.EVT_BUTTON, self.fonc2, ben2)
        self.Bind(wx.EVT_BUTTON, self.fonc3, ben3)


        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(texta, 0, wx.ALL|wx.CENTER, 10)

        boit = wx.BoxSizer(wx.HORIZONTAL)
        
        boit.Add(bsizer, 0, wx.ALL, 10)
        boit.Add(bsizer1, 0, wx.ALL, 10)
        sizer.Add(boit, 0, wx.ALL|wx.CENTER, 10)
        
        sizer.Add(bsizer2, 0, wx.ALL|wx.CENTER, 10)
        
        boit1 = wx.BoxSizer(wx.HORIZONTAL)
        
        boit1.Add(b1, 0, wx.ALL, 10)
        boit1.Add(b2, 0, wx.ALL, 10)
        sizer.Add(boit1, 0, wx.ALL|wx.CENTER, 10)
        panel.SetSizer(sizer)
        panel.Layout()


        self.Centre()


    def quiter(self, evt):
        self.Close()


    def choi1(self, evt):
        global choix1,b11
        if choix1==0:
            b11.Enable(True)
            choix1=1
        else :
            b11.Enable(False)
            choix1=0

    def choi2(self, evt):
        global choix2,b12
        if choix2==0:
            b12.Enable(True)
            choix2=1
        else :
            b12.Enable(False)
            choix2=0


    def imson(self,evt):
        global chso,fichier
        dlg = wx.FileDialog(
            self, message=u"Importer un fichier audio", defaultDir=os.getcwd(), 
            defaultFile="", wildcard=u"Fichier audio Windows Média (*.wma)|*.wma|Tout les fichiers|*.*", style=wx.OPEN
            )


        if dlg.ShowModal() == wx.ID_OK:
            
            fichier = dlg.GetPaths()
            fichier = fichier[0]
            nombre = len(fichier)-4
            if fichier[nombre:].lower()==u'.wma':
                chso=1
            else :
                dia=wx.MessageDialog(self, u"Vous n'avez pas sélectionner de fichier audio valide.", caption = u"Erreur", style = wx.OK|wx.ICON_ERROR,
                             pos = wx.DefaultPosition)
                valeur = dia.ShowModal()
                chso=0

    def imima(self,evt):
        global chim,fichier2
        dlg = wx.FileDialog(
            self, message=u"Importer un fichier image", defaultDir=os.getcwd(), 
            defaultFile="", wildcard=u"Fichier JPG (*.JPG)|*.JPG|Fichier PNG (*.PNG)|*.PNG|Fichier bmp (*.bmp)|*.bmp|Tout les fichiers|*.*", style=wx.OPEN
            )


        if dlg.ShowModal() == wx.ID_OK:
            
            fichier2 = dlg.GetPaths()
            fichier2 = fichier2[0]
            nombre = len(fichier2)-4
            if fichier2[nombre:].lower()==u'.jpg' or fichier2[nombre:].lower()==u'.png' or fichier2[nombre:].lower()==u'.bmp':
                chim=1
            else :
                dia=wx.MessageDialog(self, u"Vous n'avez pas sélectionner de fichier image valide.", caption = u"Erreur", style = wx.OK|wx.ICON_ERROR,
                             pos = wx.DefaultPosition)
                valeur = dia.ShowModal()
                chim=0
        

    

    def aide(self, evt):
        dia=wx.MessageDialog(self, u"Aide\n\n\nCe programme vous permet de créé une page dite html, c'est à dire\nune page Internet. Vous n'avez qu'a renter les informations demander (ce\nn'est pas compliquer !). La page html sera créé ou vous l'avez indiquer\nsur votre disque dure. Bonne utilisation !", caption = u"Aide", style = wx.OK,
                             pos = wx.DefaultPosition)
        valeur = dia.ShowModal()
        dia.Destroy()
        
    def propo(self, evt):
        dlg = TestDialog(self, -1, u"À propos de ...", size=(350, 200),
                         #style = wxCAPTION | wxSYSTEM_MENU | wxTHICK_FRAME
                         style = wx.DEFAULT_DIALOG_STYLE
                         )
        dlg.CenterOnScreen()
        val = dlg.ShowModal()

    def fonc1(self, evt):
        win = MyMiniFrame1(self, u'Carractère spéciaux du champs "Titre"',entree_1,
                          style=wx.DEFAULT_FRAME_STYLE | wx.TINY_CAPTION_HORIZ)
        win.CenterOnParent(wx.BOTH)
        win.SetSize((500, 200)) 
        win.Show(True)

    def fonc2(self, evt):
        win = MyMiniFrame1(self, u'Carractère spéciaux du champs "Ligne n°1"',entree_2,
                          style=wx.DEFAULT_FRAME_STYLE | wx.TINY_CAPTION_HORIZ)
        win.CenterOnParent(wx.BOTH)
        win.SetSize((500, 200)) 
        win.Show(True)

    def fonc3(self, evt):
        win = MyMiniFrame1(self, u'Carractère spéciaux du champs "Ligne n°2"',entree_3,
                          style=wx.DEFAULT_FRAME_STYLE | wx.TINY_CAPTION_HORIZ)
        win.CenterOnParent(wx.BOTH)
        win.SetSize((500, 200)) 
        win.Show(True)

    def cree(self, evt):
        global chim,fichier2,chso,fichier,entree_1,entree_2,entree_3,choix2,choix1
        if entree_1.GetValue()=='':
            dia=wx.MessageDialog(self, u"Il faut obligatoirement renter un titre.", caption = u"Erreur", style = wx.OK|wx.ICON_ERROR,
                             pos = wx.DefaultPosition)
            valeur = dia.ShowModal()
        else:
            con=1
            if choix1==1 and chso==0:
                dia=wx.MessageDialog(self, u"Vous n'avez pas sélectionner de fichier son. Voullez vous continuer ?", caption = u"Question son", style = wx.YES_NO|wx.ICON_QUESTION,
                             pos = wx.DefaultPosition)
                valeur = dia.ShowModal()
                if valeur==wx.ID_NO:
                    con=0
            if con==1:
                if choix2==1 and chim==0:
                    dia=wx.MessageDialog(self, u"Vous n'avez pas sélectionner de fichier image. Voullez vous continuer ?", caption = u"Question image", style = wx.YES_NO|wx.ICON_QUESTION,
                                 pos = wx.DefaultPosition)
                    valeur = dia.ShowModal()
                    if valeur==wx.ID_NO:
                        con=0
                    else:
                        con=1
            if con==1:
                dlg = wx.FileDialog(self, message=u"Créé le fichier html", defaultDir=os.getcwd(),
                                    defaultFile="", wildcard=u"Fichier web html (*.html)|*.html", style=wx.SAVE)
                if dlg.ShowModal() == wx.ID_OK:
                    fi=dlg.GetPath()
                    outfile = open(fi, "w")
                    fil="""<HTML><HEAD>
<TITLE>%s</TITLE>
</HEAD><BODY><DIV ALIGN="center">""" % (entree_1.GetValue())
                    if choix2==1 and chim==1:
                        fil=fil+"""

<IMG SRC="%s">""" % (fichier2)
                    if choix1==1 and chso==1:
                        fil=fil+"""

<bgsound src="%s" loop="1">""" % (fichier)
                    fil=fil + """

<H2>%s</H2>
<P>%s</P>
</FORM>
</DIV></BODY></HTML>""" % (entree_2.GetValue(),entree_3.GetValue())
                    outfile.write(fil.encode("windows-1252"))
                    outfile.close()
                    
                    

                    
        

        

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, u"Créé une page html")
        self.SetTopWindow(frame)

        frame.Show(True)
        return True
        
app = MyApp(True)
app.MainLoop()

