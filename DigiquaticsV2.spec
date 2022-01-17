# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:/Users/Harri/OneDrive/Projects/PatronCounts/main.py'],
             pathex=[],
             binaries=[],
             datas=[('C:/Users/Harri/OneDrive/Projects/PatronCounts/ChemicalRecordTemplate.xlsx', '.'), ('C:/Users/Harri/OneDrive/Projects/PatronCounts/input.txt', '.'), ('C:/Users/Harri/OneDrive/Projects/PatronCounts/update1.1.txt', '.'), ('C:/Users/Harri/OneDrive/Projects/PatronCounts/update1.2.txt', '.'), ('C:/Users/Harri/OneDrive/Projects/PatronCounts/update1.3.txt', '.'), ('C:/Users/Harri/OneDrive/Projects/PatronCounts/Version.txt', '.'), ('C:/Users/Harri/OneDrive/Projects/PatronCounts/Website', 'Website/'), ('C:/Users/Harri/AppData/Local/Programs/Python/Python310/chromedriver.exe', '.'), ('C:/Users/Harri/AppData/Local/Programs/Python/Python310/geckodriver.exe', '.'), ('C:/Users/Harri/AppData/Local/Programs/Python/Python310/IEDriverServer.exe', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          [],
          exclude_binaries=True,
          name='DigiquaticsV2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , version='C:\\Users\\Harri\\OneDrive\\Projects\\PatronCounts\\file_version_info.txt', icon='C:\\Users\\Harri\\Downloads\\Logomark.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='DigiquaticsV2')
