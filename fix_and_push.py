#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix gradlew line endings and push to GitHub"""

import subprocess
import sys

def run_command(cmd, cwd=None):
    """Run command and print output"""
    print(f"\n> {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, encoding='utf-8')
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.returncode

def main():
    repo_path = r'D:\project\XiaoDaoGuoGuoGame'
    gradlew_path = r'D:\project\XiaoDaoGuoGuoGame\gradlew'

    print("=" * 60)
    print("Step 1: Converting gradlew to LF line endings...")
    print("=" * 60)

    # Read file in binary mode
    with open(gradlew_path, 'rb') as f:
        content = f.read()

    original_size = len(content)
    crlf_count = content.count(b'\r\n')

    print(f"Original file size: {original_size} bytes")
    print(f"CRLF occurrences: {crlf_count}")

    # Convert CRLF to LF
    content = content.replace(b'\r\n', b'\n')

    # Write back in binary mode
    with open(gradlew_path, 'wb') as f:
        f.write(content)

    new_size = len(content)
    print(f"New file size: {new_size} bytes")
    print(f"Bytes saved: {original_size - new_size}")
    print("✓ Conversion complete!")

    print("\n" + "=" * 60)
    print("Step 2: Checking git status...")
    print("=" * 60)
    run_command('git status', cwd=repo_path)

    print("\n" + "=" * 60)
    print("Step 3: Adding gradlew to git...")
    print("=" * 60)
    run_command('git add gradlew', cwd=repo_path)

    print("\n" + "=" * 60)
    print("Step 4: Committing changes...")
    print("=" * 60)
    run_command('git commit -m "将gradlew转换为Unix LF换行符"', cwd=repo_path)

    print("\n" + "=" * 60)
    print("Step 5: Pushing to GitHub main branch...")
    print("=" * 60)
    if run_command('git push origin main', cwd=repo_path) != 0:
        print("ERROR: Failed to push to main branch!")
        return 1

    print("\n" + "=" * 60)
    print("Step 6: Force pushing tag v1.0.0...")
    print("=" * 60)
    if run_command('git push origin v1.0.0 --force', cwd=repo_path) != 0:
        print("ERROR: Failed to push tag!")
        return 1

    print("\n" + "=" * 60)
    print("✓ All done!")
    print("=" * 60)
    print("\nCheck build status at:")
    print("https://github.com/xiaodaoguoguo/XiaoDaoGuoGuoGame/actions")

    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        print(f"\nERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
