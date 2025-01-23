
# 🎬 Movie Recommendation System 🎥

A sleek and user-friendly **Movie Recommendation System** built using **Python** and **Streamlit**. Select a genre, and the app will recommend similar movies based on that genre, with their posters fetched dynamically from the **TMDb API**.

## 🚀 Features
- **Genre-Based Recommendations**: Get movie suggestions based on your selected genre.
- **Dynamic Posters**: Movie posters are fetched dynamically from the TMDb API.
- **Modern UI**: Clean, interactive, and modern user interface for seamless interaction.

## 🛠️ Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: [Python](https://www.python.org/)
- **Database**: Precomputed similarity matrix (Pickle)
- **API**: [TMDb API](https://www.themoviedb.org/documentation/api) for fetching movie posters

## 🎬 How It Works
1. **Select a Genre**: Choose your favorite movie genre from the dropdown menu.
2. **Get Recommendations**: Click the "Show Recommendation" button to receive a list of similar movies within the selected genre.
3. **View Posters**: See movie titles paired with their posters displayed side-by-side for easy viewing.

## 🛑 Prerequisites
Before running the app, ensure you have the following:
- Python **3.7+**
- **TMDb API Key** (stored in the `.env` file)

## 📦 Installation

Follow these steps to get your project up and running:

### 1. Clone the Repository
```bash
git clone https://github.com/LohithReddyy/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Create a Virtual Environment
For **Linux/Mac**:
```bash
python -m venv venv
source venv/bin/activate
```
For **Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add TMDb API Key
Create a `.env` file in the root directory and add your **TMDb API key**:
```plaintext
API_KEY=your_tmdb_api_key
```

### 5. Run the App
```bash
streamlit run app.py
```

## 🌐 Deployment

Want to deploy your app? You can deploy it with ease using [Streamlit Community Cloud](https://share.streamlit.io/). Check out the [Deployment Guide](https://docs.streamlit.io/streamlit-community-cloud) for detailed instructions.

---

### 🌟 Enjoyed the app? ⭐

If you found this project helpful, don't forget to **star the repository**! 🌟

