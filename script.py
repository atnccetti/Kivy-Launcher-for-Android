# coding=utf-8
import os
import pexpect
from sub_text import ManipulaTxt
import time

interval = 0.2

class Launcher():

    def __init__(self):
        self.file = "par_release.txt"
        

    def create_keystore(self, ):
        """

        :return:
        """

        print("\n\n---Starting Keystore Creation---....\n"
              "---Iniciando a criação da Keystore---\n")
        time.sleep(interval)


        #data keystore
        #dados da keystore
        self.alias = self.le_line_script(self.file,"aliasname")
        self.name_key = self.le_line_script(self.file,"keyname")
        self.storepass = self.le_line_script(self.file,"keystore")
        self.keypass = self.le_line_script(self.file,"keypass")
        self.validity = self.le_line_script(self.file,"validity")
        self.keypath = self.le_line_script(self.file,"path_key")
        self.api = self.le_line_script(self.file,"api")
        self.name = self.le_line_script(self.file, "name")
        self.organizational_unit = self.le_line_script(self.file, "organizational_unit")
        self.your_organization = self.le_line_script(self.file, "your_organization")
        self.city = self.le_line_script(self.file, "city")
        self.estate = self.le_line_script(self.file, "estate")
        self.nation = self.le_line_script(self.file, "nation")
        self.path_zipalign = self.le_line_script(self.file, "zipalign")

        #this list is created to serve as parameters for the "create_apk" function.
        #esta lista é criada para ser parametro da função "creat apk".
        self.data_key = [self.alias,
                         self.name_key,
                         self.storepass,
                         self.keypass,
                         self.validity,
                         self.keypath
                         ]


        #variable is associated with the command to create keystore.
        #variável é associada a comando para criar keystore.
        self.key = "keytool -genkey -v -keystore "+self.keypath + \
                   self.name_key+".keystore -alias " + \
                   self.alias + " -storepass " + \
                   self.storepass +" -keypass " + \
                   self.keypass + " -keyalg RSA -validity " + \
                   self.validity

        if self.check_file_exists("file", self.name_key, self.keypath ) == True:

            print("\n----KEY ALREADY EXIST IN THE BOARD OF DIRECTORS, MOVING ON----\n"
                  "----KEY JÁ EXISTE NI DIRETÓRIO, SEGUNDO EM FRENTE----\n")

            time.sleep(interval)
        try:
            self.p = pexpect.spawn(self.key, timeout=10)
            self.p.expect('What.*?')
            self.p.sendline(self.name)
            self.p.expect('What.*?')
            self.p.sendline(self.organizational_unit)
            self.p.expect('What.*?')
            self.p.sendline(self.your_organization)
            self.p.expect('What.*?')
            self.p.sendline(self.city)
            self.p.expect('What.*?')
            self.p.sendline(self.estate)
            self.p.expect('What.*?')
            self.p.sendline(self.nation)
            self.p.expect('Is.*?:')
            self.p.sendline("yes")
            self.p.expect(pexpect.EOF)
            # print (self.p.before)
            self.create_apk(self.data_key)

        except:
            print("\n----KEY ALREADY EXIST IN THE BOARD OF DIRECTORS, MOVING ON----\n"
                  "----KEY JÁ EXISTE NI DIRETÓRIO, SEGUNDO EM FRENTE----\n")
            time.sleep(interval)
            self.create_apk(self.data_key)

    def create_apk(self, data_key):
        """
        :param type: debug, release, deploy run, clean
        :param path_apk: /home/kivy/Desktop/helloword/bin/
        :param name_apk:
        :param data_key: ['aliasname', 'namekey', 'stor183590', 'key183590', '14000', '/home/kivy/Desktop/']
        :return:
        """
        print("\n----Starting work on apk----....\n"
              "----Iniciando trabalho no app---\n")
        time.sleep(interval)

        self.path_apk = self.le_line_script(self.file,"path_apk")
        self.name_apk = self.le_line_script(self.file,"name_apk")
        self.data_key = data_key
        self.name_apk_2 = self.name_apk.replace(".apk", "")



        # copia apktool para pasta sistema
        print("\n----Copying apktool to /usr/local/bin----....\n"
              "----Copiando apktool para /usr/local/bin----\n")
        time.sleep(interval)

        os.system("cp -a ./apktool/apktool.jar /usr/local/bin",)
        os.system("cp -a ./apktool/apktool /usr/local/bin")
        os.system("cd /usr/local/bin; chmod +x apktool")
        os.system("cd /usr/local/bin; chmod +x apktool.jar")


        # exclui projeto anterior
        print("\n---- Excluding previous apkatools folder, if any ----....\n"
              "----Excluindo pasta anterior do apkatools, caso exista----")
        time.sleep(interval)
        if self.check_file_exists("dir", self.path_apk, self.name_apk_2) == True:
            os.system("rm -R " + self.path_apk + self.name_apk_2)
        elif self.check_file_exists("dir", self.path_apk, self.name_apk_2) == False:
            print("\n----No previous project----\n"
                  "----Não há projeto anterior----....\n")
            time.sleep(interval)


        # executa comandos para desempacotar apk
        print("\n----Starting apk unpacking----....\n"
              "\n----Iniciando desempacotamento de apk----....\n")
        os.system("cd " + self.path_apk + "; " + "apktool d " + self.name_apk)
        time.sleep(interval)


        # cria arquivos de confoguração xml e yml para ser trabalhado
        print("\n----Inciando criação de arquivos xml e yml----....\n")
        self.cria_arquivo_vazio("apktool.yml")
        self.cria_arquivo_vazio("AndroidManifest.xml")
        time.sleep(interval)
        print("\n----Sucesso na criação dos arquivos----....\n")
        time.sleep(interval)


        # importa dados e faz alteração do xml e yml padrao
        print("\n\n----Importando dados xml e yml original e alterando informações de Api----....\n\n")
        time.sleep(interval)
        self.manipula_xml(self.path_apk + self.name_apk_2 + "/AndroidManifest.xml", "AndroidManifest.xml",
                               'platformBuildVersionCode="19"', 'platformBuildVersionCode="' + self.api +'"')
        self.manipula_xml(self.path_apk + self.name_apk_2 + "/apktool.yml", "apktool.yml",
                           "targetSdkVersion: '19'", "targetSdkVersion: '"+ self.api +"'")
        print("\n----Arquivos alterados com sucesso----....\n")
        time.sleep(interval)


        # apaga xml yml obsoletos
        print("\n----INICIANDO A EXLCLUSÃO DE XML E YML OBSOLETOS----....\n")
        time.sleep(interval)
        os.system("rm - r " + self.path_apk + self.name_apk_2 +"/AndroidManifest.xml")
        os.system("rm - r " + self.path_apk + self.name_apk_2 +"/apktool.yml")
        print("\n----Arquivos exculidos com sucesso....----\n")


        # copia arquivos criados para pasta do apk
        print("\n----INICIANDO A TRANSFERENCIA DE XML E YML MODIFICADOS----....\n")
        time.sleep(interval)
        os.system("cp -a ./AndroidManifest.xml " + self.path_apk + self.name_apk_2)
        os.system("cp -a ./apktool.yml " + self.path_apk + self.name_apk_2)
        print("\n----Arquivos transferidos com sucesso----....\n")
        time.sleep(interval)


        # reempacota app
        print("\n----INICIANDO A REEMPACOTAMENTO DE APK----....\n")
        time.sleep(interval)
        os.system("cd " + self.path_apk + "; " + "apktool b " + self.name_apk_2)
        print("\n----REEMPACOTAMENTO EXECUTADO COM SUCESSO----....\n")
        time.sleep(interval)


        # apaga apk otimizado obsoleto
        print("\n----Verificando se existem desempacotamentos anteriores e excluindo se houver----....\n")
        time.sleep(interval)
        if self.check_file_exists("file" ,self.data_key[0] + "optimized_for_playstore.apk", self.path_apk ) == True:
            os.system("rm - r " + self.path_apk + self.data_key[0] + "optimized_for_playstore.apk")
            print("\n----Arquivo excluido----....\n")
        elif self.check_file_exists("file" ,self.data_key[0] + "optimized_for_playstore.apk", self.path_apk ) == False:

            print("\n----Não existe arquivo para excluir----....\n")


        # apaga apk releaase do buidozer
        os.system("rm - r " + self.path_apk + self.name_apk)


        # copia arquivo alterado para pasta do apk
        print("\n----CRIANDO APKA COM NOVA API----....\n")
        time.sleep(interval)
        os.system("cp -a " + self.path_apk + self.name_apk_2+"/dist/" + self.name_apk +" " + self.path_apk)


        # assina apk
        print("\n----ASSINANDO APP----....\n")
        time.sleep(interval)
        self.signature_apk = ("jarsigner -sigalg SHA1withRSA -digestalg SHA1  -signedjar " +
                              self.data_key[0] + " -storepass " + self.data_key[2] + " -keypass " +
                              self.data_key[3] + " -keystore " + self.data_key[5] + self.data_key[1] +
                              ".keystore" + " " + self.path_apk + self.name_apk + " " + self.data_key[0])


        os.system("cd " + self.path_apk + "; " + self.signature_apk)

        self.zipalign = (
            "zipalign -v 4 " + self.path_apk + self.data_key[0] + " " + self.path_apk + self.data_key[
                0] + "optimized_for_playstore.apk")


        try:
            print("\n ----INICIANDO ZIPALIGN----....\n")
            os.system(self.zipalign)

            time.sleep(interval)
        except:
            os.system(
                self.path_zipalign+"; apt-get install zipalign")
            os.system(self.zipalign)
            print("\n ----ZIPALIGN NÃO EXISTE, INSTALANDO----....\n")
            time.sleep(interval)
        print("\n\n\n----YOUR APP IS READY----\n"
              "----SEU APP ESTÁ PRONTO----\n\n\n\n"
              "----I recommend backing up your par_release, there is information about your keystore.----\n"
              "----Aconselho fazer backup do seu par_release, pois há informaçoes da sua keystore.\n\n"
              "----In the future there will be a version manager----\n"
              "----Futuramente haverá um gerenciador de versões\n \n")



    def check_file_exists(self, tip, name, path):
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

    def le_line_script(self, x, y):
        """
        função para script.py
        :param x: name file
        :param y: name_data
        :return: le linha do arquivo e transforma em lista com split
        e retorna valor do segundo item como parametro
        """
        with open(x, "r") as self.f:
            for line in self.f:
                divide = line.split("=")
                if divide[0] == y:
                    return divide[1].replace("\n","")


    def manipula_xml(self, x, file_origin, alterar_de, alterar_para):
        """
        :param x:  arqquivo a ser alterado
        :param file_origin: arquivo originario, local e nome
        :param alterar:   dados a ser alterado, de para
        :return:
        """
        with open(x, "r") as self.f:
            for line in self.f:
                lm = str(line)
                m= (lm.replace(alterar_de , alterar_para))
                self.create_file_line(m, file_origin)

    def create_file_line(self, x, y):
        """
        :param x: valor da linha a ser adicionada
        :param y: nome do arquivo em que a linha será adicionada
        :return: adiciona linha no arquivo definido por parametro (y)
        """
        try:
            self.arquivo_1 = open(y, 'r')
            self.conteudo = self.arquivo_1.readlines()
            self.conteudo.append(x)
            self.arquivo_1 = open(y, 'w')
            self.arquivo_1.writelines(self.conteudo)
        finally:
            self.arquivo_1.close()


    def cria_arquivo_vazio(self, x):
        """
        :param x: nome do arquivo a ser crido
        :return:funcao cria arquivo vazio
        """
        with open(x, "w") as self.f:
            self.f.close()

lauc = Launcher()
lauc.create_keystore()