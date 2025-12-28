from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI running"}

@app.get("/stock/{symbol}")
def get_stock(symbol: str):
    df = yf.download(symbol, period="1y", interval="1d")


    if df.empty:
        return {"error": "Invalid symbol"}

    latest = df.iloc[-1]
    prev = df.iloc[-2]

    change_pct = ((latest["Close"] - prev["Close"]) / prev["Close"]) * 100

    return {
        "symbol": symbol.upper(),
        "latest_close": float(latest["Close"]),
        "prev_close": float(prev["Close"]),
        "change_percent": round(change_pct, 2)
    }

from fastapi.responses import JSONResponse

@app.get("/history/{symbol}")
def get_history(symbol: str):

    print("🔥 HISTORY ENDPOINT CALLED:", symbol)

    df = yf.download(
        symbol,
        period="1y",
        interval="1d",
        auto_adjust=True   # ✅ suppress yfinance warning
    )

    if df.empty:
        return {"error": "Invalid stock symbol"}

    df = df.reset_index()
    df["Date"] = df["Date"].astype(str)

    records = []
    for _, row in df.iterrows():
        records.append({
            "date": row["Date"],
            "open": float(row["Open"].item()),
            "high": float(row["High"].item()),
            "low": float(row["Low"].item()),
            "close": float(row["Close"].item()),
            "volume": int(row["Volume"].item())
        })

    return {
        "symbol": symbol.upper(),
        "count": len(records),
        "records": records
    }
