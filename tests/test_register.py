from api.auth import Register
from fixtures.delete_user import delete_user
from utils.enums import HttpCodes

def test_register_new_uniq_user(delete_user):
    reg_client = Register()

    response = reg_client.register_new_user
    assert response.status_code == HttpCodes.OK

    token = response.json().get("accessToken")
    headers = {"Authorization": f"{token}"}

    delete_user.update(headers)