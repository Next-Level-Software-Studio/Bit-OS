#!/usr/bin/env python3

# Aviso ao usuário
# Este script gerencia grande parte do Bit-OS, mudar isto provavemente vai quebrar tudo.

import pyfuse3

class bvfso(pyfuse3.Operations):
    def getattr(self, inode, ctx):
        return super().getattr(inode, ctx)
    def readdir(self, fh, start_id, token):
        return super().readdir(fh, start_id, token)
    def access(self, inode, mode, ctx):
        return super().access(inode, mode, ctx)
    def open(self, inode, flags, ctx):
        return super().open(inode, flags, ctx)
    def create(self, parent_inode, name, mode, flags, ctx):
        return super().create(parent_inode, name, mode, flags, ctx)
    def read(self, fh, off, size):
        return super().read(fh, off, size)
    def write(self, fh, off, buf):
        return super().write(fh, off, buf)
    def flush(self, fh):
        return super().flush(fh)
    def release(self, fh):
        return super().release(fh)
    def mkdir(self, parent_inode, name, mode, ctx):
        return super().mkdir(parent_inode, name, mode, ctx)
    def rmdir(self, parent_inode, name, ctx):
        return super().rmdir(parent_inode, name, ctx)
    def unlink(self, parent_inode, name, ctx):
        return super().unlink(parent_inode, name, ctx)
    def rename(self, parent_inode_old, name_old, parent_inode_new, name_new, flags, ctx):
        return super().rename(parent_inode_old, name_old, parent_inode_new, name_new, flags, ctx)
    def symlink(self, parent_inode, name, target, ctx):
        return super().symlink(parent_inode, name, target, ctx)
    def readlink(self, inode, ctx):
        return super().readlink(inode, ctx)
    def statfs(self, ctx):
        return super().statfs(ctx)
    def fsync(self, fh, datasync):
        return super().fsync(fh, datasync)
    def mknod(self, parent_inode, name, mode, rdev, ctx):
        return super().mknod(parent_inode, name, mode, rdev, ctx)
    def init(self):
        return super().init()
if __name__ == "__main__":
    