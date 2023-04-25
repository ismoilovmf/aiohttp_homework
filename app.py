from aiohttp import web
from views import UserView, AdvView, hello
from middlewares import session_middleware
from models import Base, engine

app = web.Application(middlewares=[session_middleware])


async def orm_context(app: web.Application):
    print('Started')
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()
    print('Stopped')


app.cleanup_ctx.append(orm_context)

app.add_routes([web.get('/hello', hello)])

app.add_routes([
    web.get('/users/{user_id:\d+}', UserView),
    web.delete('/users/{user_id:\d+}', UserView),
    web.post('/users', UserView)
])

app.add_routes([
    web.get('/advs/{adv_id:\d+}', AdvView),
    web.delete('/advs/{adv_id:\d+}', AdvView),
    web.post('/advs', AdvView)
])

if __name__ == '__main__':
    web.run_app(app)
