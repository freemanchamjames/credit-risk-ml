from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Config:
    # Project paths
    project_root: Path = Path(__file__).resolve().parents[1]
    data_raw_dir: Path = project_root / "data" / "raw"
    data_processed_dir: Path = project_root / "data" / "processed"
    models_dir: Path = project_root / "models"

    # Dataset file name (keep the CSV local; do not commit it)
    raw_filename: str = "accepted_2007_to_2018q4.csv"

    # Target + split
    target_col: str = "loan_status"
    test_size: float = 0.20
    random_state: int = 42
