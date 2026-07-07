import joblib
import matplotlib.pyplot as plt

# ==============================
# LOAD MODEL
# ==============================

model = joblib.load(
    "ml/readiness_model.pkl"
)

# ==============================
# FEATURES
# ==============================

features = [

    "Fluency",

    "Correctness",

    "Eye Contact",

    "Posture",

    "Head Stability"

]

importance = model.feature_importances_

# ==============================
# SORT
# ==============================

pairs = sorted(

    zip(features, importance),

    key=lambda x: x[1],

    reverse=True

)

features = [x[0] for x in pairs]

importance = [x[1] for x in pairs]

# ==============================
# PLOT
# ==============================

plt.figure(figsize=(8,5))

plt.bar(

    features,

    importance

)

plt.title(

    "Feature Importance"

)

plt.xlabel(

    "Interview Features"

)

plt.ylabel(

    "Importance Score"

)

plt.tight_layout()

plt.savefig(

    "ml/feature_importance.png",

    dpi=300

)

plt.show()

print("\nFeature Importance Graph Saved!")