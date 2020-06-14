import pathlib

save_file = pathlib.Path("assets/data/worldSave.json")
zone_dict = pathlib.Path("assets/data/zones/")

if save_file.exists():
    save_file.unlink()

for file in zone_dict.rglob("*"):
    file.unlink()
zone_dict.rmdir()

print("Game save files deleted")
