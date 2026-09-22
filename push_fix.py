#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Push the gradlew fix"""

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

    print("=" * 60)
    print("Committing and pushing gradlew fix...")
    print("=" * 60)

    run_command('git add gradlew', cwd=repo_path)
    run_command('git commit -m "修复gradlew脚本中的转义字符错误"', cwd=repo_path)
    run_command('git push origin main', cwd=repo_path)
    run_command('git push origin v1.0.0 --force', cwd=repo_path)

    print("\n" + "=" * 60)
    print("✓ Done! Check build at:")
    print("https://github.com/xiaodaoguoguo/XiaoDaoGuoGuoGame/actions")
    print("=" * 60)

    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        print(f"\nERROR: {e}", file=sys.stderr)
        sys.exit(1)
