from dataclasses import dataclass


@dataclass(frozen=True)
class BillingRecord:
    customer_id: str
    amount: float
