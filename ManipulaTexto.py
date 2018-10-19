# coding=utf-8


class ManipulaTxt():
    def __init__(self):
        pass

    def le_line(self, x):
        """
        :param x: nome do arquivo a ser lido
        :return: print linhas do arquivo
        """
        with open("apktool.yml", "r") as self.f:
            for line in self.f:
                print line


    def cria_arquivo_vazio(self, x):
        """
        :param x: nome do arquivo a ser crido
        :return:funcao cria arquivo vazio
        """
        with open(x, "w") as self.f:
            self.f.close()


    def cria_arquivo_line(self, x, y):
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


    def le_line_cria(self, nome_arquivo_lido, novo_arquivo_gravado ):
        """
        le arquivo passado como parametro
        :param y: novo arquivo a ser gravado
        :param x: arquivo que será lido
        :return: cria novo arquivo com nome definido por parametro,
        """
        with open(nome_arquivo_lido, 'r') as self.f:
            for line in self.f:
                self.cria_arquivo_line(line, novo_arquivo_gravado)


    def get_dat(self,x):
        """procura linhas conforme filtro
        e adiciona no documento escolhido por parametro
        x = nome do arquivo que linha será adicionada
        """
        self.f = open('3.txt', 'r')
        for line in self.f:
            if line[0:10] == "  minSdkVe":
                self.cria_arquivo_line("  minSdkVersion: '19'\n", x)

            elif line[0:10] == "  targetSd":
                self.cria_arquivo_line("  targetSdkVersion: '29'\n", x)
            else:
                self.cria_arquivo_line(line, x)


    def manipula_xml(self):
        with open('AndroidManifest.xml', "r") as self.f:
            for line in self.f:
                if line.replace("platformBuildVersionCode=19","platformBuildVersionCode=28" ):
                    print line



ManipulaTxt().cria_arquivo_vazio("novo.yml")
ManipulaTxt().cria_arquivo_vazio("3.txt")
ManipulaTxt().le_line_cria('apktool.yml', '3.txt')
ManipulaTxt().get_dat("novo.yml")

ManipulaTxt().cria_arquivo_vazio("novo.xml")
ManipulaTxt().le_line_cria('AndroidManifest.xml', 'novo.xml')


