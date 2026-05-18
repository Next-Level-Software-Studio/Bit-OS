#Adding services to the default runlevel to ensure they start on boot
rc-update add sddm default
rc-update add local default

sudo env-update #Updating the environment variables
source /etc/profile #sourcing the profile to apply changes