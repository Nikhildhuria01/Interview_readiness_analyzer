from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

questions = pd.read_csv(BASE_DIR / "data/processed/master_question_bank.csv")

print("\nTotal Questions:")
print(len(questions))

print("\nAvailable Roles:")
print(questions["role"].dropna().unique()[:20])
