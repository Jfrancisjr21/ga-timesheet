def test_healthz(client, db):
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_email_is_lowercased(db, django_user_model):
    user = django_user_model.objects.create(username="a", email="  Jane@School.EDU ")
    assert user.email == "jane@school.edu"
