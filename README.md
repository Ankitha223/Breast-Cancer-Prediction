&#x20;**Breast Cancer Prediction using Machine Learning**



&#x20;**Project Overview**



Breast cancer is one of the most common cancers worldwide, and early detection plays a vital role in improving patient outcomes. This project leverages Machine Learning techniques to classify breast tumors as \*\*Benign\*\* or \*\*Malignant\*\* using the Breast Cancer Wisconsin Dataset.



The project includes data preprocessing, model training, model serialization, and a Python-based prediction interface.





&#x20;**Features**



\- Data preprocessing and cleaning

\- Machine Learning model training

\- High-accuracy tumor classification

\- Saved trained model (`.pkl`)

\- Python-based frontend for predictions

\- Easy-to-use interface



&#x20;**Technologies Used**



\- Python

\- Jupyter Notebook

\- Scikit-learn

\- Pandas

\- NumPy

\- Matplotlib

\- Pickle



&#x20;**Project Structure**





Breast-Cancer-Prediction

│

├── Backend.ipynb                 # Machine Learning model development

├── Frontend.py                   # Prediction interface

├── Breast\_Cancer\_Project.pkl     # Trained ML model

│

├── breast\_cancer.csv

├── breast\_cancer\_unclean.csv

├── wdbc.data

├── wpbc.data

├── breast-cancer-wisconsin.names

│

├── ML report.docx



&#x20;**Machine Learning Model**



\- Algorithm: Decision Tree Classifier

\- Task: Binary Classification

\- Output:

&#x20; - Benign

&#x20; - Malignant

&#x20;**How to Run**



1\. Open \*\*Backend.ipynb\*\* to understand model development and training.

2\. Ensure the trained model (`Breast\_Cancer\_Project.pkl`) is available.

3\. Run the frontend:

python Frontend.py



4\. Enter the required medical parameters.

5\. The application predicts whether the tumor is \*\*Benign\*\* or \*\*Malignant\*\*.



&#x20;**Dataset**



This project uses the \*\*Breast Cancer Wisconsin Dataset\*\*, which contains diagnostic measurements computed from digitized images of breast masses.



&#x20;**Future Improvements**



\- Deploy the model as a web application.

\- Improve prediction accuracy using ensemble learning.

\- Add advanced data visualizations.

\- Develop a modern graphical user interface.

\- Deploy using Flask or Streamlit.



&#x20;**License**



This project is developed for educational purposes.



