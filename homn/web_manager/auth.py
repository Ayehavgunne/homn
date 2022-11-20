from tonberry import expose
from tonberry.content_types import ApplicationJson


class Auth:
    @expose.post
    async def index(self, username: str, password: str) -> ApplicationJson:
        print(f"{username=} {password=}")
        return True
