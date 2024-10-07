import subprocess
import time
from datetime import datetime
import pytz
import os
from tqdm import tqdm
subprocess.run(['pip', 'install', '-qq', 'pytz', 'tqdm', 'gdown'])
# subprocess.run(['sudo', '-v', ';', 'curl', 'https://rclone.org/install.sh', '|', 'sudo', 'bash'])
vietnam_tz = pytz.timezone('Asia/Ho_Chi_Minh')
TIMESTAMP = datetime.now(vietnam_tz).strftime('%Y-%m-%d %H-%M-%S')

def sync_files(src, dest):
    os.makedirs(dest, exist_ok=True)
    sync_command = ['rclone', 'sync', src, dest, '-P', '-L']
    try:
        subprocess.run(sync_command, check=True)
        print(f"Sync completed successfully to {dest}")
    except subprocess.CalledProcessError as e:
        print(f"Error during sync: {e}")

def sync(loop=False):
    source = "/kaggle/working/PPAL/work_dirs"
    dest = "onedrive:EPBAL"
    dest = os.path.join(dest, TIMESTAMP)
    if not loop:
        print('-'*40)
        print(f"{source} -> {dest}")
        sync_files(source, dest)
    else:
        while True:
            print('-'*40)
            print(f"{source} -> {dest}")
            sync_files(source, dest)
            for _ in tqdm(range(300), desc="Waiting for next sync", ncols=100):
                time.sleep(1)
def main():
    sync(loop=True)

if __name__ == "__main__":
    main()