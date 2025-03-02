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

from typing import TYPE_CHECKING, Literal, Optional, TypeVar, Union

from .item import Item
from ..components import FileComponent, UnfurledMediaItem
from ..enums import ComponentType

if TYPE_CHECKING:
    from typing_extensions import Self

    from .view import View

V = TypeVar('V', bound='View', covariant=True)

__all__ = ('File',)


class File(Item[V]):
    """Represents a UI file component.

    .. versionadded:: 2.6

    Parameters
    ----------
    media: Union[:class:`str`, :class:`.UnfurledMediaItem`]
        This file's media. If this is a string itmust point to a local
        file uploaded within the parent view of this item, and must
        meet the ``attachment://file-name.extension`` structure.
    spoiler: :class:`bool`
        Whether to flag this file as a spoiler. Defaults to ``False``.
    row: Optional[:class:`int`]
        The relative row this file component belongs to. By default
        items are arranged automatically into those rows. If you'd
        like to control the relative positioning of the row then
        passing an index is advised. For example, row=1 will show
        up before row=2. Defaults to ``None``, which is automatic
        ordering. The row number must be between 0 and 9 (i.e. zero indexed)
    """

    def __init__(
        self,
        media: Union[str, UnfurledMediaItem],
        *,
        spoiler: bool = False,
        row: Optional[int] = None,
    ) -> None:
        super().__init__()
        self._underlying = FileComponent._raw_construct(
            media=UnfurledMediaItem(media) if isinstance(media, str) else media,
            spoiler=spoiler,
        )

        self.row = row

    def _is_v2(self):
        return True

    @property
    def width(self):
        return 5

    @property
    def type(self) -> Literal[ComponentType.file]:
        return self._underlying.type

    @property
    def media(self) -> UnfurledMediaItem:
        """:class:`.UnfurledMediaItem`: Returns this file media."""
        return self._underlying.media

    @media.setter
    def media(self, value: UnfurledMediaItem) -> None:
        self._underlying.media = value

    @property
    def url(self) -> str:
        """:class:`str`: Returns this file's url."""
        return self._underlying.media.url

    @url.setter
    def url(self, value: str) -> None:
        self._underlying.media = UnfurledMediaItem(value)

    @property
    def spoiler(self) -> bool:
        """:class:`bool`: Returns whether this file should be flagged as a spoiler."""
        return self._underlying.spoiler

    @spoiler.setter
    def spoiler(self, value: bool) -> None:
        self._underlying.spoiler = value

    def to_component_dict(self):
        return self._underlying.to_dict()

    @classmethod
    def from_component(cls, component: FileComponent) -> Self:
        return cls(
            media=component.media,
            spoiler=component.spoiler,
        )
