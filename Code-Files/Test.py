import pytest
import json
from backend.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ─── HEALTH CHECK ────────────────────────────────────────────

def test_health_check(client):
    res = client.get("/health")
    assert res.status_code == 200
    data = json.loads(res.data)
    assert data["status"] == "ok"


# ─── CREATE NOTE ─────────────────────────────────────────────

def test_create_note(client):
    res = client.post("/api/notes", json={
        "title": "My First Note",
        "content": "This is a test note.",
        "tag": "work"
    })
    assert res.status_code == 201
    data = json.loads(res.data)
    assert data["success"] is True
    assert data["note"]["title"] == "My First Note"


def test_create_note_missing_fields(client):
    res = client.post("/api/notes", json={"title": "Only Title"})
    assert res.status_code == 400


# ─── GET NOTES ───────────────────────────────────────────────

def test_get_all_notes(client):
    res = client.get("/api/notes")
    assert res.status_code == 200
    data = json.loads(res.data)
    assert "notes" in data


# ─── DELETE NOTE ─────────────────────────────────────────────

def test_delete_nonexistent_note(client):
    res = client.delete("/api/notes/fake-id-999")
    assert res.status_code == 404
