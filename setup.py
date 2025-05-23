# setup.py
from setuptools import setup
import nltk

def download_nltk_data():
    nltk.download('stopwords')
    nltk.download('wordnet')

setup(
    name="MoodBird",
    version="0.1",
    packages=[],
    install_requires=[
        'pandas>=2.0.0',
        'numpy>=1.24.0',
        'seaborn>=0.12.0',
        'matplotlib>=3.7.0',
        'nltk>=3.8.1',
        'tensorflow>=2.15.0',
        'emoji>=2.8.0',
        'scikit-learn>=1.3.0',
    ],
    python_requires='>=3.8',
)

# Executa o download dos recursos do NLTK após a instalação
download_nltk_data()