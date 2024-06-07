import subprocess
import sys

def install_dependencies():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def run_test():
    subprocess.check_call([sys.executable, "-m", "pytest"])

if __name__ == "__main__":
    install_dependencies()
    run_test()