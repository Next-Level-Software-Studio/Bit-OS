import subprocess, portage, re; from pathlib import Path
makeconfigurations = Path("/etc/portage/make.conf")
package = "app-portage/cpuid2cpuflags"
vdb = portage.db[portage.root]["vartree"].dbapi
if "/" in package and vdb.match(package):
    pass
else:
    subprocess.run(["emerge", package, "--quiet-build", ""])
comand = subprocess.run(["cpuid2cpuflags"], capture_output=True, text=True, check=True)
flags = comand.stdout.strip().replace(": ", '="') + '"'
with open(makeconfigurations, "a") as f:
    f.write(flags)