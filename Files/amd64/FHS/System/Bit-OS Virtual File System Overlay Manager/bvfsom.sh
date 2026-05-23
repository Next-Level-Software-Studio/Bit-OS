sudo mkdir -p "/System/Bit-OS Virtual File System Overlay Manager/Overlay"
sudo python3 "/System/Bit-OS Virtual File System Overlay Manager/fuse.py" "/System/Bit-OS Virtual File System Overlay Manager/Overlay" &
sleep 1
sudo unshare --mount --pid --fork sh -c "mount --make-rslave / && chroot '/System/Bit-OS Virtual File System Overlay Manager/Overlay' /bin/bash"