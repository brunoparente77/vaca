# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['vaca.py'],
    pathex=[],
    binaries=[],
    datas=[('icon.svg', '.'),
           ('calc_icon.svg', '.'),
           ('clear_icon.svg', '.'),
           ('relat_icon.svg', '.'),
           ('alert.svg', '.'),
           ('ok.svg', '.'),
           ('critical.svg', '.'),
           ('logo.png', '.'),
           ('vaca.qss', '.'),
           ('theme', 'theme'),
           ('LICENSE', '.'),
           ('Cantarell-Regular.ttf', '.'),
           ('Cantarell-Bold.ttf', '.'),
           ('Cantarell-BoldItalic.ttf', '.'),
           ('Cantarell-Italic.ttf', '.'),
           ('licenças', 'licenças')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='vaca',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    contents_directory='.',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='vaca',
)
