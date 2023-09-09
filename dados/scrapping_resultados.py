from zipfile import ZipFile, is_zipfile
from requests import get
from io import BytesIO
import pandas as pd
import urllib3

urllib3.disable_warnings()

#URL = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=lotofacil'
path = './Lotofacil.csv'

def html_resultados(path):
	"""
	Obtém os dados de todos os sorteios da lotofácil.
	
	:param url: Endereço para obter o arquivo ZIP
	com os dados dos sorteios da lotofácil
	
	:returns: Conteúdo HTML do arquivo ZIP

	"""
	"""resposta = get(url, stream = True, verify = False)
	verifica_zip = is_zipfile(BytesIO(resposta.content))

	if verifica_zip:
		arquivo = ZipFile(BytesIO(resposta.content))
		
		with arquivo as zip:
			dados = zip.read('d_lotfac.htm')
		zip.close

		return dados
		"""
	

	
#html = html_resultados(URL)

# Cria uma lista a partir da variável (html)
#dados = read_html(html)

#tratar xlsx em csv

dados = pd.read_csv(path)

# Obtém os dados de todos os sorteios
base = dados[0].iloc[:, [*[i for i in range(17)], 18]]

# Remove dados duplicados
base = base.drop_duplicates('Concurso')

# Renomeia as colunas do DataFrame
colunas = {'Bola1': 'B1', 'Bola2': 'B2', 'Bola3': 'B3', 'Bola4': 'B4', 'Bola5': 'B5',
		   'Bola6': 'B6', 'Bola7': 'B7', 'Bola8': 'B8', 'Bola9': 'B9', 'Bola10': 'B10',
		   'Bola11': 'B11', 'Bola12': 'B12', 'Bola13': 'B13', 'Bola14': 'B14', 'Bola15': 'B15',
		   'Ganhadores_15_Acertos': 'Ganhou'}

base.rename(columns=colunas, inplace=True)

# Exporta os dados em arquivo CSV
base.to_csv('./base/resultados.csv', sep=';', encoding='utf8', index=False)


if __name__ == '__main__':

	# Informações
	concurso = base['Concurso'].max()
	data = str(base[base['Concurso'] == concurso]['Data Sorteio'])[8:18]

	print(f'\n\033[1;32mTODOS OS RESULTADOS DOS CONCURSOS DA LOTOFÁCIL FORAM BAIXADOS COM SUCESSO!\033[m')
	print(f'\n\n\033[1;36mÚltimo sorteio:\033[m {data}\n\033[1;36mConcurso:\033[m {concurso}')

	print(f'\n\n\033[1;35mArquivo salvo em:\033[m \033[1;33m./base/resultados.csv\033[m')
