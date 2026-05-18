from pathlib import Path
from datetime import datetime, timezone
systemfolder = Path("/System")
usersfolder = Path("/Users")
logfile = systemfolder / "var" / "log" / "IntegrityCheck.jonl.log"

def log(msg):
    with open(logfile, "a") as f:
        f.write(str(msg))

if systemfolder.exists() is False:
    systemfolder.mkdir()
    log(r"{timestamp:}")
if usersfolder.exists() is False:
    usersfolder.mkdir()
if logfile.exists() is False:
    logfile.touch()
print(datetime.now(timezone.utc).strftime("%d/%m/%Y %H:%M:%S"))