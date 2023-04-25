import json
from aiohttp import web
from models import User, Advertisement


async def hello(request):
    return web.json_response({
        'hello': 'world'
    })


async def get_user(user_id: int, session):
    user = await session.get(User, user_id)
    if user is None:
        raise web.HTTPNotFound(
            text=json.dumps({'status': 'error', 'detail': 'user not found'}),
            content_type='application/json'
        )
    return user


async def get_adv(adv_id: int, session):
    adv = await session.get(Advertisement, adv_id)
    if adv is None:
        raise web.HTTPNotFound(
            text=json.dumps({'status': 'error', 'detail': 'advertisement not found'}),
            content_type='application/json'
        )
    return adv


class UserView(web.View):
    @property
    def session(self):
        return self.request['session']

    async def get(self):
        user_id = int(self.request.match_info['user_id'])
        user = await get_user(user_id, self.session)
        return web.json_response({
            'id': user.id,
            'email': user.email,
        })

    async def post(self):
        user_data = await self.request.json()
        user = User(**user_data)
        self.session.add(user)
        await self.session.commit()
        return web.json_response({
            'id': user.id,
            'email': user.email,
        })

    async def delete(self):
        user_id = int(self.request.match_info['user_id'])
        user = await get_user(user_id, self.session)
        await self.session.delete(user)
        await self.session.commit()
        return web.json_response({'status': 'deleted'})


class AdvView(web.View):
    @property
    def session(self):
        return self.request['session']

    async def get(self):
        adv_id = int(self.request.match_info['adv_id'])
        adv = await get_adv(adv_id, self.session)
        return web.json_response({
            'id': adv.id,
            'title': adv.title,
        })

    async def post(self):
        adv_data = await self.request.json()
        adv = Advertisement(**adv_data)
        self.session.add(adv)
        await self.session.commit()
        return web.json_response({
            'id': adv.id,
            'title': adv.title,
        })

    async def delete(self):
        adv_id = int(self.request.match_info['adv_id'])
        adv = await get_adv(adv_id, self.session)
        await self.session.delete(adv)
        await self.session.commit()
        return web.json_response({'status': 'deleted'})
