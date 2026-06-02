# 🎬 Movie Recommender System

A high-performance, professional content-based movie recommendation web application. The system leverages machine learning vector math to analyze movie metadata, processing features like genres, keywords, cast, and crew. It pairs a clean **Streamlit** user interface with real-time **The Movie Database (TMDb) API** integrations to deliver an immersive, data-driven user experience complete with dynamic artwork.

---

## 🚀 Architectural Overview

The application utilizes a decoupling pattern separating data preparation (offline) from the user interface presentation (online):

1. **The Machine Learning Pipeline (Offline):** Movie features are preprocessed, tokens are vectorized using Bag-of-Words or TF-IDF, and a Cosine Similarity matrix is calculated. This data is serialized into compressed pickle (`.pkl`) files.
2. **The Presentation Layer (Online):** Streamlit reads the spatial vectors, targets the user selection index, extracts top-performing neighbors, and constructs contextual card wrappers.
3. **The Enrichment Layer (Asynchronous API):** The app maps internal dataset IDs to official TMDb global IDs, pulling high-resolution graphic assets securely over HTTPS.

---

## ✨ Features

* **Content-Based Filtering:** Employs high-dimensional spatial distance calculation (Cosine Similarity) to find semantic relationships between films.
* **Modern Interface Cards:** Built using unified modular component blocks (`st.container` borders) creating a distinct, elegant dashboard layout.
* **Smart Exception Handling:** Features a robust API fallback script. If an API timeout occurs or a movie lacks an official poster, a dynamic placeholder card is rendered automatically to prevent UI breakages.
* **Search-As-You-Type Dropdown:** Incorporates optimized internal indexing to allow quick, reactive filtering through thousands of film titles instantly.
* **Asynchronous UX Design:** Uses progress spinners (`st.spinner`) during computation to ensure a fluid application state flow.

---

## 📂 Detailed Project Structure

```text
MovieRecommenderSystem/
│
├── app.py                # Core production script containing UI and API connections
├── requirements.txt      # Production library dependencies with pinned components
├── movies.pkl            # Serialized Pandas DataFrame holding processed metadata and IDs
└── similarity.pkl        # Serialized 2D NumPy array containing pre-computed similarity scores