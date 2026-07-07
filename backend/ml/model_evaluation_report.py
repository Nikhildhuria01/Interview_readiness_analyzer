from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.units import inch

import math

# ===========================================
# MODEL RESULTS
# ===========================================

import json

with open("ml/model_evaluation.json", "r") as f:

    evaluation = json.load(f)

MODEL_NAME = evaluation["model"]

DATASET_SIZE = evaluation["dataset_size"]

MAE = evaluation["mae"]

MSE = evaluation["mse"]

RMSE = evaluation["rmse"]

R2 = evaluation["r2"]

BEST_PARAMETERS = evaluation["best_parameters"]

# ===========================================
# PDF
# ===========================================

doc = SimpleDocTemplate("Model_Evaluation_Report.pdf")

styles = getSampleStyleSheet()

story = []

# ===========================================
# TITLE
# ===========================================

story.append(
    Paragraph(
        "<b><font size=20>Interview Readiness Analyzer</font></b>", styles["Title"]
    )
)

story.append(Paragraph("<b>Machine Learning Evaluation Report</b>", styles["Heading2"]))

story.append(Spacer(1, 20))

# ===========================================
# MODEL INFO
# ===========================================

story.append(Paragraph(f"<b>Model :</b> {MODEL_NAME}", styles["Normal"]))

story.append(Paragraph(f"<b>Dataset Size :</b> {DATASET_SIZE}", styles["Normal"]))

story.append(Spacer(1, 15))

# ===========================================
# METRICS
# ===========================================

story.append(Paragraph("<b>Evaluation Metrics</b>", styles["Heading2"]))

story.append(Paragraph(f"MAE : {MAE}", styles["Normal"]))

story.append(Paragraph(f"MSE : {MSE}", styles["Normal"]))

story.append(Paragraph(f"RMSE : {RMSE}", styles["Normal"]))

story.append(Paragraph(f"R² Score : {R2}", styles["Normal"]))

story.append(Spacer(1, 15))

# ===========================================
# PARAMETERS
# ===========================================

story.append(Paragraph("<b>Best Hyperparameters</b>", styles["Heading2"]))

for key, value in BEST_PARAMETERS.items():

    story.append(Paragraph(f"{key} : {value}", styles["Normal"]))

story.append(Spacer(1, 20))

# ===========================================
# FEATURE IMPORTANCE
# ===========================================

story.append(Paragraph("<b>Feature Importance</b>", styles["Heading2"]))

story.append(
    Image("ml/feature_importance.png", width=6 * inch, height=4 * inch)
)

story.append(Spacer(1, 20))

# ===========================================
# ACTUAL VS PREDICTED
# ===========================================

story.append(Paragraph("<b>Actual vs Predicted</b>", styles["Heading2"]))

story.append(
    Image("ml/actual_vs_predicted.png", width=6 * inch, height=6 * inch)
)

story.append(Spacer(1, 20))

# ===========================================
# RESIDUAL
# ===========================================

story.append(Paragraph("<b>Residual Plot</b>", styles["Heading2"]))

story.append(Image("ml/residual_plot.png", width=6 * inch, height=4 * inch))

story.append(Spacer(1, 20))

# ===========================================
# INTERPRETATION
# ===========================================

story.append(Paragraph("<b>Model Interpretation</b>", styles["Heading2"]))

story.append(
    Paragraph(
        """
The XGBoost model achieved a strong R² score of approximately 0.86,
indicating that it successfully explains most of the variation in
candidate interview readiness. Feature importance analysis shows that
technical correctness contributes the most to the final prediction,
followed by fluency, eye contact, posture and head stability.

The Actual vs Predicted plot demonstrates good agreement between
predicted and true readiness scores, while the residual plot shows
randomly distributed errors around zero, indicating that the model
does not suffer from systematic prediction bias.

Overall, the trained model is suitable for deployment within the
Interview Readiness Analyzer.
""",
        styles["BodyText"],
    )
)

# ===========================================
# BUILD
# ===========================================

doc.build(story)

print("\nModel Evaluation Report Generated Successfully!")
