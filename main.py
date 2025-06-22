from fastmcp import FastMCP
import requests
from requests import Response

mcp = FastMCP("Fetch schedule data from Timetable Restinga website")


@mcp.tool
def get_teachers() -> dict:
    response: Response = requests.get("http://localhost:3000/api/teachers")
    return response.json()


@mcp.tool
def get_subjects() -> dict:
    response: Response = requests.get("http://localhost:3000/api/subjects")
    return response.json()


@mcp.tool
def get_classrooms() -> dict:
    response: Response = requests.get("http://localhost:3000/api/classrooms")
    return response.json()


@mcp.tool
def get_classes() -> dict:
    response: Response = requests.get("http://localhost:3000/api/classes")
    return response.json()


@mcp.tool
def get_periods() -> dict:
    response: Response = requests.get("http://localhost:3000/api/periods")
    return response.json()


@mcp.tool
def get_dayparts() -> dict:
    response: Response = requests.get("http://localhost:3000/api/dayparts")
    return response.json()


@mcp.tool
def get_dates() -> dict:
    response: Response = requests.get("http://localhost:3000/api/dates")
    return response.json()


@mcp.tool
def get_event_types() -> dict:
    response: Response = requests.get("http://localhost:3000/api/event_types")
    return response.json()


if __name__ == "__main__":
    mcp.run()
