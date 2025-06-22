# MoodBird Análise de Sentimentos com DistilBERT

Este projeto implementa um classificador de sentimentos utilizando o modelo DistilBERT, treinado na base de dados SST-2. O sistema é capaz de classificar textos como depressivos ou não depressivos.

## Requisitos do Sistema

- Python 3.8 ou superior
- Mínimo de 4GB de RAM
- GPU é recomendada para treinamento (opcional)

## Instalação

1. Clone este repositório:
```bash
git clone https://github.com/PedroRoca7/MoodBird.git
cd https://github.com/PedroRoca7/MoodBird.gitO
```

2. Crie um ambiente virtual Python:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
- No Windows:
```bash
venv\Scripts\activate
```
- No Linux/Mac:
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso do Modelo

### Opção 1: Executar o Modelo Pré-treinado

Para utilizar o modelo já treinado, simplesmente execute:
```bash
python program.py
```

O programa irá:
- Carregar o modelo pré-treinado
- Permitir que você digite textos para análise
- Classificar cada texto como depressivo ou não depressivo
- Mostrar a porcentagem de confiança da classificação

Para sair do programa, digite 'sair'.

### Opção 2: Treinar um Novo Modelo

Se você deseja treinar o modelo novamente:

1. Abra o notebook `distilBert_BaseSST_2.ipynb` usando Jupyter Notebook:
```bash
jupyter notebook
```

2. Execute todas as células do notebook em ordem

O treinamento irá:
- Baixar automaticamente o dataset SST-2
- Treinar o modelo por 2 épocas
- Salvar o modelo treinado na pasta `meu_modelo_distilbertBaseSST-2`

## Estrutura do Projeto

.
├── distilBert_BaseSST_2.ipynb # Notebook para treinamento
├── program.py # Programa para execução do modelo
├── requirements.txt # Dependências do projeto
├── meu_modelo_distilbertBaseSST-2/# Pasta com o modelo treinado
│ ├── config.json
│ ├── pytorch_model.bin
│ └── ...
└── README.md

## Dependências Principais

- transformers>=4.30.0
- datasets>=3.6.0
- torch>=2.0.0
- pandas>=2.2.0
- scikit-learn>=1.0.0
- numpy>=1.17.0
- huggingface-hub>=0.24.0

## Notas Importantes

- O modelo foi treinado para classificação binária (depressivo/não depressivo)
- Os resultados incluem um score de confiança para cada classificação
- O modelo está otimizado para textos em inglês
- O treinamento pode levar alguns minutos, especialmente sem GPU

## Contribuições

Contribuições são bem-vindas! Por favor, sinta-se à vontade para enviar pull requests ou abrir issues para melhorias.
