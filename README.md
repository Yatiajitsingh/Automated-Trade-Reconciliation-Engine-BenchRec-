The Business Problem
In institutional trading, millions of dollars are transferred daily between internal bank ledgers and external clearinghouses. When a transaction is recorded with mismatched data (e.g., a pricing discrepancy of just $0.01, missing timestamps, or mismatched currencies), the trade fails to settle. These "breaks" freeze capital in limbo and expose the firm to severe regulatory penalties if not resolved by Operations Analysts before the end of the trading day.

The Solution
This engine replaces manual, high-risk Excel reconciliation by systematically ingesting chaotic data, automating perfect matches, and isolating exceptions based on financial exposure.

Built using the official ICAIF 2023 BenchRec dataset (a real-world cash reconciliation dataset released by a Tier-1 financial institution), this Python/Pandas pipeline executes a complete backend settlement workflow:

Data Ingestion & Ledger Splitting: Extracts raw, mixed-schema transactional data and normalizes it into distinct Internal (Pile A) and External (Pile B) ledgers.

Multi-Factor Straight-Through Processing (STP): Executes high-speed inner joins requiring exact, multi-variable matches on Amount, Currency, and Date. This automatically clears clean trades, completely bypassing human intervention.

Exception Management: Systematically isolates trade breaks that fail the STP criteria, preventing mismatched trades from settling.

Risk-Based Prioritization: Quantifies the unsettled financial exposure of every broken trade. The engine generates a prioritized output report, directing human Operations Analysts to resolve million-dollar discrepancies before addressing low-risk breaks.

Tech Stack
Language: Python

Libraries: Pandas (High-volume Data manipulation, ETL, Vectorized Joins)

Data: Tier-1 Bank BenchRec Dataset (Kaggle)
