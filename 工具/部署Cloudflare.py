#!/usr/bin/env python3
"""使用本机 Wrangler 授权发布；不在项目中保存云凭证。"""
from pathlib import Path
import argparse
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--wrangler-js', help='可选：已安装的 Wrangler CLI 完整路径')
    args = parser.parse_args()
    subprocess.run([sys.executable, str(ROOT / '工具/构建静态站.py')], cwd=ROOT, check=True)
    command = ['node', args.wrangler_js] if args.wrangler_js else ['npx', '--yes', 'wrangler@4.151.0']
    command += ['pages', 'deploy', 'dist', '--project-name', 'store-operations-demo', '--branch', 'main']
    revision = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True)
    if revision.returncode == 0:
        command += ['--commit-hash', revision.stdout.strip()]
    subprocess.run(command, cwd=ROOT, check=True)
