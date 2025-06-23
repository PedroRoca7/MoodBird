import os
import logging
import warnings

# Configurações para suprimir avisos
warnings.filterwarnings('ignore')  # Ignora todos os avisos
logging.getLogger('tensorflow').setLevel(logging.ERROR)  # Configura logging do TF para mostrar apenas erros
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suprime avisos do TensorFlow

from transformers import pipeline

# Obtém o diretório onde o arquivo program.py está localizado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo para a pasta do modelo
caminho_modelo = os.path.join(diretorio_atual, "meu_modelo_distilbertBaseSST-2")

# pipeline de classificação com modelo salvo
classificador = pipeline("text-classification", 
                       model=caminho_modelo, 
                       tokenizer=caminho_modelo)

def analisar_texto(texto):
    resultado = classificador(texto)
    label = resultado[0]['label']
    score = resultado[0]['score']
    
    if label == 'LABEL_1':
        mensagem = "Texto não depressivo"
    else:
        mensagem = "Texto depressivo"
    
    print(f"\nResultado da análise:")
    print(f"Classificação: {mensagem}")
    print(f"Confiança: {score:.2%}")

# Loop principal para interação via terminal
print("=== Análise de Sentimentos ===")
print("Digite 'sair' para encerrar o programa")

while True:
    texto = input("\nDigite o texto para análise: ")
    
    if texto.lower() == 'sair':
        print("Programa encerrado.")
        break
    
    analisar_texto(texto)