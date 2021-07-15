#!/usr/bin/env python

"""Tests for `onlineafspraken` package."""
import datetime

import pytest
import respx
from httpx import Response

from onlineafspraken.api import appointment, availability, customers, general
from onlineafspraken.api.client import OnlineAfsprakenAPI




def test_get_bookable_days():
    bd = availability.get_bookable_days(32492, 346655, "2021-07-12", "2021-12-31")
    pass


def test_get_bookable_times():
    bd = availability.get_bookable_times(32492, 346655, "2021-07-13")
    pass


def test_set_customer():
    c = customers.set_customer("john", "doe", "johbdoe@test.com")
    pass


def test_get_customers():
    c = customers.get_customers()
    pass


def test_get_customer():
    c = customers.get_customer(26142790)
    pass


def test_appointment():

    types = general.get_appointment_types()

    agendas = general.get_agendas()

    bookable_times = availability.get_bookable_times(agenda_id=agendas[0].id, appointment_type_id=types[0].id, date=datetime.date.today())

    first_slot = bookable_times[0]

    result = appointment.set_appointment(
        32492,
        first_slot.start_time,
        first_slot.date,
        26142790,
        346655,
        description="Test 1234",
        name="Test Appointment",
    )

    assert result.id

    obj = appointment.get_appointment(result.id)

    assert obj.appointment.id == result.id

    appointment.remove_appointment(result.id)
