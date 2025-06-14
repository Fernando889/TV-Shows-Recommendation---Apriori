# 📺 TV Show Recommendation System using Apriori

This project implements a simple Market Basket Analysis for TV shows using the **Apriori algorithm**. It analyzes a dataset of TV shows that users have watched and generates association rules to recommend TV shows that are often watched together.

---

## 📂 Dataset

- The dataset `tv_shows.csv` should contain user watch histories in a transaction-like format:
  - Each row represents one user's watched shows.
  - Each column in a row is a TV show the user watched.
  - Example:
    ```
    Breaking Bad, Game of Thrones, Vikings
    The Wire, Breaking Bad
    ...
    ```

---

## 🚀 How it works

1. **Load data:**  
   The script reads the CSV file with no header.

2. **Preprocess data:**  
   Each row is converted to a list of shows, creating a list of transactions.

3. **Apply Apriori:**  
   Using `apyori`, it finds frequent itemsets and generates association rules based on:

   - Minimum support: `0.003`
   - Minimum confidence: `0.2`
   - Minimum lift: `3`
   - Rule length: `2` (pairs only)

4. **Display results:**  
   The top 10 strongest rules (by Lift) are displayed in a DataFrame.

---

## 📊 Example output

| Left Hand Side     | Right Hand Side | Supports | Confidence | Lift      |
| ------------------ | --------------- | -------- | ---------- | --------- |
| Fringe             | Lost            | 0.003096 | 0.379747   | 11.392405 |
| Game of Thrones    | Vikings         | 0.004850 | 0.279762   | 8.290192  |
| The 100            | Dark            | 0.004644 | 0.416667   | 4.673032  |
| Person of Interest | Mr. Robot       | 0.006914 | 0.429487   | 3.926161  |
| Rick And Morty     | Family Guy      | 0.009185 | 0.276398   | 3.864779  |
| ...                | ...             | ...      | ...        | ...       |

---

## 📌 Requirements

- Python 3.11.9
- Libraries:
  - `numpy`
  - `pandas`
  - `apyori`

Install dependencies:

```bash
pip install numpy pandas apyori
```

---

## 📑 Usage

1. Place your `tv_shows.csv` in the same directory as the script.
2. Run the Python script:
   ```bash
   python tv_show_recommender.py
   ```
3. Check the console for the top recommended TV show pairs!

---

## ⚡️ Notes

- You can tune `min_support`, `min_confidence`, `min_lift`, and `min_length` to discover more or fewer associations.
- This method can be adapted for any item-based recommendation system (movies, books, products, etc.).

---

## 📖 References

- [Apriori algorithm](https://en.wikipedia.org/wiki/Apriori_algorithm)
- [apyori Python library](https://pypi.org/project/apyori/)
- This project is for educational purposes and also as portfolio. I got the tv_shows.csv file from Kaggle

---

✅ **Happy Recommending!**
