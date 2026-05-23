sudo mkdir -p "/System/Bit-OS Virtual File System Overlay Manager/Overlay"
sudo system-python "/System/Bit-OS Virtual File System Overlay Manager/fuse.py" "/System/Bit-OS Virtual File System Overlay Manager/Overlay"
sudo unshare --mount --pid --net --fork /bin/bash
mount --make-rslave /
chroot "/System/Bit-OS Virtual File System Overlay Manager/Overlay" /bin/bash