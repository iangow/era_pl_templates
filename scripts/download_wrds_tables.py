from dotenv import load_dotenv
from db2pq import wrds_update_pq


def main() -> None:
    load_dotenv()

    tables = [
        ("ccmxpf_lnkhist", "crsp", {"col_types": {"lpermno": "int32", "lpermco": "int32"}}),
        ("stocknames", "crsp", {}),
        ("dsi", "crsp", {}),
        ("comphist", "crsp", {}),
        ("dsedelist", "crsp", {}),
        ("dseexchdates", "crsp", {}),
        ("dsedist", "crsp", {}),
        ("msi", "crsp", {}),
        ("mse", "crsp", {}),
        ("msf", "crsp", {}),
        ("erdport1", "crsp", {}),
        ("dsf", "crsp", {}),
        ("factors_daily", "ff", {}),
        ("company", "comp", {}),
        ("funda", "comp", {}),
        ("funda_fncd", "comp", {}),
        ("fundq", "comp", {}),
        ("r_auditors", "comp", {}),
        ("idx_daily", "comp", {}),
        ("aco_pnfnda", "comp", {}),
        ("seg_customer", "compseg", {}),
        ("names_seg", "compseg", {}),
    ]

    for table, library, kwargs in tables:
        wrds_update_pq(table, library, **kwargs)


if __name__ == "__main__":
    main()
