# coding=utf-8
import os
import kivy
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ListProperty
from platform import python_version
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
import pexpect



class CreateKeystore():
    def __init__(self):
        pass


class Lanca():
    def __init__(self):
        pass

    def download_apktool(self):
        os.system("sudo mkdir /home/kivy/apktool")
        os.system("sudo wget -c -P  https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.3.4.jar")


    def check_file_exists(self,tip, name, path):
        """
        :param tip: dir or file
        :param name: name file or = not_file
        :param path: path
        :return:
        """

        self.name = name
        self.path = path
        if os.path.isfile(self.path + self.name):

            return True

        else:
            return False


    def exe_linux(self,x):
        "cria comando para linux"

        os.system(x)


    def create_keystore(self, x , y):
        """recebe parametros e monta key conforme dados recebidos
           x = ['aliasname', 'namekey', 'stor183590', 'key183590', '14000', '/home/kivy/Desktop/']
           y = ['ailton', 'orgkivy', 'uniao kivy', 'sao paulo', 'sao paulo', 'br']
        """

        self.alias = x[0]
        self.name_key = x[1]
        self.storepass = x[2]
        self.keypass = x[3]
        self.validity = x[4]
        self.keypath = x[5]

        self.v = str("keytool -genkey -v -keystore " + self.keypath + self.name_key +
            ".keystore -alias " + self.alias + " -storepass " + self.storepass +
            " -keypass " + self.keypass + " -keyalg RSA -validity " + self.validity)

        print (self.v)


        self.p = pexpect.spawn(self.v, timeout=10)
        self.p.expect('What.*?')
        self.p.sendline("dddddddd")
        self.p.expect('What.*?')
        self.p.sendline("cccc")
        self.p.expect('What.*?')
        self.p.sendline("wdfsdvfsd")
        self.p.expect('What.*?')
        self.p.sendline("cccc")
        self.p.expect('What.*?')
        self.p.sendline("ss")
        self.p.expect('What.*?')
        self.p.sendline("ss")
        self.p.expect('Is.*?:')
        self.p.sendline("yes")
        #self.p.expect(pexpect.EOF)
        #print (self.p.before)


class PopApk(BoxLayout):
    pass


class Menu(Screen):
    pass


class PopKey(Popup):
    pass


class PopupAviso(Popup):
    pass


class PopKey_1(BoxLayout):
    def __init__(self, **kwargs):
        super(PopKey_1, self).__init__(**kwargs)

    def clean(self):
        self.clear_widgets()
        self.add_widget(PopKey_2())

    def clean_2(self):
        self.clear_widgets()
        self.add_widget(PopKey_3())


class PopKey_2(BoxLayout):
    def __init__(self, **kwargs):
        super(PopKey_2, self).__init__(**kwargs)

    def clean_2(self,):
        self.clear_widgets()
        self.add_widget(PopKey_1())


class PopKey_3(BoxLayout):
    def __init__(self, **kwargs):
        super(PopKey_3, self).__init__(**kwargs)

    def clean(self,):
        self.clear_widgets()
        self.add_widget(PopKey_1())


class PopKeyScreen(BoxLayout):
    pass


class Main(ScreenManager):

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)


    def checa_key(self,tip, name, path):

        self.m = Lanca()
        self.x_1 = name + ".keystore"
        self.x_5 = path

        # verifica se key já existe no diretorio
        if self.m.check_file_exists("file", self.x_1, self.x_5) == True:
            return True


        # chama classe externa
        elif self.m.check_file_exists("file", self.x_1, self.x_5) == False:
            return False



    def create_key(self, x, y):
        """
        recebe dados de popup_key.kv
        x = ['aliasname', 'namekey', 'stor183590', 'key183590', '14000', '/home/kivy/Desktop/']
        y = ['ailton', 'orgkivy', 'uniao kivy', 'sao paulo', 'sao paulo', 'br']
        envia listas com dados da keystore
        """
        self.m = Lanca()
        self.x_1 = x[1]+".keystore"
        self.x_5 = x[5]


        #verifica se key já existe no diretorio
        if self.m.check_file_exists("file", self.x_1, self.x_5  ) ==True:
            print ("arquivo ja existe")


        #chama classe externa
        elif self.m.check_file_exists("file", self.x_1, self.x_5  ) ==False:
            self.m = Lanca()
            self.m.create_keystore(x , y)
            #print (self.m.create_keystore(x, y))


    def cria_popup_senha(self,x):
        #content = Button(text =x)




        self.popup_senha = PopKey(title="CREATE YOUR KEY OR REPORT THE WAY", size_hint=(.7, .9),
                                   auto_dismiss=True,
                                   title_align="center",
                                   )

        self.pop_1 = PopKey_1()
        self.popup_senha.add_widget(self.pop_1)
        #content.bind(on_press=self.popup_senha.dismiss)
        #self.canvas.add(Color(1., 1., 0))
        #self.canvas.add(Color(1., 1., 0))
        #self.canvas.add(Rectangle(size=(50, 50)))
        #self.popup_senha.add_widget(Main())
        self.popup_senha.open()


    def cria_popup_apk(self,x):

        self.popup_apk = PopKey(title="CREATE YOUR APK OR REPORT THE WAY", size_hint=(.7, .9),
                                   auto_dismiss=True,
                                   title_align="center",
                                   )
        self.pop_1 = PopApk()
        self.popup_apk.add_widget(self.pop_1)
        self.popup_apk.open()


    def cria_popup_aviso(self,x):
        self.Bt_aviso = Button
        content = self.Bt_aviso(text =x)
        self.popup_senha = PopupAviso(title="Aviso", size_hint=(.7, .4),
                                   auto_dismiss=True,
                                   title_align="center",
                                   content=content)


        content.bind(on_press=self.popup_senha.dismiss)
        #self.canvas.add(Color(1., 1., 0))
        #self.canvas.add(Color(1., 1., 0))
        #self.canvas.add(Rectangle(size=(50, 50)))
        self.popup_senha.open()


    def create_apk(self, x ,y):
        """
        :param x: debug, release, deploy run, clean
        :param y: path_apkn = /home/kivy/Desktop/helloword/bin/
        :return:
        """

        self.type_apk = x
        os.system("cp -a ./apktool/apktool.jar /usr/local/bin")
        os.system("cp -a ./apktool/apktool /usr/local/bin")
        os.system("cd /usr/local/bin; chmod +x apktool")
        os.system("cd /usr/local/bin; chmod +x apktool.jar")
        os.system("cd" + y +"; apktool d myapp-0.1-release-unsigned.apk")


    def pop_dism(self, x):
        """
        fecha popup
        :param x: parametro referente a popup a ser fechado
        :return:
        """
        if x== 1:

            self.popup_apk.dismiss()
        if x == 2:
            self.popup_senha.dismiss()

#screen


    def create_keystore(self):
        self.current = 'create_keystore'

#screen
    def menu(self):
        self.current = 'menu'


class MainApp(App):

    #DADOS KEYSTORE
    alias = StringProperty("aliasname")
    name_key = StringProperty("")
    storepass = StringProperty("183590")
    keypass = StringProperty("183590")
    validity = StringProperty("10000")
    keypath = StringProperty("/home/kivy/Desktop/helloword/keystores/")

    #pacote do projeto
    path_project = StringProperty("/home/kivy/Desktop/helloword/")

    #path ndk
    path_ndk = StringProperty("/home/kivy/.buildozer/android/platform/android-ndk-r16b/")

    #path apktool
    path_apktool  = StringProperty("/home/kivy/apktool")

    #param keystore configurada?
    keystore_ok = BooleanProperty(False)

    #path do apk
    path_apk = ("/home/kivy/Desktop/helloword/bin/")

    #parametro textinput disabled (True ou False)
    par_1 = BooleanProperty(True)

    #parametro cor
    par_2 = StringProperty("e4efee")

    #parametro cor
    par_3 = StringProperty("ffffff")


    par_creatkey = ListProperty()

    
    data_key = ListProperty()

    def build(self):
        self.root = Main()
        return self.root


if __name__ == '__main__':
    MainApp().run()




