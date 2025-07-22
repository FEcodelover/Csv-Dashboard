import subprocess

# Configure these variables
app_dir = "."  # Path to your app
connect_server = "https://rstudio-uat.sawater.com.au/connect/"
connect_api_key = "adWMAoH3YoFKDRDJKB2c2akanwNtPnkm"

def deploy():
    # This assumes rsconnect-python is installed and configured
    result = subprocess.run([
        "rsconnect", "deploy", "python",
        app_dir,
        "--server", connect_server,
        "--api-key", connect_api_key
    ])
    if result.returncode == 0:
        print("Deployment successful.")
    else:
        print("Deployment failed.", result)

if __name__ == "__main__":
    deploy()
