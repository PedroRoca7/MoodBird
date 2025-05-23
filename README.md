# 🧠 MoodBird — Detectando Sinais de Depressão em Tweets com IA

**MoodBird** é um projeto de inteligência artificial voltado para a **análise de sentimentos com foco na detecção precoce de possíveis sinais de depressão** em postagens no Twitter.

💬 As palavras que usamos nas redes sociais podem revelar muito sobre nosso estado emocional. MoodBird utiliza técnicas de **processamento de linguagem natural (NLP)** e **redes neurais** para analisar padrões linguísticos que podem indicar tristeza profunda, desânimo ou outros sentimentos associados à depressão.

## 🎯 Objetivo

Ajudar a identificar possíveis sinais de **depressão** com base em tweets, apoiando estudos e ferramentas que contribuam para o **bem-estar mental** e possibilitem **intervenções preventivas**.

## 🛠️ O que o projeto faz:

- Coleta e pré-processamento de tweets  
- Limpeza textual, remoção de *stopwords*, emojis e lematização  
- Treinamento de modelo de IA (LSTM) para classificação de sentimentos  
- Detecção de padrões de linguagem associados a sintomas depressivos  
- Visualizações e métricas para avaliar o desempenho do modelo  

## ⚠️ Importante

Este projeto tem fins **educacionais e experimentais**.  
**Não substitui diagnóstico médico.** Sempre procure profissionais de saúde mental para orientação adequada.

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/PedroRoca7/MoodBird-.git
cd MoodBird
```

2. Instale as dependências (isso também baixará automaticamente os recursos do NLTK):
```bash
pip install -e .
```

Ou alternativamente:
```bash
pip install -r requirements.txt
python setup.py
```