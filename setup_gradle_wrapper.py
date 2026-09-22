#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Download and setup Gradle Wrapper"""

import os
import urllib.request
import subprocess

def main():
    repo_path = r'D:\project\XiaoDaoGuoGuoGame'
    wrapper_dir = os.path.join(repo_path, 'gradle', 'wrapper')

    print("=" * 60)
    print("Setting up Gradle Wrapper...")
    print("=" * 60)

    # Create wrapper directory
    os.makedirs(wrapper_dir, exist_ok=True)
    print(f"\n✓ Created directory: {wrapper_dir}")

    # Download gradle-wrapper.jar
    jar_url = "https://raw.githubusercontent.com/gradle/gradle/master/gradle/wrapper/gradle-wrapper.jar"
    jar_path = os.path.join(wrapper_dir, 'gradle-wrapper.jar')

    print(f"\nDownloading gradle-wrapper.jar...")
    print(f"From: {jar_url}")
    print(f"To: {jar_path}")

    try:
        urllib.request.urlretrieve(jar_url, jar_path)
        print(f"✓ Downloaded: {os.path.getsize(jar_path)} bytes")
    except Exception as e:
        print(f"✗ Download failed: {e}")
        return 1

    # Create gradle-wrapper.properties
    properties_path = os.path.join(wrapper_dir, 'gradle-wrapper.properties')
    properties_content = """distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\\://services.gradle.org/distributions/gradle-8.0-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
"""

    with open(properties_path, 'w', newline='\n') as f:
        f.write(properties_content)

    print(f"\n✓ Created: {properties_path}")

    # Add to git
    print("\nAdding to Git...")
    os.chdir(repo_path)
    subprocess.run(['git', 'add', 'gradle/'], check=True)
    subprocess.run(['git', 'commit', '-m', '添加Gradle Wrapper文件'], check=True)
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
