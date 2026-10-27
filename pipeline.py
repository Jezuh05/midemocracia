"""
MiDemocracIA - Pipeline de Preprocesamiento e Inferencia NLP
Proyecto colaborativo de Inteligencia Artificial - Saturdays.AI (Universidad de Alicante)
Autor / Responsable de Datos: Jesús Mariano Núñez Fernández
"""

import re
import os
import joblib
import nltk
from nltk.corpus import stopwords

# Asegurar recursos lingüísticos necesarios de NLTK
try:
    _ = stopwords.words('spanish')
except LookupError:
    nltk.download('stopwords', quiet=True)

class LegislativeNLPClassifier:
    """
    Clasificador de iniciativas parlamentarias basado en NLP y Regresión Logística
    entrenado sobre el corpus legislativo del Congreso de los Diputados (L11-L15).
    """

    def __init__(self, model_path=None, vectorizer_path=None):
        self.stop_words = set(stopwords.words('spanish'))
        self.model = None
        self.vectorizer = None

        if model_path and os.path.exists(model_path):
            self.model = joblib.load(model_path)
        if vectorizer_path and os.path.exists(vectorizer_path):
            self.vectorizer = joblib.load(vectorizer_path)

    @staticmethod
    def extract_text_from_pdf(pdf_path: str) -> str:
        """Extrae el contenido textual de un archivo PDF utilizando PyMuPDF."""
        try:
            import fitz
        except ImportError:
            raise ImportError("PyMuPDF no está instalado. Ejecuta 'pip install pymupdf'.")

        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"No se encontró el documento PDF en: {pdf_path}")

        doc = fitz.open(pdf_path)
        text = "".join(page.get_text() for page in doc)
        return text

    def clean_text(self, text: str) -> str:
        """
        Normaliza el texto legal:
        1. Conversión a minúsculas.
        2. Supresión de dígitos y signos no alfanuméricos.
        3. Poda de stopwords en español.
        4. Recorte de cabeceras/pies burocráticos parlamentarios.
        """
        text = text.lower()
        text = re.sub(r'\d+', ' ', text)
        text = re.sub(r'\W+', ' ', text)
        words = text.split()
        words = [w for w in words if w not in self.stop_words]

        # Recorte de fórmulas oficiales iniciales y finales si el texto es extenso
        if len(words) > 40:
            words = words[20:-20]

        return " ".join(words)

    def predict(self, raw_text: str):
        """Genera una predicción a partir de texto en bruto normalizado."""
        if not self.model or not self.vectorizer:
            raise RuntimeError("El modelo o el vectorizador no han sido cargados correctamente.")

        cleaned = self.clean_text(raw_text)
        vec = self.vectorizer.transform([cleaned])
        return self.model.predict(vec)[0]


if __name__ == "__main__":
    print("=" * 60)
    print("MiDemocracIA - NLP Pipeline (Saturdays.AI Alicante)")
    print("=" * 60)
    pipeline = LegislativeNLPClassifier()
    sample_text = (
        "Proposición de ley relativa a la reforma del mercado eléctrico y "
        "fijación de tarifas reguladas para la protección del consumidor vulnerable."
    )
    cleaned_sample = pipeline.clean_text(sample_text)
    print("\n[✓] Módulo de procesamiento y pipeline NLP cargado correctamente.")
    print(f"Texto original:\n  {sample_text}")
    print(f"\nTexto normalizado (sin stopwords):\n  {cleaned_sample}\n")
