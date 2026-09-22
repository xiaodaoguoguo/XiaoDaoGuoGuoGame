#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove txt files from res directories"""

import os
import subprocess

def main():
    repo_path = r'D:\project\XiaoDaoGuoGuoGame'

    print("=" * 60)
    print("Removing .txt files from res directories...")
    print("=" * 60)

    txt_files = [
        r'app\src\main\res\mipmap-hdpi\图标说明.txt',
        r'app\src\main\res\mipmap-mdpi\图标说明.txt',
        r'app\src\main\res\mipmap-xhdpi\图标说明.txt',
        r'app\src\main\res\mipmap-xxhdpi\图标说明.txt',
        r'app\src\main\res\mipmap-xxxhdpi\图标说明.txt',
    ]

    os.chdir(repo_path)

    for txt_file in txt_files:
        full_path = os.path.join(repo_path, txt_file)
        if os.path.exists(full_path):
            os.remove(full_path)
            print(f"✓ Removed: {txt_file}")
        else:
            print(f"  Not found: {txt_file}")

    print("\nCommitting changes...")
    subprocess.run(['git', 'add', '-A'], check=True)
    subprocess.run(['git', 'commit', '-m', '删除res目录中的txt文件以修复构建错误'], check=True)
    subprocess.run(['git', 'push', 'origin', 'main'], check=True)
    subprocess.run(['git', 'push', 'origin', 'v1.0.0', '--force'], check=True)

    print("\n" + "=" * 60)
    print("✓ Done! Check build at:")
    print("https://github.com/xiaodaoguoguo/XiaoDaoGuoGuoGame/actions")
    print("=" * 60)

    return 0

if __name__ == '__main__':
    import sys
    try:
        sys.exit(main())
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
