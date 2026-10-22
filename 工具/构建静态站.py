#!/usr/bin/env python3
"""将原始单文件 Demo 原样复制至 Cloudflare Pages 发布目录。"""
from pathlib import Path
from hashlib import sha256
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / '门店经营.html'
OUTPUT = ROOT / 'dist'

if __name__ == '__main__':
    OUTPUT.mkdir(exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT / 'index.html')
    shutil.copyfile(ROOT / '_headers', OUTPUT / '_headers')
    assert (OUTPUT / 'index.html').read_bytes() == SOURCE.read_bytes()
    print('输出：dist/index.html')
    print('SHA-256：' + sha256(SOURCE.read_bytes()).hexdigest())
