#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Force Git to renormalize gradlew"""

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
    print("Force Git to renormalize all files...")
    print("=" * 60)

    # Remove all files from index
    print("\nStep 1: Removing all files from Git index...")
    run_command('git rm --cached -r .', cwd=repo_path)

    # Reset HEAD to restore .gitattributes
    print("\nStep 2: Resetting HEAD...")
    run_command('git reset --hard HEAD', cwd=repo_path)

    # Re-add all files with new normalization
    print("\nStep 3: Re-adding all files with normalization...")
    run_command('git add --renormalize .', cwd=repo_path)

    # Check status
    print("\nStep 4: Checking status...")
    run_command('git status', cwd=repo_path)

    # Commit if there are changes
    print("\nStep 5: Committing normalized files...")
    ret = run_command('git commit -m "重新规范化所有文本文件的换行符"', cwd=repo_path)

    if ret == 0:
        print("\nStep 6: Pushing to GitHub...")
        run_command('git push origin main', cwd=repo_path)

        print("\nStep 7: Force pushing tag to trigger build...")
        run_command('git push origin v1.0.0 --force', cwd=repo_path)

        print("\n" + "=" * 60)
        print("✓ Done! Check:")
        print("https://github.com/xiaodaoguoguo/XiaoDaoGuoGuoGame/actions")
        print("=" * 60)
    else:
        print("\nNo changes to commit.")

    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        print(f"\nERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
