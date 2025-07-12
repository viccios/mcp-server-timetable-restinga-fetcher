import os
import requests
from requests import Response
from dotenv import load_dotenv
from fastmcp import FastMCP

load_dotenv()

TIMETABLE_RESTINGA_FETCHER_API_URL = os.environ["TIMETABLE_RESTINGA_FETCHER_API_URL"]

mcp = FastMCP("Fetch schedule data from Timetable Restinga website")


@mcp.tool
def get_periods() -> dict:
    """Get the name, ID and start and end time of the periods"""
    response: Response = requests.get(f"{TIMETABLE_RESTINGA_FETCHER_API_URL}/periods")
    return response.json()


@mcp.tool
def get_subjects() -> dict:
    """Get the name and ID of the subjects"""
    response: Response = requests.get(f"{TIMETABLE_RESTINGA_FETCHER_API_URL}/subjects")
    return response.json()


@mcp.tool
def get_teachers() -> dict:
    """Get the name and ID of the teachers"""
    response: Response = requests.get(f"{TIMETABLE_RESTINGA_FETCHER_API_URL}/teachers")
    return response.json()


@mcp.tool
def get_classes() -> dict:
    """Get the name and ID of school subjects"""
    response: Response = requests.get(f"{TIMETABLE_RESTINGA_FETCHER_API_URL}/classes")
    return response.json()


@mcp.tool
def get_classrooms() -> dict:
    """Get the name and ID of the classroooms"""
    response: Response = requests.get(
        f"{TIMETABLE_RESTINGA_FETCHER_API_URL}/classrooms"
    )
    return response.json()


@mcp.tool
def get_class_schedule() -> dict:
    """
    Get the name and ID of the classes,
    with detailed schedule information
    """
    response: Response = requests.get(
        f"{TIMETABLE_RESTINGA_FETCHER_API_URL}/class_schedule"
    )
    return response.json()


@mcp.tool
def get_teachers_schedule() -> dict:
    """
    Get the name and ID of teachers,
    with detailed information about
    classes, classrooms and schedules
    """
    response: Response = requests.get(
        f"{TIMETABLE_RESTINGA_FETCHER_API_URL}/teachers_schedule"
    )
    return response.json()


@mcp.tool
def get_classrooms_schedule() -> dict:
    """
    Get the name and ID of the classrooms,
    with detailed information about
    classes, teachers, classes and schedules
    """
    response: Response = requests.get(
        f"{TIMETABLE_RESTINGA_FETCHER_API_URL}/classrooms_schedule"
    )
    return response.json()


if __name__ == "__main__":
    mcp.run()
