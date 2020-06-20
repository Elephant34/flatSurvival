import pathlib

save_file = pathlib.Path("assets/data/worldSave.json")
zone_dict = pathlib.Path("assets/data/zones/")

try:
    save_file.unlink()

    for file in zone_dict.rglob("*"):
        file.unlink()
    zone_dict.rmdir()
except FileNotFoundError:
    pass

print("Game save files deleted")
