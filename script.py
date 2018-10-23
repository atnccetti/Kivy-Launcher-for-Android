# coding=utf-8
import os

import pexpect

from sub_text import ManipulaTxt



class Launcher():

    def __init__(self):
        self.file = "par_release.txt"


    def create_keystore(self, ):
        """recebe parametros e monta key conforme dados recebidos
           x = ['aliasname', 'namekey', 'stor183590', 'key183590', '14000', '/home/kivy/Desktop/']
           y = ['ailton', 'orgkivy', 'uniao kivy', 'sao paulo', 'sao paulo', 'br']
        """

        print("Iniciando criação da keystore....\n\n")
        self.text = ManipulaTxt()

        self.alias = self.text.le_line_script(self.file,"aliasname")
        self.name_key = self.text.le_line_script(self.file,"keyname")
        self.storepass = self.text.le_line_script(self.file,"keystore")
        self.keypass = self.text.le_line_script(self.file,"keypass")
        self.validity = self.text.le_line_script(self.file,"validity")
        self.keypath = self.text.le_line_script(self.file,"path_key")


        self.data_key = [self.alias,
                         self.name_key,
                         self.storepass,
                         self.keypass,
                         self.validity,
                         self.keypath
                         ]






        self.key = "keytool -genkey -v -keystore "+self.keypath+self.name_key+".keystore -alias " + self.alias + " -storepass " + self.storepass +" -keypass " + self.keypass + " -keyalg RSA -validity " + self.validity


        print("\nTentando criar a keystore....\n")


        try:
            self.p = pexpect.spawn(self.key, timeout=10)
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
            self.p.expect(pexpect.EOF)
            print (self.p.before)

            self.create_apk(self.data_key)
        except:
            print("\nkeystore já existe no diretório....\n")
            self.create_apk(self.data_key)




    def create_apk(self, data_key):
        """
        jarsigner -sigalg SHA1withRSA -digestalg SHA1
        -signedjar aliasname -storepass 183590 -keypass 183590
        -keystore /home/kivy/Desktop/helloword/keystores/keynamedd.keystore
        /home/kivy/Desktop/helloword/bin/myapp-0.1-release-unsigned.apk aliasname

        :param type: debug, release, deploy run, clean
        :param path_apk: /home/kivy/Desktop/helloword/bin/
        :param name_apk:
        :param data_key: ['aliasname', 'namekey', 'stor183590', 'key183590', '14000', '/home/kivy/Desktop/']

        :return:
        """

        print("\nIniciando trabalho no apk....\n")
        #self.type_apk = type
        self.path_apk = self.text.le_line_script(self.file,"path_apk")
        self.name_apk = self.text.le_line_script(self.file,"name_apk")
        self.data_key = data_key
        self.name_apk_2 = self.name_apk.replace(".apk", "")
        

        # copia apktool para pasta sistema
        print("\nCopiando apktool para /usr/local/bin ....\n")

        try:
            os.system("cp -a ./apktool/apktool.jar /usr/local/bin")
            os.system("cp -a ./apktool/apktool /usr/local/bin")

        # transforma apktool em executavel
            os.system("cd /usr/local/bin; chmod +x apktool")
            os.system("cd /usr/local/bin; chmod +x apktool.jar")
        except:
            print("\nAlgo deu errado...\n")



        # exclui projeto anterior
        print("\nExcluindo projeto anterior....\n")
        try:
            os.system("rm -R " + self.path_apk + self.name_apk_2)
        except:
            print("\nNão há projeto anterior....\n")
            pass



        # executa comandos para desempacotar apk
        print("\n\nIniciando desempacotamento de apk....\n\n")
        os.system("cd " + self.path_apk + "; " + "apktool d " + self.name_apk)



        # cria arquivos de confoguração xml e yml para ser trabalhado
        print("\nInciando criação de arquivos xml e yml....\n")
        self.text.cria_arquivo_vazio("apktool.yml")
        self.text.cria_arquivo_vazio("AndroidManifest.xml")
        print("\nSucesso na criação dos arquivos....\n")



        # importa dados e faz alteração do xml e yml padrao
        print("\n\nImportando dados do xml e yml original e alterando informações de Api....\n\n")
        try:
            self.text.manipula_xml(self.path_apk + self.name_apk_2 + "/AndroidManifest.xml", "AndroidManifest.xml",
                                   'platformBuildVersionCode="19"', 'platformBuildVersionCode="26"')
            self.text.manipula_xml(self.path_apk + self.name_apk_2 + "/apktool.yml", "apktool.yml",
                               "targetSdkVersion: '19'", "targetSdkVersion: '26'")
        except:
            print("\nAlgo deu errado, verifique se não há erros no par_release.txt....\n")
        print("\nArquivos alterados com sucesso....\n")



        # apaga xml yml obsoletos
        try:
            print("\nINICIANDO A EXLCLUSÃO DE XML E YML OBSOLETOS....\n")

            os.system("rm - r " + self.path_apk + self.name_apk_2 +"/AndroidManifest.xml")
            os.system("rm - r " + self.path_apk + self.name_apk_2 +"/apktool.yml")
        except:
            print("\nAlgo deu errado, verifique se não há erros no par_release.txt....\n")
        print("\nArquivos exculidos com sucesso....\n")




        # copia arquivos criados para pasta do apk
        print("\nINICIANDO A TRANSFERENCIA DE XML E YML MODIFICADOS....\n")
        try:
            os.system("cp -a ./AndroidManifest.xml " + self.path_apk + self.name_apk_2)
            os.system("cp -a ./apktool.yml " + self.path_apk + self.name_apk_2)
        except:
            print("\nAlgo deu errado, verifique se não há erros no par_release.txt....\n")
        print("\nArquivos transferidos com sucesso....\n")




        # reempacota app
        print("\nINICIANDO A REEMPACOTAMENTO DE APK....\n")
        try:
            os.system("cd " + self.path_apk + "; " + "apktool b " + self.name_apk_2)
        except:
            print("\nAlgo deu errado, verifique se não há erros no par_release.txt....\n")
        print("\nREEMPACOTAMENTO EXECUTADO COM SUCESSO....\n")


        # apaga apk otimizado obsoleto
        print("\nVerificando se existem desempacotamentos anteriores e excluindo se houver....\n")
        try:
            os.system("rm - r " + self.path_apk + self.data_key[0] + "optimized_for_playstore.apk")
        except:
            print("\nNão existe arquivo para excluir....\n")
        print("\nArquivo exculido com sucesso....\n")



        # apaga apk releaase do buidozer
        #os.system("rm - r " + self.path_apk + self.name_apk)

        # copia arquivo alterado para pasta do apk
        os.system("cp -a " + self.path_apk + self.name_apk_2+"/dist/" + self.name_apk + self.path_apk)
        #
        # assina apk
        self.signature_apk = ("jarsigner -sigalg SHA1withRSA -digestalg SHA1  -signedjar " +
                              self.data_key[0] + " -storepass " + self.data_key[2] + " -keypass " +
                              self.data_key[3] + " -keystore " + self.data_key[5] + self.data_key[1] +
                              ".keystore" + " " + self.path_apk + self.name_apk + " " + self.data_key[0])

        print(self.signature_apk)
        os.system("cd " + self.path_apk + "; " + self.signature_apk)

        self.zipalign = (
            "zipalign -v 4 " + self.path_apk + self.data_key[0] + " " + self.path_apk + self.data_key[
                0] + "optimized.apk")


        try:
            os.system(self.zipalign)



        except:
            os.system(
                "cd /home/kivy/.buildozer/android/platform/android-sdk-23/build-tools/23.0.1/; apt-get install zipalign")
            os.system(self.zipalign)






lauc = Launcher()

lauc.create_keystore()