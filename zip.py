import zipfile
import os

def create_github_zip():
    """将项目所有核心文件打包成 ZIP 以便上传 GitHub"""
    
    # 需要被打包的文件列表
    files_to_zip = [
        'README.md',
        '.gitignore',
        'requirements.txt',
        'config.py',
        'simulator.py',
        'agent.py',
        'main.py',
        'pack_to_zip.py'
    ]

    zip_filename = 'MicroEnv_Warning_Agent.zip'

    print("开始生成 GitHub 项目压缩包...")
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_zip:
            if os.path.exists(file):
                zipf.write(file)
                print(f"  [成功] 已添加文件: {file}")
            else:
                print(f"  [警告] 找不到文件，跳过: {file}")

    print(f"\n✅ 打包完成！成功生成压缩包：{zip_filename}")
    print("你可以直接将该压缩包上传到 GitHub，或者在本地解压后执行 git init 推送。")

if __name__ == "__main__":
    create_github_zip()