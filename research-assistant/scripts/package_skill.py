#!/usr/bin/env python3
"""
打包 research-assistant skill 为 .skill 文件
"""
import os
import sys
import zipfile
from pathlib import Path

def package_skill(skill_dir: str, output_dir: str = None) -> str:
    """将skill目录打包为.skill文件"""
    skill_path = Path(skill_dir).resolve()
    skill_name = skill_path.name

    if output_dir is None:
        output_dir = skill_path.parent

    output_path = Path(output_dir) / f"{skill_name}.skill"

    # 创建zip文件
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in skill_path.rglob('*'):
            if file_path.is_file():
                # 跳过已存在的.skill文件
                if file_path.suffix == '.skill':
                    continue
                arcname = file_path.relative_to(skill_path)
                zf.write(file_path, arcname)
                print(f"  添加: {arcname}")

    print(f"\n✅ 打包完成: {output_path}")
    print(f"   文件大小: {output_path.stat().st_size / 1024:.1f} KB")
    return str(output_path)

if __name__ == "__main__":
    skill_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    package_skill(skill_dir, output_dir)
