import asyncio
from fastapi import Depends
import requests
import pandas as pd
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from models import IPLocation   
from pymongo.collection import Collection

from git import Repo

from persistence import get_db

class DataPullingService:
    async def __init__(self, url: str, db: Collection = Depends(get_db)):
        self.repo_url = url
        self.db = db
    
    async def clone_repo(self):
        pass
    
    async def pulling_task(self):
        pass