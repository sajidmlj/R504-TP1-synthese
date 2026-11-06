def debit_mbps(octets: int, secondes: float) -> float:
    return octets * 8 / 1_000_000 / secondes
