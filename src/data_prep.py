from pathlib import Path
import pandas as pd

from src.config import Config


def load_raw(cfg: Config) -> pd.DataFrame:
    """Load raw dataset from data/raw."""
    raw_path = cfg.data_raw_dir / cfg.raw_filename
    if not raw_path.exists():
        raise FileNotFoundError(
            f"Raw data not found at: {raw_path}\n"
            f"Place your CSV in data/raw and set Config.raw_filename accordingly."
        )
    return pd.read_csv(raw_path)


def main() -> None:
    cfg = Config()
    df = load_raw(cfg)

    # Quick sanity prints (we'll refine later)
    print("Shape:", df.shape)
    print("Columns:", len(df.columns))
    print("Top loan_status values (if present):")
    if cfg.target_col in df.columns:
        print(df[cfg.target_col].value_counts().head(20))
    else:
        print(f"Missing target column: {cfg.target_col}")


if __name__ == "__main__":
    main()
