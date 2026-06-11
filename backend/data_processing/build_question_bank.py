from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

# Load datasets
software = pd.read_csv(BASE_DIR / "data/processed/software_questions_clean.csv")

full = pd.read_csv(
    BASE_DIR / "data/processed/full_interview_questions_dataset_clean.csv"
)

# Standardize Software Questions
software = software.rename(
    columns={"Question": "question", "Category": "category", "Difficulty": "difficulty"}
)

software["role"] = "General"

software = software[["question", "role", "category", "difficulty"]]

# Standardize Full Dataset
full = full[["question", "role", "category", "difficulty"]]

# Merge
master = pd.concat([software, full], ignore_index=True)

# Remove duplicate questions
master.drop_duplicates(subset=["question"], inplace=True)

# Save
output = BASE_DIR / "data/processed/master_question_bank.csv"

master.to_csv(output, index=False)

print("Master Question Bank Created")
print(master.shape)
print(master.head())
