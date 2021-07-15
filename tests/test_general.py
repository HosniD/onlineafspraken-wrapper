import pytest
import respx
from httpx import Response

from onlineafspraken.api import general
from onlineafspraken.api.client import OnlineAfsprakenAPI
from onlineafspraken.schema.general import (
    GetAgendasResponse,
    AppointmentTypeSchema,
    AgendaSchema,
    GetAgendaResponse,
    GetAppointmentTypeResponse,
    ResourceSchema,
)


@pytest.fixture
def mock_get_agendas():
    api = OnlineAfsprakenAPI()

    with respx.mock(base_url=api.get_base_url(), assert_all_called=False) as mock:
        route = mock.get(params=api.set_params("getAgendas"), name="get_agendas")
        mock_resp_content = """<?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Status>
                <APIVersion>1.0</APIVersion>
                <Date>2021-06-25 14:09:13</Date>
                <Timestamp>1624622953</Timestamp>
                <Status>success</Status>
            </Status>
            <Objects>
                <Agenda>
                    <Id>32492</Id>
                    <Name>Test 1</Name>
                    <DateFormat>D d/m/Y</DateFormat>
                    <TimeFormat>H:i</TimeFormat>
                    <AlignGrid>5</AlignGrid>
                    <IsDefault>1</IsDefault>
                </Agenda>
                <Agenda>
                    <Id>32493</Id>
                    <Name>Test 2</Name>
                    <DateFormat>D d/m/Y</DateFormat>
                    <TimeFormat>H:i</TimeFormat>
                    <AlignGrid>5</AlignGrid>
                    <IsDefault>1</IsDefault>
                </Agenda>
            </Objects>
        </Response>
        """
        route.return_value = Response(200, text=mock_resp_content)
        yield mock


def test_get_agendas_200(mock_get_agendas):
    response = general.get_agendas()

    assert mock_get_agendas["get_agendas"].called

    assert isinstance(response, list)
    assert isinstance(response[0], AgendaSchema)
    assert response[0].name == "Test 1"


def test_get_agenda(agenda_id):
    response = general.get_agenda(agenda_id=agenda_id)
    assert isinstance(response, AgendaSchema)


def test_get_appointment_types():
    result = general.get_appointment_types()
    assert isinstance(result, list)
    assert isinstance(result[0], AppointmentTypeSchema)

    result = general.get_appointment_type(result[0].id)

    assert isinstance(result, AppointmentTypeSchema)


def test_get_resources():
    response = general.get_resources()
    assert isinstance(response, list)
    assert isinstance(response[0], ResourceSchema)

    response = general.get_resource(response[0].id)
    assert isinstance(response, ResourceSchema)
