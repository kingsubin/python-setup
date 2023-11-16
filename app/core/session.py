from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core import config

sqlalchemy_database_url = config.settings.SQLALCHEMY_DATABASE_URL

async_engine = create_async_engine(sqlalchemy_database_url, echo=True)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)
