from importlib.metadata import metadata
from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"You have created {number_of_advanced_collectibles} collectibles!")
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it to overwhite")
        else:
            print(f"Creating Metadata file: {metadata_file_name}")
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f"An adorable {breed} pup"
            image_path = "./img" + breed.lower().replace("_", "-") + ".png"
            # image_uri = upload_to_ipfs()
            # collectible_metadata["image"]=image_uri


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        # upload the binary ti IPFS
        image_biary = fp.read()
        ipfs_url = "http://127.0.0.1:5001/"
        endpoint = "/api/v0/add"
        reponse = requests.pot(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        # ""./img/PUG.png" -> "PUG.png"
        filename = filepath.split("/")[-1][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
