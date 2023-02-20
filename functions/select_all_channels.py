from loader import db


async def get_all_channels():
    return await db.select_all_channels()
