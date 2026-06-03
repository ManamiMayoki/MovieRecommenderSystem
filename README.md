# 🎬 Movie Recommender System

> A high-performance, content-based movie recommendation engine powered by machine learning and enriched with live TMDb data.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![TMDb API](https://img.shields.io/badge/TMDb-API-01D277?style=flat-square&logo=themoviedatabase&logoColor=white)](https://www.themoviedatabase.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Dependencies](#-dependencies)
- [License](#-license)

---

## 🧠 Overview

The **Movie Recommender System** is a full-stack data science application that delivers personalized movie suggestions using **content-based collaborative filtering**. It analyzes semantic relationships between films by processing structured metadata — genres, keywords, cast, and crew — and computes high-dimensional cosine similarity scores to surface the most relevant recommendations.

The application pairs a clean, reactive **Streamlit** frontend with real-time **The Movie Database (TMDb) API** integration to render dynamic poster artwork and enrich each recommendation card with live data.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Content-Based Filtering** | Cosine similarity over TF-IDF / Bag-of-Words vectors for semantic film matching |
| **Live TMDb Enrichment** | Maps internal dataset IDs to TMDb global IDs, fetching high-resolution poster assets over HTTPS |
| **Modern Card UI** | Modular `st.container` border components for a clean, dashboard-style layout |
| **Search-As-You-Type** | Optimized internal indexing for instant reactive filtering across thousands of titles |
| **Robust Fallback Handling** | Graceful degradation on API timeouts or missing posters — renders a placeholder card automatically |
| **Async UX** | `st.spinner` progress states ensure a fluid, non-blocking user experience during computation |

---

## 🏗 Architecture

The system follows a **decoupled offline/online** design pattern, separating the computationally expensive ML pipeline from the lightweight presentation layer.

```
┌─────────────────────────────────────────────────────────┐
│                  OFFLINE: ML PIPELINE                   │
│                                                         │
│  Raw Metadata → Feature Engineering → Vectorization     │
│       → Cosine Similarity Matrix → Serialization (.pkl) │
└──────────────────────────┬──────────────────────────────┘
                           │  movies.pkl / similarity.pkl
┌──────────────────────────▼──────────────────────────────┐
│               ONLINE: STREAMLIT APP (app.py)            │
│                                                         │
│  Load Vectors → User Selection → Nearest Neighbor Query │
│              → Render Recommendation Cards              │
└──────────────────────────┬──────────────────────────────┘
                           │  TMDb Movie IDs
┌──────────────────────────▼──────────────────────────────┐
│            ENRICHMENT: TMDb API (Async)                 │
│                                                         │
│  ID Mapping → HTTPS Poster Fetch → Dynamic Card Render  │
└─────────────────────────────────────────────────────────┘
```

**Pipeline stages:**

1. **ML Pipeline (Offline)** — Movie features are preprocessed, tokenized, and vectorized using Bag-of-Words or TF-IDF. A full Cosine Similarity matrix is computed and serialized into compressed `.pkl` files for fast startup.

2. **Presentation Layer (Online)** — Streamlit deserializes the precomputed vectors, resolves the user-selected movie's index, and extracts the top-N nearest neighbors from the similarity matrix.

3. **Enrichment Layer (Asynchronous)** — Internal dataset IDs are mapped to official TMDb global IDs. High-resolution poster artwork is fetched securely over HTTPS and rendered into each recommendation card.

---

## 📂 Project Structure

```text
MovieRecommenderSystem/
│
├── app.py                # Core Streamlit application — UI, API calls, recommendation logic
├── requirements.txt      # Pinned production dependencies
├── movies.pkl            # Serialized Pandas DataFrame: processed metadata + TMDb IDs
└── similarity.pkl        # Serialized 2D NumPy array: precomputed cosine similarity scores
```

| File | Purpose |
|---|---|
| `app.py` | Entry point. Loads pickled artifacts, renders the Streamlit interface, queries the TMDb API, and handles fallback logic. |
| `requirements.txt` | All Python dependencies with pinned versions for reproducible deployments. |
| `movies.pkl` | Preprocessed movie metadata (title, genres, keywords, cast, crew, TMDb ID) serialized for fast I/O. |
| `similarity.pkl` | The N×N cosine similarity matrix. Each cell `[i][j]` holds the similarity score between movie `i` and movie `j`. |

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8** or higher
- A valid **TMDb API key** — obtain one free at [themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/MovieRecommenderSystem.git
cd MovieRecommenderSystem
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure your TMDb API key** *(see [Configuration](#-configuration))*

**5. Launch the application**

```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## ⚙️ Configuration

Set your TMDb API key as an environment variable before running the app:

```bash
# macOS / Linux
export TMDB_API_KEY="your_api_key_here"

# Windows (Command Prompt)
set TMDB_API_KEY=your_api_key_here

# Windows (PowerShell)
$env:TMDB_API_KEY="your_api_key_here"
```

Alternatively, for **Streamlit Cloud** deployments, add the key to `.streamlit/secrets.toml`:

```toml
TMDB_API_KEY = "your_api_key_here"
```

---

## 🎯 Usage

1. Open the app at `http://localhost:8501`.
2. Use the **search dropdown** to select a movie title from the dataset.
3. Click **"Get Recommendations"**.
4. Browse the **recommendation cards** — each displays the movie poster, title, and metadata fetched live from TMDb.

> **Note:** If a poster is unavailable or the API request times out, a styled placeholder card is rendered automatically so the UI never breaks.

---

## 🔬 How It Works

### Feature Engineering

Raw movie metadata fields (genres, keywords, cast, crew) are tokenized, lowercased, and concatenated into a single feature string called a **"tag"** per movie.

### Vectorization

Tags are vectorized using either **Bag-of-Words** (CountVectorizer) or **TF-IDF** (TfidfVectorizer), producing a sparse high-dimensional matrix where each dimension represents a unique token.

### Similarity Computation

**Cosine Similarity** is computed pairwise across all movie vectors:

$$\text{similarity}(A, B) = \frac{A \cdot B}{\|A\| \cdot \|B\|}$$

A score of `1.0` indicates identical feature profiles; `0.0` indicates no overlap.

### Recommendation Retrieval

Given a user-selected movie at index `i`, the app retrieves row `i` from the similarity matrix, sorts by descending score, and returns the top-N results (excluding the query movie itself).

---

## 📦 Dependencies

| Library | Purpose |
|---|---|
| `streamlit` | Web application framework and UI components |
| `pandas` | DataFrame operations and metadata management |
| `numpy` | Numerical operations on the similarity matrix |
| `scikit-learn` | Vectorization (CountVectorizer / TfidfVectorizer) and cosine similarity |
| `requests` | HTTP client for TMDb API calls |
| `pickle` | Serialization and deserialization of ML artifacts |

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built with ❤️ using Python, Streamlit, and The Movie Database API
</p>