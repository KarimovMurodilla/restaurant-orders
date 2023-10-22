from httpx import AsyncClient


async def test_register(ac: AsyncClient):
    response = await ac.post("/auth/register", json={
        "name": "test",
        "email": "test@gmail.com",
        "password": "1234",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False
    })

    assert response.status_code == 201
