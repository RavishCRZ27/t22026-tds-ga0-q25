from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 220.23,
    "uptime_pct": 97.675,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 188.36,
    "uptime_pct": 98.196,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 183.87,
    "uptime_pct": 98.04,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 191.19,
    "uptime_pct": 97.248,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 118.28,
    "uptime_pct": 98.827,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 133.49,
    "uptime_pct": 98.183,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 212.55,
    "uptime_pct": 97.997,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 155.65,
    "uptime_pct": 97.657,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 205.7,
    "uptime_pct": 97.204,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 142.1,
    "uptime_pct": 98.478,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 211.8,
    "uptime_pct": 99.15,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 181.09,
    "uptime_pct": 97.579,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 149.96,
    "uptime_pct": 98.677,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 112.88,
    "uptime_pct": 99.11,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 192.76,
    "uptime_pct": 97.769,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 194.2,
    "uptime_pct": 99.456,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 195.89,
    "uptime_pct": 97.498,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 226.25,
    "uptime_pct": 97.797,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 175.95,
    "uptime_pct": 97.56,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 220.73,
    "uptime_pct": 99.341,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 175.32,
    "uptime_pct": 97.793,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 158.21,
    "uptime_pct": 98.078,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 169.42,
    "uptime_pct": 97.467,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 137.24,
    "uptime_pct": 98.728,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 214.18,
    "uptime_pct": 99.001,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 131.52,
    "uptime_pct": 98.314,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 156.37,
    "uptime_pct": 97.501,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 230.35,
    "uptime_pct": 97.822,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 136.26,
    "uptime_pct": 97.434,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 145.15,
    "uptime_pct": 97.327,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 221.23,
    "uptime_pct": 99.243,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 169.04,
    "uptime_pct": 99.461,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 121.19,
    "uptime_pct": 98.671,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 128.51,
    "uptime_pct": 98.178,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 130.88,
    "uptime_pct": 99.314,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 172.45,
    "uptime_pct": 97.709,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
