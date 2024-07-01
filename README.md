## Bank Loan Approval

### Overview

The Bank Loan Approval project is a machine learning application designed to predict the likelihood of loan approval based on various applicant details. This project aims to assist banks and financial institutions in automating the loan approval process, reducing manual efforts, and minimizing the risk of default by evaluating the creditworthiness of applicants. It takes into account the following parameters to decide on Loan Application Approval:
- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Amount Term
- Credit History

### Features

- **Data Preprocessing:** Cleans and prepares the input data for analysis by handling missing values, encoding categorical variables, and normalizing numerical features.
- **Exploratory Data Analysis (EDA):** Provides insights into the dataset through visualizations and statistical summaries, identifying key trends and patterns.
- **Model Building:** Implements various machine learning algorithms, such as Logistic Regression, Decision Trees, Random Forest, and Gradient Boosting, to predict loan approval status.
- **Model Evaluation:** Assesses the performance of the models using metrics like accuracy, precision, recall, F1-score, and ROC-AUC.
- **Hyperparameter Tuning:** Optimizes model performance through techniques like Grid Search and Random Search.
- **Deployment:** Demonstrates how to deploy the best-performing model using Django for creating a simple web interface for user inputs and predictions.

### Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Django

### Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hiren2599/bankloanapproval.git
   cd bank-loan-approval
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python manage.py runserver
   ```

4. **Access the web interface:**
   Open your web browser and navigate to `http://localhost:8000`.

### Dataset

The dataset used in this project is sourced from the bankloan.csv file attached.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
