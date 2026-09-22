#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Download correct gradlew from Gradle repository"""

import urllib.request
import subprocess
import os

def main():
    repo_path = r'D:\project\XiaoDaoGuoGuoGame'
    gradlew_path = os.path.join(repo_path, 'gradlew')

    print("=" * 60)
    print("Downloading correct gradlew from official source...")
    print("=" * 60)

    # Download from Gradle's official repository
    url = "https://raw.githubusercontent.com/gradle/gradle/master/gradlew"

    print(f"\nDownloading from: {url}")
    print(f"To: {gradlew_path}")

    try:
        urllib.request.urlretrieve(url, gradlew_path)
        file_size = os.path.getsize(gradlew_path)
        print(f"✓ Downloaded: {file_size} bytes")
    except Exception as e:
        print(f"✗ Download failed: {e}")
        return 1

    # Set executable permission in Git
    print("\nSetting executable permission...")
    os.chdir(repo_path)
    subprocess.run(['git', 'update-index', '--chmod=+x', 'gradlew'], check=True)
    print("✓ Permission set")

    # Commit and push
    print("\nCommitting changes...")
    subprocess.run(['git', 'add', 'gradlew'], check=True)
    subprocess.run(['git', 'commit', '-m', '使用官方正确的gradlew脚本'], check=True)
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
