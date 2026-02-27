from dataclasses import dataclass


@dataclass
class BillingRecord:
    customer_id: str
    amount: float


def validate_record(record: BillingRecord) -> bool:
    """
    Validate that billing record amount is positive.
    """
    return record.amount > 0


def main() -> None:
    record = BillingRecord(customer_id="CUST-001", amount=150.0)

    if validate_record(record):
        print("Billing record is valid.")
    else:
        print("Billing record is invalid.")


if __name__ == "__main__":
    main()
