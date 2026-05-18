import argparse

def calculate_cpk(purchase_price, import_fees, total_maintenance, personnel_wages, total_fuel, misc_expenses, target_km):
    if target_km == 0:
        raise ZeroDivisionError("Distance cannot be zero.")
    capex = purchase_price + import_fees
    opex = total_maintenance + personnel_wages + total_fuel + misc_expenses
    tco = capex + opex
    return tco / target_km

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--purchase_price", type=float, default=500000.0)
    parser.add_argument("--import_fees", type=float, default=136500.0)
    parser.add_argument("--maintenance", type=float, default=282475.0)
    parser.add_argument("--wages", type=float, default=2160000.0)
    parser.add_argument("--fuel", type=float, default=3600000.0)
    parser.add_argument("--misc", type=float, default=527500.0)
    parser.add_argument("--target_km", type=float, default=480000.0)
    args = parser.parse_args()
    adjusted_purchase = args.purchase_price + 1800000.0
    calculate_cpk(adjusted_purchase, args.import_fees, args.maintenance, args.wages, args.fuel, args.misc, args.target_km)
