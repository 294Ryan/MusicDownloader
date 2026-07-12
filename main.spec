# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('ffmpeg_bin', 'ffmpeg_bin')],
    hiddenimports=['quickjs', 'quickjs_ng'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='musicDownloader_v2.4',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
<<<<<<< HEAD:main.spec
    icon=['icon_v2.ico'],
=======
    icon=['/icons/icon_v2.ico'],
>>>>>>> 1639c3114f6f03f9700090c9d53a3988d6932fb2:v2.3/musicDownloader_v2.3.spec
)
