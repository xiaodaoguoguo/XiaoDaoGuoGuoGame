#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check and fix gradlew permissions in Git"""

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
    return result.returncode, result.stdout

def main():
    repo_path = r'D:\project\XiaoDaoGuoGuoGame'

    print("=" * 60)
    print("Checking gradlew file permissions in Git...")
    print("=" * 60)

    # Check current permissions
    ret, output = run_command('git ls-files -s gradlew', cwd=repo_path)

    if '100644' in output:
        print("\n⚠ gradlew is NOT executable (mode: 100644)")
        print("Fixing permissions...")

        run_command('git update-index --chmod=+x gradlew', cwd=repo_path)

        print("\nVerifying fix...")
        ret, output = run_command('git ls-files -s gradlew', cwd=repo_path)

        if '100755' in output:
            print("✓ gradlew is now executable (mode: 100755)")

            print("\nCommitting permission change...")
            run_command('git commit -m "设置gradlew为可执行文件"', cwd=repo_path)

            print("\nPushing to GitHub...")
            run_command('git push origin main', cwd=repo_path)

            print("\nForce pushing tag to trigger build...")
            run_command('git push origin v1.0.0 --force', cwd=repo_path)

            print("\n" + "=" * 60)
            print("✓ Done! Check build at:")
            print("https://github.com/xiaodaoguoguo/XiaoDaoGuoGuoGame/actions")
            print("=" * 60)
        else:
            print("✗ Failed to set executable permission")
            return 1
    elif '100755' in output:
        print("\n✓ gradlew is already executable (mode: 100755)")
        print("Permissions are correct.")
    else:
        print(f"\n⚠ Unknown mode in output: {output}")

    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        print(f"\nERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
