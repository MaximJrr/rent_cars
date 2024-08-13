import pytest

from app.users.service import UserService


@pytest.mark.parametrize("user_id, email, is_exists", [
    (7, "user@example.com", True),
    (6, "5sharik@moloko.ru", True),
    (6656, "error", False)
])
async def test_get_user_by_id(user_id, email, is_exists):
    user = await UserService.get_by_id(user_id)

    if is_exists:
        assert user
        assert user.id == user_id
        assert user.email == email
    else:
        assert not user
