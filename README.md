# convert_to_webp_addon

## Usage
1. Install `pip` and `Pillow`
```
<BlenderのPython実行ファイルのパス> -m ensurepip
<BlenderのPython実行ファイルのパス> -m pip install Pillow
```

- Windows: C:\Program Files\Blender Foundation\Blender <バージョン>\<バージョン>\python\bin\python.exe
= macOS: /Applications/Blender.app/Contents/Resources/<バージョン>/python/bin/python3.10
- Linux: blender/<バージョン>/python/bin/python3.10

2. Download zip from git
3. Open Blender and register the zip file downloaded from git as an add-on
  - Change the Blender version in the __init__.py file if necessary.
4. If the command is added as follows, you are done