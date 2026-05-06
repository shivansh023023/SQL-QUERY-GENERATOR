You can access the website at - https://sql-query-generator-lcmmrl3rurizsup225bez2.streamlit.app/

```markdown
# 📊 SQL Query Generator

A simple yet powerful web application that generates SQL queries from plain English prompts using **Google's Gemini Pro Model**. This tool also provides explanations and sample outputs for the generated SQL queries.

##  Features

- ✅ Convert natural language to SQL queries
- ✅ Get **sample outputs** for your SQL queries
- ✅ Simple and easy-to-understand **query explanations**
- ✅ Interactive UI built with **Streamlit**

## 🛠️ Technologies Used:

- **Python** - Core programming language
- **Streamlit** - For building the interactive web app
- **Google Generative AI (Gemini Pro)** - For generating SQL queries and explanations
- **HTML & Markdown** - Used within Streamlit for UI styling
- **SQL** - Generated as output queries

## 📦 Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/sql-query-generator.git
   cd sql-query-generator
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Google API Key:**
   - Get your API key from [Google Cloud Console](https://console.cloud.google.com/).
   - Replace the placeholder in the code with your API key:
     ```python
     GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
     ```

5. **Run the App:**
   ```bash
   streamlit run app.py
   ```

## 💡 Usage

1. Enter your request in plain English (e.g., "Get all employees who joined after 2020").
2. Click on **"Generate SQL Query"**.
3. The app will display:
   - ✅ The SQL Query
   - 📊 A sample output table
   - 📝 A simple explanation of the query

## 📷 Screenshots

*(Add screenshots of your app here)*

## 📝 Example

**Input:**
```
Show me the top 5 customers with the highest purchases in 2023.
```

**Generated SQL:**
```sql
SELECT customer_name, SUM(purchase_amount) AS total_purchases
FROM sales
WHERE YEAR(purchase_date) = 2023
GROUP BY customer_name
ORDER BY total_purchases DESC
LIMIT 5;
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 🙌 Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://cloud.google.com/vertex-ai)
- [SQL Documentation](https://www.sqltutorial.org/)

---

⭐ *If you found this project helpful, feel free to star the repository!* ⭐
```

