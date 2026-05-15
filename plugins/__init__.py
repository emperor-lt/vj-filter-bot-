# Don't Remove Credit @SUPREME_BOTz
# Subscribe YouTube Channel For Amazing Bot @SUPREME_BOTz
# Ask Doubt on telegram @SUPREME_BOTz

from aiohttp import web
from .route import routes

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
