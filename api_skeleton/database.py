from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from supabase import create_client, Client
import os

from dotenv import load_dotenv

load_dotenv('/workspaces/algoexpert/api_skeleton/.env', override=True)

DATABASE_URL = os.environ['SUPABASE_CONNECTION_STRING']

engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Update the get_db function to use the async session maker
async def get_db():
    async with async_session_maker() as session:
        yield session
