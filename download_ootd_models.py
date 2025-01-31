from huggingface_hub import snapshot_download

# Replace 'levihsu/OOTDiffusion' with the repository ID you want to download
repo_id = "levihsu/OOTDiffusion"
local_dir = "./OOTDiffusion"  # Local directory to save the files
revision = "main"  # Branch name or commit hash

# Download all files from the repository
snapshot_download(
    repo_id=repo_id,
    repo_type="model",  # Use "dataset" for datasets
    revision=revision,
    local_dir=local_dir,
    local_dir_use_symlinks=False  # Set to False to copy files instead of using symlinks
)

print(f"Repository '{repo_id}' downloaded to '{local_dir}'.")
