import tkinter as tk
from tkinter import ttk
import numpy as np
import pickle

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("Breast_Cancer_Project.pkl", "rb"))

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Breast Cancer Prediction System")
root.geometry("750x950")
root.configure(bg="#EAF6F6")

# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="Breast Cancer Prediction System",
    font=("Helvetica", 24, "bold"),
    bg="#EAF6F6",
    fg="#1B4965"
)
title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Machine Learning using Decision Tree Classifier",
    font=("Arial", 12),
    bg="#EAF6F6",
    fg="#555555"
)
subtitle.pack()

# ---------------- MAIN FRAME ----------------
frame = tk.Frame(
    root,
    bg="white",
    bd=3,
    relief=tk.RIDGE
)

frame.pack(
    padx=30,
    pady=20,
    fill="both",
    expand=True
)

# ---------------- FEATURES ----------------
features = [
    "Clump Thickness",
    "Uniformity Cell Size",
    "Uniformity Cell Shape",
    "Marginal Adhesion",
    "Single Epithelial Cell Size",
    "Bare Nuclei",
    "Bland Chromatin",
    "Normal Nucleoli",
    "Mitoses"
]

dropdowns = []

# Values from 1 to 10
values = ["Select",1,2,3,4,5,6,7,8,9,10]

# ---------------- CREATE DROPDOWNS ----------------
for feature in features:

    label = tk.Label(
        frame,
        text=feature,
        font=("Arial", 11, "bold"),
        bg="white",
        anchor="w"
    )

    label.pack(
        fill="x",
        padx=20,
        pady=(6, 0)
    )

    combo = ttk.Combobox(
        frame,
        values=values,
        font=("Arial", 11),
        state="readonly"
    )

    combo.pack(
        fill="x",
        padx=20,
        pady=2
    )

    combo.current(0)

    dropdowns.append(combo)

# ---------------- RESULT LABEL ----------------
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 18, "bold"),
    bg="#EAF6F6"
)

result_label.pack(pady=10)

# ---------------- PREDICTION FUNCTION ----------------
def predict():

    values = [float(combo.get()) for combo in dropdowns]

    data = np.array([values])

    prediction = model.predict(data)

    if prediction[0] == 0:

        result_label.config(
            text="Prediction Result: BENIGN",
            fg="green"
        )

    else:

        result_label.config(
            text="Prediction Result: MALIGNANT",
            fg="red"
        )

# ---------------- CLEAR FUNCTION ----------------
def clear():

    for combo in dropdowns:
        combo.current(0)

    result_label.config(text="")

# ---------------- BUTTON FRAME ----------------
button_frame = tk.Frame(
    root,
    bg="#EAF6F6"
)

button_frame.pack(pady=20)

# ---------------- PREDICT BUTTON ----------------
predict_btn = tk.Button(
    button_frame,
    text="Predict",
    command=predict,
    font=("Arial", 12, "bold"),
    bg="#1B4965",
    fg="white",
    width=15,
    height=2,
    cursor="hand2"
)

predict_btn.grid(
    row=0,
    column=0,
    padx=20
)

# ---------------- CLEAR BUTTON ----------------
clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear,
    font=("Arial", 12, "bold"),
    bg="#5FA8D3",
    fg="white",
    width=15,
    height=2,
    cursor="hand2"
)

clear_btn.grid(
    row=0,
    column=1,
    padx=20
)

# ---------------- FOOTER ----------------
footer = tk.Label(
    root,
    text="Developed using Python, Tkinter and Decision Tree Classifier",
    font=("Arial", 10),
    bg="#EAF6F6",
    fg="gray"
)

footer.pack(
    side="bottom",
    pady=10
)

# ---------------- RUN APPLICATION ----------------
root.mainloop()