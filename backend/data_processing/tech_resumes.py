from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

resume_df = pd.read_csv(
    BASE_DIR / "data/processed/Resume_clean.csv"
)

TECH_CATEGORIES = [
    "INFORMATION-TECHNOLOGY",
    "ENGINEERING"
]

tech_resumes = resume_df[
    resume_df["Category"].isin(TECH_CATEGORIES)
]

print("Original Shape:", resume_df.shape)
print("Tech Shape:", tech_resumes.shape)

tech_resumes.to_csv(
    BASE_DIR / "data/processed/tech_resumes.csv",
    index=False
)

print("Saved tech_resumes.csv")