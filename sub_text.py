# coding=utf-8


class ManipulaTxt():

    def __init__(self):
        pass


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


    def le_line(self, x):
        """
        :param x: nome do arquivo a ser lido
        :return: print linhas do arquivo
        """
        with open(x, "r") as self.f:
            for line in self.f:
                print(line)
                return line


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
        with open('3.txt', 'r') as self.f:
            for line in self.f:
                if line[0:10] == "  minSdkVe":
                    self.cria_arquivo_line("  minSdkVersion: '19'\n", x)

                elif line[0:10] == "  targetSd":
                    self.cria_arquivo_line("  targetSdkVersion: '29'\n", x)
                else:
                    self.cria_arquivo_line(line, x)


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
                self.cria_arquivo_line(m, file_origin)

