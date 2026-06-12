from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

df = pd.read_csv(
    BASE_DIR / "data/processed/tech_resumes.csv"
)

print(df.iloc[0]["Category"])

print("\nResume Preview:\n")

print(df.iloc[0]["Resume_str"][:2000])