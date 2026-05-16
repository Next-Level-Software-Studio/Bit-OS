from pathlib import Path
systemfolder = Path("/System")
usersfolder = Path("/Users")
logfile = systemfolder / "var" / "log" / "IntegrityCheck.log"
systemfolder.mkdir(parents=True, exist_ok=True)
usersfolder.mkdir(parents=True, exist_ok=True)
logfile.touch(exist_ok=True)