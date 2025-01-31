from huggingface_hub import snapshot_download

# Define repository details
repo_id = "openai/clip-vit-large-patch14"  # Hugging Face repository ID
local_dir = "./checkpoints/clip-vit-large-patch14"  # Directory to save the files
revision = "main"  # Branch name or specific commit hash (default: "main")

# Download all files from the repository
snapshot_download(
    repo_id=repo_id,
    repo_type="model",  # Specify "model" as it's a model repository
    revision=revision,
    local_dir=local_dir,
    local_dir_use_symlinks=False  # Copy files instead of using symlinks
)

print(f"Repository '{repo_id}' downloaded to '{local_dir}'.")
