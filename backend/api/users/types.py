from typing import List

import strawberry

from countries.types import Country


@strawberry.type
class MeUser:
    id: strawberry.ID
    email: str
    first_name: str
    last_name: str
    gender: str
    open_to_recruiting: bool
    date_birth: str
    business_name: str
    fiscal_code: str
    vat_number: str
    recipient_code: str
    pec_address: str
    address: str
    country: Country
    phone_number: str

    @strawberry.field
    def tickets(self, info, conference: str) -> List["Ticket"]:
        return self.tickets.filter(ticket_fare__conference__code=conference).all()


@strawberry.type
class User:
    id: strawberry.ID
    email: str
    name: str
    username: str
    first_name: str
    gender: str
    open_to_recruiting: bool
    date_birth: str
    business_name: str
    fiscal_code: str
    vat_number: str
    recipient_code: str
    pec_address: str
    address: str
    country: Country
    phone_number: str
