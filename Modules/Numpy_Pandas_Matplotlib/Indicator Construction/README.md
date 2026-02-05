# Exercise: Indicator Construction with NumPy, Pandas & Matplotlib
---------------------------------------------------------------

Context:
You are given time-series measurement data from a monitored biological or
biotechnological process. The data contains an underlying trend and natural
fluctuations.

Your task is to construct technical-style indicators commonly used in
scientific monitoring, signal processing, and quantitative analysis.

This exercise focuses on mathematical reasoning, vectorized operations,
and visualization.

--------------------------------------------------
Part 1 — Data loading
--------------------------------------------------

1. Load the provided CSV file into a Pandas DataFrame.
2. Ensure the data is correctly typed (numeric).
3. Inspect the data structure.

--------------------------------------------------
Part 2 — Moving averages
--------------------------------------------------

4. Compute two moving averages:
   - A fast moving average (short window)
   - A slow moving average (long window)

5. Add both moving averages as new columns in the DataFrame.

--------------------------------------------------
Part 3 — Deviation bands
--------------------------------------------------

6. Choose a reference signal (e.g. slow moving average).
7. Compute the standard deviation of the signal.
8. Construct deviation bands:
   - Upper band = mean + k * std
   - Lower band = mean - k * std

9. Add the deviation bands as columns.

--------------------------------------------------
Part 4 — Signal logic
--------------------------------------------------

10. Identify:
    - Points where the fast MA crosses the slow MA
    - Points where values leave the deviation bands

11. Create boolean columns to flag these events.

--------------------------------------------------
Part 5 — Visualization
--------------------------------------------------

12. Create a Matplotlib plot showing:
    - Raw data
    - Fast moving average
    - Slow moving average
    - Deviation bands

13. Highlight detected signal events.

--------------------------------------------------
Goal:
Learn how indicators are constructed from raw data using NumPy and Pandas,
and how mathematical concepts such as smoothing and volatility translate
into visual and analytical signals.

This exercise mirrors real-world workflows in:
- Bioprocess monitoring
- Quality control
- Quantitative signal analysis
