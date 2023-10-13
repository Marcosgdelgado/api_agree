"""Asyncio utils."""

import aiohttp
import json
from fastapi import HTTPException


async def async_post_request(url: str, data: dict):
    """Make request to external API."""
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=json.dumps(data)) as response:
            if response.status != 200:
                raise HTTPException(
                    status_code=response.status,
                    detail="Error while making request",
                )
            return await response.json()


async def async_get_request(url: str, params: dict = None):
    """Make GET request to external API."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status != 200:
                raise HTTPException(
                    status_code=response.status,
                    detail="Error while making request",
                )
            return await response.json()
