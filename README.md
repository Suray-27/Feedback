# **🤖 Comprehensive Sentiment Analysis and AI-Powered Response System**

![AI-Driven Feedback System](https://via.placeholder.com/800x300?text=AI+Feedback+System)

## **🔬 Project Overview**
This project revolutionizes customer feedback management by integrating AI, machine learning, and cloud-based solutions. Built on the "Ola Sentiment Reviews" dataset, the system predicts customer sentiments (Positive, Neutral, Negative), generates polite AI-driven responses, and automates personalized email follow-ups for neutral and negative feedback. It provides seamless real-time interaction via a Streamlit web interface and stores feedback and model artifacts in MongoDB for efficient data management.

---

## 🎯 Scope and Objectives
### Scope
- Analyze customer reviews to extract actionable insights.
- Predict sentiments (Positive, Neutral, Negative) using ML models.
- Provide polite AI-generated responses for customer feedback.
- Build a database to store customer interactions and feedback history.
- Automate email responses for negative/neutral sentiments.
- Deploy a user-friendly web interface using Streamlit.

### Objectives
1. Conduct Exploratory Data Analysis (EDA) to uncover trends and patterns.
2. Develop a preprocessing pipeline to clean and prepare text data.
3. Train and deploy a logistic regression model for sentiment classification.
4. Store and manage data efficiently using MongoDB.
5. Automate personalized responses using AI and Gemini API.
6. Create an interactive dashboard for seamless user interactions.

---


## **🔄 Workflow**
1. **Data Collection:** Load and preprocess data (`EDA.py`, `pre_process.py`).
2. **Model Training:** Train logistic regression model for sentiment analysis (`sentiment_model.ipynb`).
3. **Database Setup:** Create and manage MongoDB databases (`Mongo_DB.py`).
4. **AI Response:** Implement automated responses using Gemini API (`ai_response.py`).
5. **Email Automation:** Send emails for specific sentiments (`email_utils.py`).
6. **Web Deployment:** Deploy a user-friendly interface (`app.py`).

---

## 📊 Exploratory Data Analysis (EDA)
**File:** `EDA.py`
### 🔍 Insights
- **Trend Analysis by Year:** Significant increase in reviews starting from 2017, peaking in 2019.
- **Monthly Trends:** Gradual rise from January to March, with peaks in August.
- **Hourly Trends:** High activity during 4–6 AM and 12–2 PM.
- **App Version Analysis:** Weak negative correlation between `appVersion` and `rating`. Older versions received higher ratings.
- **Developer Responses:** Ratings with developer responses were statistically different.

---

## 🧹 Preprocessing Pipeline
**File:** `pre_process.py`
### 🛠️ Tools and Libraries
- **Libraries:** `nltk`, `textblob`, `emoji`, `re`
- **Key Features:**
  - Removed stopwords using `nltk`.
  - Included emoji analysis for modern conversational relevance.
  - Addressed classification biases, e.g., competitor appraisals marked as negative.
  - Tokenization, lemmatization, and cleaning of text data.

---

### **🌐 Sentiment Analysis and Model Building**

**File:** `sentiment_model.ipynb`
### ⚙️ Methodology
- **Data:** Processed from `review_description` and `rating` columns.
- **Tools:** `TfidfVectorizer`, `StandardScaler`, `hstack`
- **Model:** Logistic Regression
- **Outputs:** Sentiments - Positive, Neutral, Negative
- **Saved Models:**
  - Logistic Regression Model
  - `TfidfVectorizer`
  - `StandardScaler`

---

## 📨 Automated Email System
**File:** `email_utils.py`
### ✉️ Features
- **Libraries:** `smtplib`, `email`
- **Functionality:**
  - Sends personalized emails to customers with negative or neutral feedback.
  - Offers discounts (15% for negative, 5% for neutral).

---

## 🗄️ Database Management
**File:** `Mongo_DB.py`
### 🛢️ Implementation
- **Database:** MongoDB (cloud-based)
- **Libraries:** `pymongo`, `joblib`, `io`
- **Data Stored:**
  - Customer email ID, feedback, sentiment, model response, timestamp.
  - `LogisticRegression`, `TfidfVectorizer`, `StandardScaler` for predictions.

---

## 💬 AI Response System
**File:** `ai_response.py`
### 🤖 Features
- **API:** Gemini API
- **Functionality:**
  - Generates polite, context-aware responses based on customer feedback.
  - Enhances customer experience by addressing their concerns.

---

## 🌐 Streamlit Application
**File:** `app.py`
### 🖥️ Features
- **Front-End:**
  - Interactive interface to submit and analyze feedback.
  - Real-time sentiment prediction and AI responses.
- **Back-End:**
  - Stores user feedback and system responses in MongoDB.
  - Facilitates interaction between the user and the logistic model.

---

## 📈 Visual Summary
- **Yearly Review Trends:** 📅 📊
- **Rating Distribution:** ⭐📊
- **App Version Analysis:** 📲 📊

---

## **🔧 Technologies Used**
| **Component**         | **Technologies**               |
|-----------------------|--------------------------------|
| Data Analysis         | Pandas, NumPy, Matplotlib, Seaborn, Scipy, Warnings |
| Text Preprocessing    | NLTK, TextBlob, Emoji, re      |
| Sentiment Prediction  | Scikit-learn, TfidfVectorizer, StandardScaler |
| AI Response           | Gemini API                     |
| Database Management   | MongoDB, PyMongo               |
| Email Automation      | smtplib, email library         |
| Web Interface         | Streamlit                      |

---

## **🔍 How to Use**
1. **Set Up Environment**:
   - Install dependencies: `pip install -r requirements.txt`
   - Configure MongoDB credentials in `.env` file.

2. **Run the Web App**:
   - Navigate to the project directory.
   - Execute: `streamlit run app.py`

3. **Explore Features**:
   - Submit feedback through the web interface.
   - View AI-generated responses and sentiment predictions.
   - Check email notifications for neutral/negative feedback.

---

## 🚀 Future Scope
- Enhance NLP models for multi-language support.
- Implement advanced machine learning models for better sentiment prediction.
- Add real-time data visualization in the Streamlit dashboard.
