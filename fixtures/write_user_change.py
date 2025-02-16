import json
import pytest

from utils.helpers import environment


@pytest.fixture
def write_user_change(request):

    yield

    new_value = data.get(request.param)

    with open(environment.USER_FILE, "r+") as file:
        json_data = json.load(file)
        json_data[request.param] = new_value
        json.dump(json_data, file)

    return write_user_change
