# Assignment 4: LSTM for Stock Price Prediction (GOOGL)

Problem:
Use stacked LSTM(s) to predict next-day `Close` stock price from historical features. Preprocess with MinMaxScaler, create sliding windows, train LSTM, and inverse-transform predictions.

Expected Output:
- Scaled dataset, created sequences (window size e.g., 60)
- Trained LSTM model and predicted vs actual close price plots
- Evaluation metric (MSE) and sample inverse-transformed predictions

## Viva QnA
- Why use MinMaxScaler and fit only on train data?: MinMax scales features to [0,1] improving training stability; fit only on train to avoid data leakage.
- Explain LSTM gates (forget/input/output).: Forget gate drops irrelevant memory, input gate controls new information, output gate controls what is emitted to next layer.
- What is `return_sequences` and when to use it?: `return_sequences=True` returns an output for each timestep (used when stacking LSTMs); `False` returns only final timestep.
- How are sliding windows constructed and why?: Create fixed-length sequences of past `window_size` timesteps to feed LSTM, converting variable history to fixed input shapes.
- How to inverse-transform single-feature predictions using multi-feature scaler?: Repeat the single prediction across feature dims, apply inverse_transform, then extract the target column.
- Limitations of LSTMs for financial data?: Markets are noisy/non-stationary, limited data, and external events not captured; LSTMs can overfit or miss regime shifts.