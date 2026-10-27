# MiDemocracIA - Análisis Legislativo con Procesamiento del Lenguaje Natural (NLP)

[![Saturdays.AI](https://img.shields.io/badge/Saturdays.AI-Edición%20Universidad%20de%20Alicante%20(2024)-red?style=for-the-badge&logo=ai&logoColor=white)](https://saturdays.ai/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![NLP](https://img.shields.io/badge/NLP-NLTK%20%7C%20Bag%20of%20N--grams-green?style=for-the-badge)](https://www.nltk.org/)

> 🎓 **Proyecto de Inteligencia Artificial desarrollado en el programa [Saturdays.AI](https://saturdays.ai/) (Sede Universidad de Alicante, edición 2024).**  
> Saturdays.AI es un movimiento internacional sin ánimo de lucro orientado a hacer accesible la educación en Inteligencia Artificial mediante proyectos prácticos con impacto social real.

---

## 📌 Contexto y Caso de Uso (Civic Tech)

Proyecto en equipo multidisciplinar

**MiDemocracIA** es una iniciativa de tecnología cívica orientada a facilitar la comprensión y transparencia de la actividad parlamentaria en España. 

La lectura y análisis de textos legales publicados en el Boletín Oficial de las Cortes Generales (BOCG) resulta compleja e inaccesible para el ciudadano medio debido a su extensión y jerga burocrática. El objetivo del proyecto fue diseñar un **pipeline de Procesamiento del Lenguaje Natural (NLP)** capaz de clasificar de manera automatizada las iniciativas legislativas del Congreso de los Diputados en dos dimensiones políticas fundamentales:

1. **Eje Económico:** Tendencia hacia la intervención pública / regulación vs. Libre mercado y desregulación.
2. **Eje Social:** Enfoque en libertades y derechos individuales / progresismo vs. Modelos tradicionales / conservadurismo.

El sistema permite contrastar las posturas de los diferentes grupos parlamentarios con los textos de las leyes efectivamente tramitadas.

---

## 👥 Equipo Multidisciplinar

El proyecto fue desarrollado en equipo durante las sesiones de Saturdays.AI en el campus de la **Universidad de Alicante**:

* **Jesús Mariano Núñez Fernández** — *Data Pipeline, Preprocesamiento NLP, Experimentación de Modelos de Machine Learning y Serialización.*
* **Leticia** — *Estudiante de Grado en Ingeniería Informática, Encargada del fronted (No se pudo recuperar esa parte del proyecto).*
* **José** — *Sistemas y Diseño Gráfico.*
* **Fran García** — *Analista Político y Coordinación de Negocio.*

*Repositorio colaborativo de desarrollo de la iniciativa:* [FranGarciaBis/midemocracia](https://github.com/FranGarciaBis/midemocracia).

---

## 🏗️ Metodología y Pipeline de Datos

```
[PDFs Oficiales del Congreso (L11-L15)] 
                 │
                 ▼
[Extracción de Texto: PyMuPDF / fitz]
                 │
                 ▼
[Preprocesamiento: Regex + Filtrado NLTK Stopwords en Español]
                 │
                 ▼
[Poda de Cabeceras/Pies Burocráticos de Documento]
                 │
                 ▼
[Vectorización: CountVectorizer (N-grams 1-2)]
                 │
                 ├───► [Modelo Eje Económico: Regresión Logística] ───► Exactitud: 71%
                 │
                 └───► [Modelo Eje Social: Regresión Logística]    ───► Clasificación Binaria
```

### 1. Ingesta y Extracción de Documentos Legales
* Procesamiento automatizado de decenas de iniciativas en formato PDF parlamentario mediante `PyMuPDF` (`fitz`), extrayendo el contenido textual íntegro.

### 2. Preprocesamiento y Normalización Textual (NLP)
* Conversión a minúsculas y eliminación sistemática de números, caracteres especiales y puntuación.
* Eliminación de palabras vacías (*stopwords*) en lengua española con el corpus lingüístico de `NLTK`.
* Algoritmo de poda de cabeceras y pies de página oficiales para aislar el articulado y la exposición de motivos de la norma.

### 3. Vectorización y Experimentación
* Se compararon diferentes enfoques de representación vectorial de texto:
  * **Bag of N-grams (1-gram y 2-grams):** Estrategia con mayor capacidad de retención de matices de fraseología jurídica y mejor desempeño empírico.
  * Bag of Words convencional.
  * TF-IDF (*Term Frequency - Inverse Document Frequency*).
* Modelos clasificadores: **Regresión Logística multiclase/binomial** con optimización de convergencia (`max_iter=1000`).
* Validación rigurosa mediante división de conjuntos `train_test_split` (80% entrenamiento / 20% test).

### 4. Resultados y Métricas
* **Exactitud global (Accuracy):** **71%** en test sobre iniciativas legales de las legislaturas L11 a L15 del Congreso.
* Evaluación mediante matrices de confusión y `classification_report` (precisión, exhaustividad y F1-score).
* Serialización de modelos y vectorizadores con `joblib` (`.pkl`) para su consumo en entornos de producción o APIs.

---

## 📂 Estructura del Repositorio

* `Modelo Social Y Economico.ipynb`: Cuaderno interactivo con el análisis exploratorio de datos (EDA), preprocesamiento, validación cruzada y entrenamiento de los clasificadores.
* `pipeline.py`: Módulo en Python que encapsula la lógica de limpieza y el pipeline de inferencia NLP reutilizable.
* `requirements.txt`: Dependencias del entorno de ejecución (`pymupdf`, `nltk`, `scikit-learn`, `pandas`, `openpyxl`).

---

## 🚀 Puesta en Marcha en Local

### 1. Clonar el repositorio
```bash
git clone https://github.com/Jezuh05/midemocracia.git
cd midemocracia
```

### 2. Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Ejecutar el pipeline de demostración
```bash
python pipeline.py
```

### 4. Abrir el cuaderno de entrenamiento
```bash
jupyter notebook "Modelo Social Y Economico.ipynb"
```

---

## 📜 Reconocimientos
Proyecto desarrollado dentro del marco formativo del curso de **Inteligencia Artificial con Python** organizado por [Saturdays.AI](https://saturdays.ai/) en la sede de la **Universidad de Alicante** (Marzo - Junio 2024).
