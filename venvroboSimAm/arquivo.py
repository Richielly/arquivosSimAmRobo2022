import os
import glob
import shutil

caminho_origem = 'C:\\Users\\equiplano\\Downloads\\'
caminho_destino = 'C:\\Users\\equiplano\\Downloads\\SimAm\\'
#caminho_destino = os.getcwd() + '/RepositorioArquivosSimAm'
class Arquivo:
    def renomear_arquivo(competencia,exercicio):
        os.chdir(caminho_origem)
        arquivos = (glob.glob('Layout_*'))
        Arquivo.criar_diretorio(exercicio)
        #os.rename(arquivos[0],caminho_destino + str(exercicio) + '\\'+str(competencia)+'_'+str(exercicio)+'.zip')
        nome = {'Abertura de Exercício':'00','Janeiro':'01','Fevereiro':'02','Março':'03','Abril':'04','Maio':'05',
                'Junho':'06','Julho':'07','Agosto':'08','Setembro':'09','Outubro':'10','Novembro':'11',
                'Dezembro':'12','Encerramento de Exercício':'13'}
        os.rename(arquivos[0],caminho_destino + str(exercicio) + '\\' + str(nome[competencia]) +'.zip')

    def criar_diretorio(exercicio):

        if os.path.exists("C:\\Users\\equiplano\\Downloads\\SimAm\\"+str(exercicio)):
            return True
        else:
            caminho = os.makedirs("C:\\Users\\equiplano\\Downloads\\SimAm\\"+str(exercicio))
            return False

    def listar_dirretorios(self):
        pass

    def criar_arquivo_log():
        log = open('log.txt', 'w')
        log.close()

    def registrar_log(mensagem):
        os.chdir(caminho_origem)
        if os.path.exists("log.txt"):
            arquivo = open('log.txt', 'r')
            log = arquivo.readlines()
            log.append(mensagem+'\n')

            arquivo = open('log.txt', 'w')
            arquivo.writelines(log)

            arquivo.close()
            return True

        else:
            Arquivo.criar_arquivo_log()
            arquivo = open('log.txt', 'r')
            log = arquivo.readlines()
            log.append(mensagem + '\n')

            arquivo = open('log.txt', 'w')
            arquivo.writelines(log)
            arquivo.close()

    def contar_arquivos(self):
        exercicios_baixados = os.listdir(caminho_destino)
        exercicios_pendentes = []
        competencias_pendentes = []
        quantidade_exercicios = len(exercicios_baixados)
        print('\nQuantidade de Exercicios: '+str(quantidade_exercicios))
        Arquivo.registrar_log('\nQuantidade de Exercicios: '+str(quantidade_exercicios))
        print("Exercicios baixados: " + str(exercicios_baixados))
        Arquivo.registrar_log("Exercicios baixados: " + str(exercicios_baixados))

        for exercicio in exercicios_baixados:
            competecias_baixadas = os.listdir(caminho_destino + '\\' + str(exercicio))

            print("\nQuantidade Competencias baixadas por Exercicio: "+ str(len(competecias_baixadas))+" em "+ str(exercicio))
            Arquivo.registrar_log("\nQuantidade Competencias baixadas por Exercicio: "+ str(len(competecias_baixadas))+" em "+ str(exercicio))
            if len(competecias_baixadas) < 14:
                print("Exercicio com falta de Arquivos: " + str(exercicio))
                Arquivo.registrar_log("Exercicio com falta de Arquivos: " + str(exercicio))
                exercicios_pendentes.append(exercicio)
        return exercicios_pendentes

    def contar_competencias(self,exercicio):

        competencias = os.listdir(caminho_destino + '\\' + str(exercicio))
        return competencias

    def deletarZip():

        #Acesso a pasta onde estão os arquivos baixados
        os.chdir('C:\\Users\\equiplano\\Downloads\SimAm')
        #Listando os exercicios encontrados
        origem = os.listdir()
        for diretorios in origem:
            #acessando as pastas pelos exercicios encontrados
            os.chdir('C:\\Users\\equiplano\\Downloads\SimAm'+'\\'+diretorios)
            #Armazenando em lista arquivos com extensão .zip
            excluir = (glob.glob('*zip'))
            # Excluindo arquivos na pasta com extensão .zip
            for item in excluir:
                #Removendo item a item da lista
                os.remove(item)

    def grafico(self):
        grafico = []
        exercicios_baixados = os.listdir(caminho_destino)
        for exercicio in exercicios_baixados:
            competencias_baixadas = os.listdir(caminho_destino+'\\'+ exercicio)
            grafico.append([exercicio,competencias_baixadas])
        return grafico

    def validarArquivoTexto(exercicio, competencia):

        os.chdir(caminho_destino + '\\' + exercicio + '\\' + competencia + '\\Contabil')

        linhas = open('DiarioContabilidade.txt', 'r')
        texto = linhas.read()

        texto_competencia = texto.split('-')

        texto_exercicio = texto_competencia[0]
        texto_exercicio = texto_exercicio[-4::]

        # print("Exercicio: ", texto_exercicio)
        # print("Competêcia: ", texto_competencia[1])

        return texto_exercicio, texto_competencia[1]

    def varrerDiretorios(self):
        dado = []
        dados = []
        exercicios = os.listdir(caminho_destino)

        for exercicio in exercicios:
            competencias = os.listdir(caminho_destino + exercicio)

            for competencia in competencias:
                pastas = os.listdir(caminho_destino + '\\' + exercicio + '\\' + competencia)
                for pasta in pastas:
                    arquivos = os.listdir(caminho_destino + exercicio + '\\' + competencia + '\\' + pasta)
                    dado = exercicio, competencia, arquivos, pasta
                    dados.append(dado)
        return dados

    def varrerDiretoriosFiltro(self, exercicio, competencia, pasta):
        dado = []
        dados = []
        arquivos = os.listdir(caminho_destino + str(exercicio) + '\\' + str(competencia) + '\\' + str(pasta))
        dado = arquivos
        dados.append(dado)
        return dados

        # print("Pastas diretorio principal exercícios: ", exercicios)
        # competencias = os.listdir(caminho_destino + '\\' + exercicios[0])
        # print("Competencias: ", competencias)
        # pastas = os.listdir(caminho_destino + '\\' + exercicios[0] + '\\' + competencias[1])
        # print("Pastas: ", pastas)
        # arquivos = os.listdir(caminho_destino + '\\' + exercicios[0] + '\\' + competencias[1] + '\\Contabil')
        # print("Arquivos txt: ", arquivos)
# exercicios = ['2016','2017']
# for exercicio in exercicios:
#     varredura = Arquivo.validarArquivoTexto(exercicio, '02')
#
#     print(varredura)
