import sys
import subprocess
from pathlib import Path

def ensure_gdown_installed():
    try:
        import gdown
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "gdown"])
    finally:
        import gdown
    return gdown

def main():
    gdown = ensure_gdown_installed()

    # Make sure the "data" folder exists
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    # Replace this with your file ID
    file_id = "1vRGkGk6Uk5W-7jE8ROtQxAsa6UgCMEeW"  
    url = f"https://drive.google.com/uc?id={file_id}"
    output = data_dir / "downloaded_data.csv"

    print(f"Downloading file to {output} ...")
    gdown.download(url, str(output), quiet=False)
    print("Download completed.")

if __name__ == "__main__":
    main()
