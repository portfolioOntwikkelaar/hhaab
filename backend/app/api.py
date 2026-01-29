from fastapi import APIRouter
from datetime import date, timedelta
from .calendar_engine import MayaCalendarEngine, get_haab_from_gregorian

router = APIRouter()

@router.get("/today")
def today():
    d = date.today()
    engine = MayaCalendarEngine.from_gregorian(d)
    return {
        "tzolkin": engine.get_tzolkin(),
        "haab": get_haab_from_gregorian(d)
    }

@router.get("/yesterday")
def yesterday():
    d = date.today() - timedelta(days=1)
    engine = MayaCalendarEngine.from_gregorian(d)
    return {
        "tzolkin": engine.get_tzolkin(),
        "haab": get_haab_from_gregorian(d)
    }

@router.get("/tomorrow")
def tomorrow():
    d = date.today() + timedelta(days=1)
    engine = MayaCalendarEngine.from_gregorian(d)
    return {
        "tzolkin": engine.get_tzolkin(),
        "haab": get_haab_from_gregorian(d)
    }
