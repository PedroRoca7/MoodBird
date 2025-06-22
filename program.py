from transformers import pipeline

# pipeline de classificação com modelo salvo
classificador = pipeline("text-classification", model="./meu_modelo_distilbertBaseSST-2", tokenizer="./meu_modelo_distilbertBaseSST-2")

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