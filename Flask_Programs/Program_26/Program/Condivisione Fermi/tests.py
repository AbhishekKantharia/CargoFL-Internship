import pytest
import server
import random

# NOTE: These tests should be executed in order AND together, or else some database-related things may not work.


@pytest.fixture
def app():
    app = server.app
    app.debug = True
    app.config["TESTING"] = True
    # Use an in-memory database for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    with app.app_context():
        server.db.create_all()
    return app.test_client()


def test_register_page(app):
    res = app.get("/register")
    assert res.status_code == 200


def test_register_no_captcha(app):
    res = app.post("/register")
    assert res.status_code == 400


def test_register_only_captcha(app):
    res = app.post("/register", data={
        "g-recaptcha-response": "sì"
    })
    assert res.status_code == 400


def test_register_missing_fields(app):
    res = app.post("/register", data={
        "g-recaptcha-response": "sì",
        "username": "ciao",
        "password": "saaaas"
    })
    assert res.status_code == 400


def test_register_valid(app):
    # 1
    res = app.post("/register", data={
        "g-recaptcha-response": "sì",
        "username": "admin@example.org",
        "password": "password123",
        "nome": "Prova",
        "cognome": "Unoduetre",
        "classe": "1A",
        "usernameTelegram": "@BotFather",
        "mailGenitori": "dad@example.org"
    }, follow_redirects=True)
    assert res.status_code == 200
    # 2
    res = app.post("/register", data={
        "g-recaptcha-response": "sì",
        "username": "user@example.org",
        "password": "password123",
        "nome": "Prova",
        "cognome": "Unoduetre",
        "classe": "1A",
        "usernameTelegram": "@BotFather",
        "mailGenitori": "mom@example.org"
    }, follow_redirects=True)
    # 3
    assert res.status_code == 200
    res = app.post("/register", data={
        "g-recaptcha-response": "sì",
        "username": "peer@example.org",
        "password": "password123",
        "nome": "Prova",
        "cognome": "Unoduetre",
        "classe": "1A",
        "usernameTelegram": "@BotFather",
        "mailGenitori": "sas@example.org"
    }, follow_redirects=True)
    assert res.status_code == 200
    # 4
    res = app.post("/register", data={
        "g-recaptcha-response": "sì",
        "username": "prof@example.org",
        "password": "password123",
        "nome": "Prova",
        "cognome": "Unoduetre",
        "classe": "1A",
        "usernameTelegram": "@BotFather",
        "mailGenitori": "sas@example.org"
    }, follow_redirects=True)
    assert res.status_code == 200
    # 5
    res = app.post("/register", data={
        "g-recaptcha-response": "sì",
        "username": "new_admin@example.org",
        "password": "password123",
        "nome": "Prova",
        "cognome": "Unoduetre",
        "classe": "1A",
        "usernameTelegram": "@BotFather",
        "mailGenitori": "sas@example.org"
    }, follow_redirects=True)
    assert res.status_code == 200


def test_login_page(app):
    res = app.get("/login")
    assert res.status_code == 200


def test_login_no_username(app):
    res = app.post("/login", data={
        "password": "haha"
    })
    assert res.status_code == 400


def test_login_no_password(app):
    res = app.post("/login", data={
        "username": "sacripante"
    })
    assert res.status_code == 400


def test_login_nothing(app):
    res = app.post("/login")
    assert res.status_code == 400


def test_login_invalid(app):
    res = app.post("/login", data={
        "username": str(random.random()),
        "password": str(random.random())
    })
    assert res.status_code == 403


def test_login_valid(app):
    res = app.post("/login", data={
        "username": "user@example.org",
        "password": "password123"
    }, follow_redirects=True)
    assert res.status_code == 200
    # TODO: Test session data changes


@pytest.fixture
def app_admin(app):
    with app.session_transaction() as ses:
        ses["username"] = "admin@example.org"
        return app


@pytest.fixture
def app_user(app):
    with app.session_transaction() as ses:
        ses["username"] = "user@example.org"
        return app


def test_user_ascend_forbidden(app_user):
    res = app_user.get("/user_ascend/1")
    assert res.status_code == 403


# def test_user_ascend_valid(app_admin):
#     TODO

# @pytest.fixture
# def app_peer(app):
#     with app.session_transaction() as ses:
#         ses["username"] = "peer@example.org"
#         return app


def test_user_godify_forbidden(app_user):
    res = app_user.get("/user_godify/1")
    assert res.status_code == 403


# def test_user_godify_valid(app_admin):
#     TODO


def test_user_teacher_forbidden(app_user):
    res = app_user.get("/user_teacher/1")
    assert res.status_code == 403


# def test_user_teacher_valid(app_admin):
#     TODO

# @pytest.fixture
# def app_prof(app):
#     with app.session_transaction() as ses:
#         ses["username"] = "prof@example.org"
#         return app

def test_dashboard_redirect_not_loggedin(app):
    res = app.get("/dashboard")
    assert res.status_code == 302


def test_dashboard_display(app_user):
    res = app_user.get("/dashboard")
    assert res.status_code == 200


def test_informazioni_display(app):
    res = app.get("/informazioni")
    assert res.status_code == 200


def test_message_add_forbidden(app_user):
    res = app_user.get("/message_add")
    assert res.status_code == 403


def test_message_del_forbidden(app_user):
    res = app_user.get("/message_del/1")
    assert res.status_code == 403


def test_user_list_forbidden(app_user):
    res = app_user.get("/user_list")
    assert res.status_code == 403


def test_user_changepw_forbidden(app_user):
    # Forse un utente dovrebbe essere in grado di cambiare la sua stessa password...
    res = app_user.get("/user_changepw/1")
    assert res.status_code == 403


def test_user_del_forbidden(app_user):
    res = app_user.get("/user_del/1")
    assert res.status_code == 403


def test_log_view_forbidden(app_user):
    res = app_user.get("/server_log")
    assert res.status_code == 403


def test_log_view_valid(app_admin):
    res = app_admin.get("/server_log")
    assert res.status_code == 200


def test_brasatura_forbidden(app_user):
    res = app_user.get("/brasatura/1")
    assert res.status_code == 403
    res = app_user.get("/brasatura/2")
    assert res.status_code == 403


# Questo dovrebbe essere l'ultimo test per motivi ovvii
def test_brasatura_valid(app_admin):
    res = app_admin.get("/brasatura/1")
    assert res.status_code == 200
    res = app_admin.get("/brasatura/2")
    assert res.status_code == 302
    # TODO: test if the data is actually deleted
