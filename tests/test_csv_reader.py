from pathlib import Path
from pao.io.csv_reader import read_billing_csv

def test_read_billing_csv(tmp_path: Path):
    p = tmp_path / "billing.csv"
    p.write_text("customer_id,amount\nC1,10\nC2,20\n", encoding="utf-8")

    records = read_billing_csv(p)
    assert len(records) == 2
    assert records[0].customer_id == "C1"
    assert records[0].amount == 10.0