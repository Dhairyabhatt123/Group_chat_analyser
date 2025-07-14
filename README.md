demo link : https://group-chat-analyser-1.onrender.com



---

### 💬 `README.md` for **WhatsApp Group Chat Analyzer**

```markdown
# 💬 WhatsApp Group Chat Analyzer 📊

This project analyzes a **WhatsApp group chat export** and visualizes various statistics, summaries, and behavior patterns. It’s a fun tool to explore group activity, top contributors, emoji usage, and more — all in one clean dashboard.

---

## 🎯 Objective

To take a `.txt` file exported from WhatsApp and turn it into an insightful, interactive summary using **data science and visualization tools**.

---

## 📂 Features

- 📈 **Daily, monthly, and weekly timelines**
- 📊 **Most active members**
- 🔤 **Most common words**
- 😂 **Emoji usage analysis**
- 📸 **Media/shared file counts**
- 🔗 **Links & message counts**
- 🕵️‍♂️ Full participant-level filtering
- 🎨 Beautiful graphs with `matplotlib` and `seaborn`

---

## 🧰 Tech Stack

- `pandas`, `numpy`
- `matplotlib`, `seaborn`, `wordcloud`
- `re` for regex text parsing
- `urlextract` to fetch links
- `Streamlit` for interactive UI

---

## 🚀 How to Use

1. Export your WhatsApp group chat (without media)
2. Place the `.txt` file in the project folder
3. Run the app:

```bash
streamlit run app.py
