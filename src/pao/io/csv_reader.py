import csv
from pathlib import Path

from pao.domain.models import BillingRecord


def read_billing_csv(path: Path) -> list[BillingRecord]:
    records: list[BillingRecord] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            customer_id = (row.get("customer_id") or "").strip()
            amount_str = (row.get("amount") or "").strip()
            amount = float(amount_str)  # wir fangen Parsing-Fehler später sauber ab
            records.append(BillingRecord(customer_id=customer_id, amount=amount))
    return records
