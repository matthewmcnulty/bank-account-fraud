# [Bank Account Fraud (NeurIPS 2022)](https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips-2022)

The project focuses on the analysis of the Bank Account Fraud Dataset available on Kaggle. The dataset consists of application data from a bank, where fraudulent applications are identified by a binary target variable. The dataset is highly imbalanced, with the majority of the applications being non-fraudulent.

To address the imbalance issue, the SMOTE algorithm is being used to generate synthetic samples for the minority class. Additionally, the project is using grid search cross-validation techniques to optimise hyperparameters and improve model performance.

The project is experimenting with learning ensemble algorithms such as XGBoost and LightGBM to develop a model that can accurately classify fraudulent applications. The performance of the models is being evaluated using precision, recall, F1 score metrics, False Positive Rate (FPR), and Area Under the Receiver Operating Characteristic Curve (AUC). The project aims to keep the FPR to a minimum to ensure that legitimate applications are not falsely flagged as fraudulent, which can cause inconvenience and mistrust among customers.
