from typing import List

from onlineafspraken.api.client import OnlineAfsprakenAPI
from onlineafspraken.api.utils import parse_schema
from onlineafspraken.schema.general import (
    GetAgendaResponse,
    GetAgendasResponse,
    GetAppointmentTypesResponse,
    GetResourceResponse,
    GetResourcesResponse,
    RequiresConfirmationResponse,
    AppointmentTypeSchema,
    AgendaSchema, ResourceSchema,
)

api = OnlineAfsprakenAPI()


def get_agenda(agenda_id) -> AgendaSchema:

    resp = api.get("getAgenda", id=agenda_id)

    return GetAgendaResponse.parse_obj(resp).agenda


def get_agendas() -> List[AgendaSchema]:

    resp = api.get("getAgendas")

    return parse_schema(
        resp,
        parse_key="Agenda",
        schema=GetAgendasResponse,
        enforce_list=True,
    )


def get_appointment_type(type_id) -> AppointmentTypeSchema:

    resp = api.get("getAppointmentType", id=type_id)

    return AppointmentTypeSchema.parse_obj(resp["Objects"]["AppointmentType"])


def get_appointment_types() -> List[AppointmentTypeSchema]:

    resp = api.get("getAppointmentTypes")

    return parse_schema(
        resp,
        parse_key="AppointmentType",
        schema=GetAppointmentTypesResponse,
        enforce_list=True,
    )


def get_resource(resource_id) -> ResourceSchema:

    resp = api.get("getResource", id=resource_id)

    return ResourceSchema.parse_obj(resp["Resource"])


def get_resources() -> List[ResourceSchema]:

    resp = api.get("getResources")

    return parse_schema(
        resp,
        parse_key="Resource",
        schema=GetResourcesResponse,
        enforce_list=True,
    )


def requires_confirmation() -> RequiresConfirmationResponse:

    resp = api.get("requiresConfirmation")

    return RequiresConfirmationResponse.parse_obj(resp)
