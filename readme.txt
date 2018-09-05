Créer une page html (avec interface graphique)----------------------------------------------
Url     : http://codes-sources.commentcamarche.net/source/40182-creer-une-page-html-avec-interface-graphiqueAuteur  : aera groupDate    : 06/08/2013
Licence :
=========

Ce document intitulé « Créer une page html (avec interface graphique) » issu de CommentCaMarche
(codes-sources.commentcamarche.net) est mis à disposition sous les termes de
la licence Creative Commons. Vous pouvez copier, modifier des copies de cette
source, dans les conditions fixées par la licence, tant que cette note
apparaît clairement.

Description :
=============

Ce code sert &agrave; cr&eacute;&eacute; facilement une page html avec un son un
e image et deux lignes de texte. L'interface graphique est avec WxPython, mais j
e pense pouvoir cr&eacute;&eacute; prochainement une autre interface avec Tkinte
r. Si vous avez des id&eacute;&eacute;s d'am&eacute;liorations, faite les moi pa
rvenirs.
<br />Le code peut parraitre un peut compliquer, mais c'est parce que,
 le fichier cr&eacute;&eacute; doit comporter des accents et autres carract&egra
ve;res sp&eacute;ciaux. Or c'est assez compliquer ; cf mon code. Si vous voullez
 plus d'explication n'&eacute;siter pas &agrave; laissez des messages.<h2>Source
 / Exemple :</h2>
<pre class='code' data-mode='python'>
import wx
import os




#########################################
class MyMiniFrame1(wx.MiniFrame):

    def __init__(
        self, parent, title,entree, pos=wx.DefaultPosition,
 size=wx.DefaultSize,
        style=wx.DEFAULT_FRAME_STYLE
        ):
       
 self.entree=entree

        wx.MiniFrame.__init__(self, parent, -1, title, po
s, size, style)
        panel = wx.Panel(self, -1)




        button1 = w
x.Button(panel, -1, u&quot;&Eacute;&quot;)
        button2 = wx.Button(panel, -
1, u&quot;&Egrave;&quot;)
        button3 = wx.Button(panel, -1, u&quot;&Agrave
;&quot;)
        button4 = wx.Button(panel, -1, u&quot;?&quot;)
        button
5 = wx.Button(panel, -1, u&quot;@&quot;)
        button6 = wx.Button(panel, -1,
 u&quot;&Ccedil;&quot;)
        button7 = wx.Button(panel, -1, u&quot;&aelig;&q
uot;)
        button8 = wx.Button(panel, -1, u&quot;?&quot;)
        button9 =
 wx.Button(panel, -1, u&quot;&copy;&quot;)
        button10 = wx.Button(panel, 
-1, u&quot;&reg;&quot;)
        boutonqui= wx.Button(panel, -1, u&quot;Fermer c
ette fen&ecirc;tre&quot;)

        self.Bind(wx.EVT_BUTTON, self.pb1, button1)

        self.Bind(wx.EVT_BUTTON, self.pb2, button2)
        self.Bind(wx.EVT_
BUTTON, self.pb3, button3)
        self.Bind(wx.EVT_BUTTON, self.pb4, button4)

        self.Bind(wx.EVT_BUTTON, self.pb5, button5)
        self.Bind(wx.EVT_B
UTTON, self.pb6, button6)
        self.Bind(wx.EVT_BUTTON, self.pb7, button7)

        self.Bind(wx.EVT_BUTTON, self.pb8, button8)
        self.Bind(wx.EVT_BU
TTON, self.pb9, button9)
        self.Bind(wx.EVT_BUTTON, self.pb10, button10)

        self.Bind(wx.EVT_BUTTON, self.qu, boutonqui)
        

        sizer
 = wx.BoxSizer(wx.VERTICAL)

        lign1 = wx.BoxSizer(wx.HORIZONTAL)
     
   lign1.Add(button1, 0, wx.ALL|wx.CENTER, 10)
        lign1.Add(button2, 0, wx
.ALL|wx.CENTER, 10)
        lign1.Add(button3, 0, wx.ALL|wx.CENTER, 10)
      
  lign1.Add(button4, 0, wx.ALL|wx.CENTER, 10)
        lign1.Add(button5, 0, wx.
ALL|wx.CENTER, 10)

        lign2 = wx.BoxSizer(wx.HORIZONTAL)
        lign2.
Add(button6, 0, wx.ALL|wx.CENTER, 10)
        lign2.Add(button7, 0, wx.ALL|wx.C
ENTER, 10)
        lign2.Add(button8, 0, wx.ALL|wx.CENTER, 10)
        lign2.A
dd(button9, 0, wx.ALL|wx.CENTER, 10)
        lign2.Add(button10, 0, wx.ALL|wx.C
ENTER, 10)

        sizer.Add(lign1, 0, wx.ALL|wx.CENTER, 10)
        sizer.A
dd(lign2, 0, wx.ALL|wx.CENTER, 10)
        sizer.Add(boutonqui, 0, wx.ALL|wx.CE
NTER, 10)

        panel.SetSizer(sizer)
        panel.Layout()

    def pb
1(self, evt):
        global carr
        carr=u&quot;&Eacute;&quot;
        
self.fonc()
    def pb2(self, evt):
        global carr
        carr=u&quot;&
Egrave;&quot;
        self.fonc()
    def pb3(self, evt):
        global carr

        carr=u&quot;&Agrave;&quot;
        self.fonc()
    def pb4(self, evt
):
        global carr
        carr=u&quot;?&quot;
        self.fonc()
    d
ef pb5(self, evt):
        global carr
        carr=u&quot;@&quot;
        se
lf.fonc()
    def pb6(self, evt):
        global carr
        carr=u&quot;&Cc
edil;&quot;
        self.fonc()
    def pb7(self, evt):
        global carr

        carr=u&quot;&aelig;&quot;
        self.fonc()
    def pb8(self, evt):

        global carr
        carr=u&quot;?&quot;
        self.fonc()
    def 
pb9(self, evt):
        global carr
        carr=u&quot;&copy;&quot;
        
self.fonc()
    def pb10(self, evt):
        global carr
        carr=u&quot;
&reg;&quot;
        self.fonc()

    def fonc(self):
        global carr
  
      tempore=self.entree.GetValue()
        self.entree.Clear()
        self.
entree.WriteText(tempore+carr)

    def qu(self, evt):
        self.Destroy()


        



class MyFrame(wx.Frame):
    def __init__(self, parent, tit
le):
        wx.Frame.__init__(self, parent, -1, title,size=((500, 600)))
    
    global choix1,choix2,b11,b12,chso,chim,entree_1,entree_2,entree_3,fichier,fi
chier2

        



        menuBar = wx.MenuBar()

         
        m
enu = wx.Menu()

        
        menu.Append(1,u&quot;Quitter\tAlt-F2&quot;,
 &quot;Quitter le programme&quot;)

        self.Bind(wx.EVT_MENU, self.quiter
, id=1)

        menuBar.Append(menu, u&quot;Fichier&quot;)

        menu2 =
 wx.Menu()
        menu2.Append(2,u&quot;Aide&quot;, &quot;Obtenir de l'aide&qu
ot;)
        menu2.AppendSeparator()
        menu2.Append(3,u&quot;&Agrave; pr
opos de ...&quot;, u&quot;Imformation g&eacute;n&eacute;rale&quot;)

        s
elf.Bind(wx.EVT_MENU, self.aide, id=2)
        self.Bind(wx.EVT_MENU, self.prop
o, id=3)

        menuBar.Append(menu2, u&quot;Aide&quot;)
        
        
self.SetMenuBar(menuBar)


        self.CreateStatusBar()


        choix1
=0
        choix2=0
        chso=0
        chim=0
        fichier=''
      
  fichier2=''


        
        panel = wx.Panel(self)

        
       
 texta=wx.StaticText(panel, -1, u&quot;Voici un programme qui permet de cr&eacut
e;&eacute; une page html avec diff&eacute;rant &eacute;lements&quot;)
        t
exta.SetSize(texta.GetBestSize())

        box = wx.StaticBox(panel, -1, u&quo
t;Son&quot;)
        bsizer = wx.StaticBoxSizer(box, wx.VERTICAL)
        text
a1 = wx.StaticText(panel, -1, u&quot;\nObtion n&deg;1 : le son                  
           \n\n&quot;)
        c1 = wx.CheckBox(panel, -1, u&quot;Ins&eacute;re
r un son&quot;)
        textb1 = wx.StaticText(panel, -1, &quot;\n&quot;)
    
    b11 = wx.Button(panel, -1, u&quot;Choisir un son&quot;)
        b11.Enable(
False)
        bsizer.Add(texta1, 0, wx.CENTER, 10)
        bsizer.Add(c1, 0,w
x.CENTER, 10)
        bsizer.Add(textb1, 0,wx.CENTER, 10)
        bsizer.Add(b
11, 0,wx.CENTER, 10)



        box1 = wx.StaticBox(panel, -1, u&quot;Image&
quot;)
        bsizer1 = wx.StaticBoxSizer(box1, wx.VERTICAL)
        texta2 =
 wx.StaticText(panel, -1, u&quot;\nObtion n&deg;2 : l'image                     
        \n\n&quot;)
        c2 = wx.CheckBox(panel, -1, u&quot;Ins&eacute;rer u
ne image&quot;)
        textb2 = wx.StaticText(panel, -1, &quot;\n&quot;)
    
    b12 = wx.Button(panel, -1, u&quot;Choisir une image&quot;)
        b12.Enab
le(False)
        bsizer1.Add(texta2, 0, wx.CENTER, 10)
        bsizer1.Add(c2
, 0,wx.CENTER, 10)
        bsizer1.Add(textb2, 0,wx.CENTER, 10)
        bsizer
1.Add(b12, 0,wx.CENTER, 10)

        box2 = wx.StaticBox(panel, -1, u&quot;Tit
re et message&quot;)
        bsizer2 = wx.StaticBoxSizer(box2, wx.VERTICAL)
  
      texta3 = wx.StaticText(panel, -1, u&quot;\nObtion n&deg;3 : l'insertion du
 titre et de deux lignes d'information                                          
  \n\n                                                                         T
itre :&quot;)
        entree_1= wx.TextCtrl(panel, -1, u&quot;Titre&quot;, size
=(200,-1))
        textb3 = wx.StaticText(panel, -1, u&quot;\nLigne n&deg;1 (en
 gras) :&quot;)
        sep1=wx.StaticText(panel, -1, u&quot;   &quot;)
      
  sep2=wx.StaticText(panel, -1, u&quot;   &quot;)
        sep3=wx.StaticText(pa
nel, -1, u&quot;   &quot;)
        entree_2= wx.TextCtrl(panel, -1, u&quot;Lign
e 1&quot;, size=(200,-1))
        textc3 = wx.StaticText(panel, -1, u&quot;\nLi
gne n&deg;2 (normal) :&quot;)
        entree_3= wx.TextCtrl(panel, -1, u&quot;L
igne 2&quot;, size=(200,-1))
        ben1=wx.Button(panel, -1, u&quot;Ins&eacut
e;rer un carract&egrave;re sp&eacute;cial&quot;)
        ben2=wx.Button(panel, 
-1, u&quot;Ins&eacute;rer un carract&egrave;re sp&eacute;cial&quot;)
        be
n3=wx.Button(panel, -1, u&quot;Ins&eacute;rer un carract&egrave;re sp&eacute;cia
l&quot;)
        
        boit7 = wx.BoxSizer(wx.HORIZONTAL)
        boit7.Ad
d(entree_1, 0,wx.CENTER, 10)
        boit7.Add(sep1, 0,wx.CENTER, 10)
        
boit7.Add(ben1, 0,wx.CENTER, 10)

        boit8 = wx.BoxSizer(wx.HORIZONTAL)

        boit8.Add(entree_2, 0,wx.CENTER, 10)
        boit8.Add(sep2, 0,wx.CENTE
R, 10)
        boit8.Add(ben2, 0,wx.CENTER, 10)

        boit9 = wx.BoxSizer(
wx.HORIZONTAL)
        boit9.Add(entree_3, 0,wx.CENTER, 10)
        boit9.Add(
sep3, 0,wx.CENTER, 10)
        boit9.Add(ben3, 0,wx.CENTER, 10)

        
  
      bsizer2.Add(texta3, 0, wx.CENTER, 10)
        bsizer2.Add(boit7, 0,wx.CEN
TER, 10)
        bsizer2.Add(textb3, 0,wx.CENTER, 10)
        bsizer2.Add(boit
8, 0,wx.CENTER, 10)
        bsizer2.Add(textc3, 0,wx.CENTER, 10)
        bsize
r2.Add(boit9, 0,wx.CENTER, 10)

        
        b1 = wx.Button(panel, -1, u&
quot;Quitter le programme&quot;)
        b2 = wx.Button(panel, -1, u&quot;Cr&ea
cute;&eacute; le fichier&quot;)
        



        
        self.Bind(wx.
EVT_BUTTON, self.quiter, b1)
        self.Bind(wx.EVT_BUTTON, self.cree, b2)   
     
        self.Bind(wx.EVT_CHECKBOX, self.choi1, c1)
        self.Bind(wx.
EVT_CHECKBOX, self.choi2, c2)
        self.Bind(wx.EVT_BUTTON, self.imson, b11)

        self.Bind(wx.EVT_BUTTON, self.imima, b12)
        self.Bind(wx.EVT_BU
TTON, self.fonc1, ben1)
        self.Bind(wx.EVT_BUTTON, self.fonc2, ben2)
   
     self.Bind(wx.EVT_BUTTON, self.fonc3, ben3)


        sizer = wx.BoxSizer
(wx.VERTICAL)
        sizer.Add(texta, 0, wx.ALL|wx.CENTER, 10)

        boit
 = wx.BoxSizer(wx.HORIZONTAL)
        
        boit.Add(bsizer, 0, wx.ALL, 10)

        boit.Add(bsizer1, 0, wx.ALL, 10)
        sizer.Add(boit, 0, wx.ALL|wx
.CENTER, 10)
        
        sizer.Add(bsizer2, 0, wx.ALL|wx.CENTER, 10)
   
     
        boit1 = wx.BoxSizer(wx.HORIZONTAL)
        
        boit1.Add(b
1, 0, wx.ALL, 10)
        boit1.Add(b2, 0, wx.ALL, 10)
        sizer.Add(boit1
, 0, wx.ALL|wx.CENTER, 10)
        panel.SetSizer(sizer)
        panel.Layout(
)


        self.Centre()


    def quiter(self, evt):
        self.Close
()


    def choi1(self, evt):
        global choix1,b11
        if choix1=
=0:
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
            choi
x2=0


    def imson(self,evt):
        global chso,fichier
        dlg = w
x.FileDialog(
            self, message=u&quot;Importer un fichier audio&quot;,
 defaultDir=os.getcwd(), 
            defaultFile=&quot;&quot;, wildcard=u&quot
;Fichier audio Windows M&eacute;dia (*.wma)|*.wma|Tout les fichiers|*.*&quot;, s
tyle=wx.OPEN
            )


        if dlg.ShowModal() == wx.ID_OK:
      
      
            fichier = dlg.GetPaths()
            fichier = fichier[0]

            nombre = len(fichier)-4
            if fichier[nombre:].lower()==u'
.wma':
                chso=1
            else :
                dia=wx.Messa
geDialog(self, u&quot;Vous n'avez pas s&eacute;lectionner de fichier audio valid
e.&quot;, caption = u&quot;Erreur&quot;, style = wx.OK|wx.ICON_ERROR,
         
                    pos = wx.DefaultPosition)
                valeur = dia.Show
Modal()
                chso=0

    def imima(self,evt):
        global chim
,fichier2
        dlg = wx.FileDialog(
            self, message=u&quot;Import
er un fichier image&quot;, defaultDir=os.getcwd(), 
            defaultFile=&qu
ot;&quot;, wildcard=u&quot;Fichier JPG (*.JPG)|*.JPG|Fichier PNG (*.PNG)|*.PNG|F
ichier bmp (*.bmp)|*.bmp|Tout les fichiers|*.*&quot;, style=wx.OPEN
           
 )


        if dlg.ShowModal() == wx.ID_OK:
            
            fichi
er2 = dlg.GetPaths()
            fichier2 = fichier2[0]
            nombre = l
en(fichier2)-4
            if fichier2[nombre:].lower()==u'.jpg' or fichier2[no
mbre:].lower()==u'.png' or fichier2[nombre:].lower()==u'.bmp':
                
chim=1
            else :
                dia=wx.MessageDialog(self, u&quot;Vo
us n'avez pas s&eacute;lectionner de fichier image valide.&quot;, caption = u&qu
ot;Erreur&quot;, style = wx.OK|wx.ICON_ERROR,
                             pos 
= wx.DefaultPosition)
                valeur = dia.ShowModal()
               
 chim=0
        

    

    def aide(self, evt):
        dia=wx.MessageDia
log(self, u&quot;Aide\n\n\nCe programme vous permet de cr&eacute;&eacute; une pa
ge dite html, c'est &agrave; dire\nune page Internet. Vous n'avez qu'a renter le
s informations demander (ce\nn'est pas compliquer !). La page html sera cr&eacut
e;&eacute; ou vous l'avez indiquer\nsur votre disque dure. Bonne utilisation !&q
uot;, caption = u&quot;Aide&quot;, style = wx.OK,
                             
pos = wx.DefaultPosition)
        valeur = dia.ShowModal()
        dia.Destroy
()
        
    def propo(self, evt):
        dia=wx.MessageDialog(self, u&qu
ot;&Agrave; propos de ce programme :\n\n_____________________________\n\nCr&eacu
te;&eacute; par A&eacute;ra group.\nVersion 2.1.1 (La version 1.0 n'est pas disp
onible)\n\nRemerciment : &agrave; N. Pourc. (cette personne se reconnaitra !) po
ur m'avoir aider sur WxPython.&quot;, caption = u&quot;&Agrave; propos de ...&qu
ot;, style = wx.OK,
                             pos = wx.DefaultPosition)
   
     valeur = dia.ShowModal()
        dia.Destroy()

    def fonc1(self, evt)
:
        win = MyMiniFrame1(self, u'Carract&egrave;re sp&eacute;ciaux du champ
s &quot;Titre&quot;',entree_1,
                          style=wx.DEFAULT_FRAME
_STYLE | wx.TINY_CAPTION_HORIZ)
        win.CenterOnParent(wx.BOTH)
        wi
n.SetSize((500, 200)) 
        win.Show(True)

    def fonc2(self, evt):
   
     win = MyMiniFrame1(self, u'Carract&egrave;re sp&eacute;ciaux du champs &quo
t;Ligne n&deg;1&quot;',entree_2,
                          style=wx.DEFAULT_FRA
ME_STYLE | wx.TINY_CAPTION_HORIZ)
        win.CenterOnParent(wx.BOTH)
        
win.SetSize((500, 200)) 
        win.Show(True)

    def fonc3(self, evt):
 
       win = MyMiniFrame1(self, u'Carract&egrave;re sp&eacute;ciaux du champs &q
uot;Ligne n&deg;2&quot;',entree_3,
                          style=wx.DEFAULT_F
RAME_STYLE | wx.TINY_CAPTION_HORIZ)
        win.CenterOnParent(wx.BOTH)
      
  win.SetSize((500, 200)) 
        win.Show(True)

    def cree(self, evt):

        global chim,fichier2,chso,fichier,entree_1,entree_2,entree_3,choix2,choi
x1
        if entree_1.GetValue()=='':
            dia=wx.MessageDialog(self, 
u&quot;Il faut obligatoirement renter un titre.&quot;, caption = u&quot;Erreur&q
uot;, style = wx.OK|wx.ICON_ERROR,
                             pos = wx.Defaul
tPosition)
            valeur = dia.ShowModal()
        else:
            con
=1
            if choix1==1 and chso==0:
                dia=wx.MessageDialog(
self, u&quot;Vous n'avez pas s&eacute;lectionner de fichier son. Voullez vous co
ntinuer ?&quot;, caption = u&quot;Question son&quot;, style = wx.YES_NO|wx.ICON_
QUESTION,
                             pos = wx.DefaultPosition)
             
   valeur = dia.ShowModal()
                if valeur==wx.ID_NO:
             
       con=0
            if con==1:
                if choix2==1 and chim==0:

                    dia=wx.MessageDialog(self, u&quot;Vous n'avez pas s&eacute;
lectionner de fichier image. Voullez vous continuer ?&quot;, caption = u&quot;Qu
estion image&quot;, style = wx.YES_NO|wx.ICON_QUESTION,
                       
          pos = wx.DefaultPosition)
                    valeur = dia.ShowModal(
)
                    if valeur==wx.ID_NO:
                        con=0
    
                else:
                        con=1
            if con==1:
  
              dlg = wx.FileDialog(self, message=u&quot;Cr&eacute;&eacute; le fic
hier html&quot;, defaultDir=os.getcwd(),
                                    de
faultFile=&quot;&quot;, wildcard=u&quot;Fichier web html (*.html)|*.html&quot;, 
style=wx.SAVE)
                if dlg.ShowModal() == wx.ID_OK:
               
     fi=dlg.GetPath()
                    outfile = open(fi, &quot;w&quot;)
  
                  fil=&quot;&quot;&quot;&lt;HTML&gt;&lt;HEAD&gt;
&lt;TITLE&gt;%
s&lt;/TITLE&gt;
&lt;/HEAD&gt;&lt;BODY&gt;&lt;DIV ALIGN=&quot;center&quot;&gt;&q
uot;&quot;&quot; % (entree_1.GetValue())
                    if choix2==1 and c
him==1:
                        fil=fil+&quot;&quot;&quot;

&lt;IMG SRC=&quot
;%s&quot;&gt;&quot;&quot;&quot; % (fichier2)
                    if choix1==1 a
nd chso==1:
                        fil=fil+&quot;&quot;&quot;

&lt;bgsound s
rc=&quot;%s&quot; loop=&quot;1&quot;&gt;&quot;&quot;&quot; % (fichier)
        
            fil=fil + &quot;&quot;&quot;

&lt;H2&gt;%s&lt;/H2&gt;
&lt;P&gt;%s
&lt;/P&gt;
&lt;/FORM&gt;
&lt;/DIV&gt;&lt;/BODY&gt;&lt;/HTML&gt;&quot;&quot;&qu
ot; % (entree_2.GetValue(),entree_3.GetValue())
                    outfile.wri
te(fil.encode(&quot;windows-1252&quot;))
                    outfile.close()
 
                   
                    

                    
        

 
       

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(
None, u&quot;Cr&eacute;&eacute; une page html&quot;)
        self.SetTopWindow(
frame)

        frame.Show(True)
        return True
        
app = MyApp(T
rue)
app.MainLoop()</pre><h2> Conclusion : </h2>Remerciment : N. Pourc. (cette 
personne se reconnetra) pour m'avoir aid&eacute; &agrave; d&eacute;buter avec Py
thon et WxPython.
<br />
<br />POUR CEUX QUI D&Eacute;SIR T&Eacute;L&Eacute;CH
ARGER WX.PYTHON :
<br />
<br />Allez sur le site <a href='http://www.wxpython.
org/download.php' target='_blank'>http://www.wxpython.org/download.php</a> et s&
eacute;lectionner la version correspondant &agrave; votre version de Python et &
agrave; votre syst&egrave;me d'exploitation.
