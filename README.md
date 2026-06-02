# 🎬 Movie Recommender System

A sleek, professional web application that suggests similar movies based on content-filtering algorithms. Built with **Streamlit** for the frontend, **Pandas** for data manipulation, and powered by **The Movie Database (TMDb) API** to fetch high-quality movie posters dynamically.

🚀 **Live Demo:** [Replace with your Render App URL, e.g., https://movie-recommender-system.onrender.com]

---

## ✨ Features
* **Content-Based Filtering:** Analyzes movie tags, genres, and metadata using Cosine Similarity matrices to suggest the closest matches.
* **Modern UI/UX:** Built using Streamlit's structural card components (`st.container` borders) for a beautiful grid-based recommendation interface.
* **Dynamic Poster Fetching:** Connects to the TMDb API in real-time using asynchronous HTTP requests to bring in high-resolution official visual artwork.
* **Responsive Layout:** Automatically scales from large desktop monitors down to mobile viewports.

---

## 📂 Project Structure
```text
MovieRecommenderSystem/
│
├── app.py                # Main Streamlit web application source code
├── requirements.txt      # Python dependencies for production environment
├── movies.pkl            # Pickled DataFrame containing movie metadata and IDs
└── similarity.pkl        # Pickled Cosine Similarity pre-computed matrix