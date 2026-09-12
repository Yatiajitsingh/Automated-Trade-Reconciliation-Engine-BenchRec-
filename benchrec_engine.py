import pandas as pd

print("Booting up BenchRec Reconciliation Engine...")

# 1. THE SETUP
# This reads that gibberish you pasted and turns it into a clean table.
# (Make sure your file is extracted from its ZIP folder and named exactly this)
raw_data = pd.read_csv("BenchRec_cash_v1.0_eval.csv", low_memory=False)

# 2. THE SPLIT
# We create Pile A (Internal Ledger) using the 'A_' columns
# We use .dropna() to remove any blank empty rows
ledger_A = raw_data[['A_id', 'A_amount', 'A_valueDate','A_currencyCode']].copy().dropna()

# We create Pile B (External Ledger) using the 'B_' columns
ledger_B = raw_data[['B_id', 'B_amount', 'B_valueDate','B_currencyCode']].copy().dropna()

# 3. STRAIGHT-THROUGH PROCESSING (STP)
# The Magic Match. We tell Python to glue them together ONLY if the money matches perfectly.
clean_matches = pd.merge(
    ledger_A, 
    ledger_B, 
    left_on='A_amount',   # Look at the money in Pile A
    right_on='B_amount',  # Match it to the money in Pile B
    how='inner'           # Only keep perfect matches
)

print(f"SUCCESS: {len(clean_matches)} trades automatically matched and cleared.")

# 4. EXCEPTION MANAGEMENT
# Find the trades in Pile A whose IDs are NOT inside our clean 'Done' bin.
# The '~' symbol means "NOT".
broken_trades = ledger_A[~ledger_A['A_id'].isin(clean_matches['A_id'])].copy()

# 5. RISK SCORING
# Sort the broken trades so the biggest dollar amounts are at the top.
# We use .abs() (absolute value) just in case a huge trade is recorded as a negative number.
broken_trades['Risk_Exposure'] = broken_trades['A_amount'].abs()
prioritized_breaks = broken_trades.sort_values(by='Risk_Exposure', ascending=False)

print(f"WARNING: {len(prioritized_breaks)} broken trades detected.")

# 6. EXPORT
# Save the prioritized list to a brand new Excel-ready file for the human to read.
prioritized_breaks.to_csv("URGENT_TRADE_BREAKS.csv", index=False)
print("Engine Complete. Open 'URGENT_TRADE_BREAKS.csv' to see what needs fixing first.")
