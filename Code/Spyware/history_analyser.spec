# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:/Hackathons And Other Competitions/IPH/history_analyser.py'],
             pathex=['D:\\Hackathons And Other Competitions\\IPH'],
             binaries=[],
             datas=[('D:\\Hackathons And Other Competitions\\IPH\\url_categories_copy.csv', '.')],
             hiddenimports=['pyrebase'],
             hookspath=['.'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='history_analyser',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
