import asyncio
from typing import List

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.responses import EventSourceResponse

app = FastAPI()


clients: List[asyncio.Queue] = []


async def event_generator(q: asyncio.Queue):
    try:
        while True:
            data = await q.get()
            yield f"data: {data}\n\n"
    except asyncio.CancelledError:
        return


@app.get("/sse")
async def sse_endpoint(request: Request):
    q: asyncio.Queue = asyncio.Queue()
    clients.append(q)

    async def generator():
        try:
            while True:
                
                if await request.is_disconnected():
                    break
                try:
                    data = await asyncio.wait_for(q.get(), timeout=15.0)
                    yield f"data: {data}\n\n"
                except asyncio.TimeoutError:
                    
                    yield ": ping\n\n"
        finally:
            try:
                clients.remove(q)
            except ValueError:
                pass

    return EventSourceResponse(generator())


@app.post("/publish")
async def publish(request: Request):
    """Accept JSON body and broadcast its JSON string to all connected SSE clients."""
    try:
        payload = await request.json()
    except Exception:
        return JSONResponse({"error": "invalid json"}, status_code=400)

    
    text = str(payload)
    for q in list(clients):
        
        try:
            q.put_nowait(text)
        except Exception:
            pass

    return {"status": "ok", "clients": len(clients)}


@app.get("/health")
async def health():
    return {"status": "running", "clients": len(clients)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("mcp_sse_server:app", host="127.0.0.1", port=8000, log_level="info")
