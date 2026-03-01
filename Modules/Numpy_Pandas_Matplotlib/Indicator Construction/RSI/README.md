# Exercise 2: Stationary Bioprocess Signal Analysis (RSI + MA)

Context
-------
You are given time-series data from a controlled bioreactor process.
The signal represents a normalized metabolic activity index measured
at fixed time intervals.

The process is assumed to be statistically stationary under normal
operation (mean-reverting behavior around a stable operating point).

However:
- Several transient sensor spikes (outliers) are present.
- Short-term fluctuations occur due to process noise.
- The goal is to detect abnormal excursions and momentum shifts.

The dataset contains 180 data points.

--------------------------------------------------
Part 1 — Data Inspection & Cleaning
--------------------------------------------------

1. Load the dataset into a Pandas DataFrame.
2. Verify stationarity visually and statistically.
3. Identify outliers:
   - Use a statistically defensible method (e.g. z-score or IQR).
   - Explicitly justify your threshold.
4. Create a cleaned version of the signal:
   - Either remove or winsorize outliers.
   - Preserve index alignment.

Deliverable:
- Column: `Value_clean`

--------------------------------------------------
Part 2 — Moving Average
--------------------------------------------------

5. Compute a rolling moving average (window justified).
6. Overlay it on the cleaned signal.
7. Briefly explain:
   - What does the MA represent in a stationary system?

--------------------------------------------------
Part 3 — RSI Implementation (Manual)
--------------------------------------------------

8. Implement the Relative Strength Index (RSI) manually.
   - Do NOT use external technical-analysis libraries.
   - Use vectorized Pandas logic.
   - Properly handle initial undefined region.

9. Justify your RSI window length.
10. Store RSI in a new column.

Deliverable:
- Column: `RSI`

--------------------------------------------------
Part 4 — Signal Logic
--------------------------------------------------

11. Define overbought / oversold conditions.
12. Identify:
    - RSI crossing above oversold threshold.
    - RSI crossing below overbought threshold.

13. Avoid perpetual signals.
    - Detect transitions, not states.

Deliverable:
- Boolean columns for events.

--------------------------------------------------
Part 5 — Visualization (Two-Panel Plot)
--------------------------------------------------

14. Create a Matplotlib figure with two subplots:

    Top panel:
    - Raw signal
    - Cleaned signal
    - Moving average

    Bottom panel:
    - RSI
    - Overbought threshold
    - Oversold threshold

15. Mark RSI signal events visually.

Requirements:
- Clear hierarchy
- No visual clutter
- Scientific style (not trading flashy)

--------------------------------------------------
Learning Objectives
--------------------------------------------------

- Work with stationary data.
- Implement RSI from first principles.
- Handle outliers rigorously.
- Separate indicator panel from main signal.
- Design clear multi-axis visualizations.