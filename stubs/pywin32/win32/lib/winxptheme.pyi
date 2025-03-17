import _win32typing

def OpenThemeData(hwnd: int, pszClasslist: str, /) -> _win32typing.PyHTHEME: ...
def CloseThemeData(hTheme: _win32typing.PyHTHEME, /) -> None: ...
def DrawThemeBackground(hTheme: _win32typing.PyHTHEME, hdc, iPartId, iStateId, pRect, pClipRect, /) -> None: ...
def DrawThemeText(
    hTheme: _win32typing.PyHTHEME, hdc, iPartId, iStateId, pszText: str, dwCharCount, dwTextFlags, dwTextFlags2, pRect, /
) -> None: ...
def GetThemeBackgroundContentRect(hTheme: _win32typing.PyHTHEME, hdc, iPartId, iStateId, pBoundingRect, /): ...
def GetThemeBackgroundExtent(hTheme: _win32typing.PyHTHEME, hdc, iPartId, iStateId, pContentRect, /): ...
def IsThemeActive() -> int: ...
def IsAppThemed() -> int: ...
def GetWindowTheme(hwnd: int, /) -> _win32typing.PyHTHEME: ...
def EnableThemeDialogTexture(hdlg, dwFlags, /) -> None: ...
def IsThemeDialogTextureEnabled(hdlg: int | None, /) -> bool: ...
def GetThemeAppProperties(): ...
def EnableTheming(fEnable, /) -> None: ...
def SetWindowTheme(hwnd: int, pszSubAppName: str, pszSubIdlist: str, /) -> None: ...
def GetCurrentThemeName() -> tuple[str, str, str]: ...

ETDT_DISABLE: int
ETDT_ENABLE: int
ETDT_ENABLETAB: int
ETDT_USETABTEXTURE: int
UNICODE: int
