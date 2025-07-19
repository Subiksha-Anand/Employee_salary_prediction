👩‍💼 Employee Salary Prediction
This is a machine learning web application that predicts the salary of an employee based on features such as experience, education, job role, and location. The app uses a trained LightGBM model and is built with Streamlit for interactive UI.

🚀 Demo
🖥️ Live App: https://employeesalaryprediction-vq5rdj5lirhmkbcnizkfcr.streamlit.app/

📌 Features
📊 Predicts employee salary based on input features

⚡ Powered by LightGBM (Gradient Boosting)

📈 User-friendly interface via Streamlit

📁 Supports structured data input

💾 Option to retrain or improve model further

🧠 Model
The model is trained using:

LightGBM as the regression model

Cleaned and preprocessed HR dataset

Feature engineering for categorical variables

Model is saved using joblib and loaded in the Streamlit app.

🛠️ Tech Stack
Python 3.10

LightGBM

Streamlit

Pandas, NumPy, SciPy

Joblib

▶️ Run Locally
bash
Copy
Edit
git clone https://github.com/your-username/employee_salary_prediction.git
cd employee_salary_prediction
pip install -r requirements.txt
streamlit run app.py
📈 Future Improvements
Add more features like company tier, location cost of living, etc.

Support model retraining from user-uploaded CSVs

Track prediction logs for analytics

🧑‍💻 Author
Subiksha Anand
💼 Aspiring Data Scientist
📫 https://www.linkedin.com/in/subiksha-anand-38591a2a2/

