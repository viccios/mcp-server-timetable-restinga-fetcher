import httpx
from fastmcp import FastMCP

client = httpx.AsyncClient(base_url="https://timetablerestingafetcher.onrender.com")

openapi_spec = httpx.get(
    "https://raw.githubusercontent.com/viccios/timetable-restinga-fetcher/refs/heads/main/openapi.json"
).json()

mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec, client=client, name="Timetable Restinga Fetcher"
)

if __name__ == "__main__":
    mcp.run()
