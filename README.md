# MiDemocracIA - Análisis Legislativo con Procesamiento del Lenguaje Natural (NLP)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![NLP](https://img.shields.io/badge/NLP-NLTK%20%7C%20Bag%20of%20N--grams-green)](https://www.nltk.org/)
[![Saturdays.AI](https://img.shields.io/badge/Saturdays.AI-Universidad%20de%20Alicante-red)](https://saturdays.ai/)

> Proyecto de Inteligencia Artificial desarrollado y presentado en el programa **Saturdays.AI (Edición Universidad de Alicante)**.

---

## 📌 Visión del Proyecto

**MiDemocracIA.es** nace con el objetivo de acercar la actividad legislativa y parlamentaria a la ciudadanía de forma transparente y accesible. Mediante técnicas de **Procesamiento del Lenguaje Natural (NLP)** y **Machine Learning**, el sistema procesa el texto íntegro de propuestas de ley y proyectos legislativos publicados por el Congreso de los Diputados, prediciendo su orientación en dos ejes políticos fundamentales:

1. **Eje Económico:** Tendencia de intervención pública vs. Libre mercado (Izquierda / Derecha).
2. **Eje Social:** Enfoque en libertades y derechos sociales (Progresista / Conservador).

Permite además evaluar la afinidad ideológica de los usuarios respecto a las leyes debatidas y la disciplina de voto de los diferentes grupos parlamentarios.

---

## 👥 Equipo del Proyecto

* **Jesús Mariano Núñez Fernández** - Desarrollo / Machine Learning & Data Pipeline
* **Leticia** - Estudiante de Ingeniería Informática
* **José** - Informático y Diseñador Gráfico
* **Fran García** - Analista Político y Emprendedor

---

## 🏗️ Pipeline de Datos y Arquitectura de Machine Learning

```
[PDFs Congreso / Leyes] 
         │
         ▼
[Extracción de Texto: PyMuPDF / fitz]
         │
         ▼
[Preprocesamiento: Regex + NLTK Stopwords en Español]
         │
         ▼
[Vectorización: CountVectorizer (N-grams 1-2)]
         │
         ├───► [Modelo Eje Económico: Regresión Logística] ───► Inferencia & Export (.pkl)
         │
         └───► [Modelo Eje Social: Regresión Logística]    ───► Inferencia & Export (.pkl)
```

### 1. Ingesta y Extracción de Documentos
* Extracción programática del texto de las iniciativas legales en formato PDF mediante `PyMuPDF` (`fitz`).

### 2. Limpieza y Normalización Textual (NLP)
* Conversión a minúsculas, eliminación de caracteres no alfanuméricos y dígitos mediante expresiones regulares.
* Filtrado exhaustivo de palabras vacías (*stopwords*) en lengua castellana con `NLTK`.
* Poda de cabeceras y pies de página burocráticos parlamentarios para aislar el cuerpo articulado de la ley.

### 3. Vectorización y Modelado
* Pruebas comparativas entre diferentes estrategias de representación textual:
  * **Bag of N-grams** (1-gram y 2-grams) *(Estrategia con mejor rendimiento)*
  * Bag of Words
  * TF-IDF
  * Word Embeddings
* Algoritmo clasificador: **Regresión Logística multiclase / binomial** optimizada con `max_iter=1000`.
* Validación cruzada y evaluación con partición aleatoria `train_test_split` (80% entrenamiento / 20% test).

### 4. Métricas de Rendimiento
* **Exactitud global (Accuracy):** **71%** en conjunto de test sobre leyes de las legislaturas L11 a L15.
* Métricas detalladas de precisión, recall y F1-score por categoría calculadas con `classification_report`.
* Exportación de modelos y vectorizadores con `joblib` para integración en servicios web.

---

## 🚀 Instalación y Uso en Local

### Requisitos previos
* Python 3.9 o superior.
* Gestor de paquetes `pip`.

### 1. Clonar el repositorio
```bash
git clone https://github.com/Jezuh05/midemocracia.git
cd midemocracia
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar el Notebook
Abre el entorno interactivo en Jupyter Lab, VS Code o Google Colab:
```bash
jupyter notebook "Modelo Social Y Economico.ipynb"
```

---

## 📄 Licencia y Reconocimientos
Proyecto realizado con fines académicos y de investigación en Saturdays.AI Alicante.
Repositorio original de trabajo colaborativo: [FranGarciaBis/midemocracia](https://github.com/FranGarciaBis/midemocracia).
