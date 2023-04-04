import asyncio
from prisma import Prisma


async def main() -> None:
    db = Prisma()
    await db.connect()

    # models = await db.model.find_many()

    async def get_modelId_from_stlID(stlID: str):
        return await db.model.find_first(where={'stlId': stlID})

    model = await get_modelId_from_stlID('1YkElT0POFyn9cVbOr2fNOWt9S_kiUPf6')
    print(model.id if model else 'No model found')

    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
