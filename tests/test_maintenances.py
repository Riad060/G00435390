from typing import Literal

from fastapi.testclient import TestClient
import pytest

def maintenance_payload(
        equipment_id = 1,
        student_id = "ST-RB1234",
        description = "This is my description",
):
    return{
        "equipment_id":equipment_id,
        "student_id":student_id,
        "description":description,
    }
def test_create_maintenance_returns_201(
        client: TestClient,

):
    response=client.post(
        "/api/maintenances",
        json=maintenance_payload(),
    )
    assert response.status_code==201
    data=response.json()
    assert data["id"]==1
    assert data ["status"]=="OPEN"

@pytest.mark.parametrize(
    "bad_ids",[0,4]
)
def test_bad_ids_returns_422(
    client: TestClient,bad_ids: Literal[0] | Literal[4]
):
    response = client.post(
        "/api/bad ids",
        json=maintenance_payload(
            student_id=bad_ids
        ),
    )
    assert response.status_code==422