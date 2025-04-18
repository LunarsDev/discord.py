"""
The MIT License (MIT)

Copyright (c) 2015-present Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations
from typing import Any, Protocol, TypeVar, TYPE_CHECKING

import asyncpg

if TYPE_CHECKING:
    from typing_extensions import TypeVar
    from .client import Client

    ClientT = TypeVar("ClientT", bound=Client, covariant=True, default=Client)
else:
    ClientT = TypeVar("ClientT", bound="Client", covariant=True)


class AsyncpgDatabase[RecordT: asyncpg.Record](Protocol):
    async def fetch(self, query: str, *args: Any) -> list[RecordT]: ...

    async def fetchrow(self, query: str, *args: Any) -> RecordT | None: ...

    async def fetchval(self, query: str, *args: Any) -> Any: ...

    async def execute(self, query: str, *args: Any) -> str: ...

    async def executemany(self, query: str, *args: Any) -> str: ...


if TYPE_CHECKING:
    from typing_extensions import TypeVar

    DatabaseT = TypeVar(
        "DatabaseT",
        bound=AsyncpgDatabase[asyncpg.Record] | None,
        covariant=True,
        default=None,
    )
else:
    DatabaseT = TypeVar(
        "DatabaseT",
        bound=AsyncpgDatabase[asyncpg.Record] | None,
        covariant=True,
    )
