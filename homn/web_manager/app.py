import uvicorn
from tonberry import File, create_app, expose
from tonberry.content_types import TextHTML


class Root:
    @expose.get
    async def index(self) -> TextHTML:
        return File("frontend/dist/index.html")


app = create_app(root=Root)
app.add_static_route("frontend/dist/assets", route="/assets")
app.add_static_route("frontend/dist", route="")
uvicorn.run(
    app,
    port=8080,
    log_level=app.config.LOG_LEVEL.lower(),
    access_log=False,
)
