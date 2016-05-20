"""Contains logic for usb flash drive detection (memssd) and trasfer of media from memssd"""

import os
import sys
import shutil
import subprocess
import tarfile
import gzip

# Base dirs for non-drm(mlbam) vods.
base_nvod_dir = '/opt/portal/vendors/mlbam/vchunks/vod'
base_alt_nvod_dir = '/mnt/media_a/mlbam_vchunks/vod'

# base directories for HLS non-DRM VODs
base_hvod_dir = '/opt/portal/media/hls/vod/assets'
base_alt_hvod_dir = '/mnt/media_a/hls_vod'

# base directores for Widevine DRM VODs
base_wvod_dir = '/opt/portal/vendors/widevine/assets'
base_alt_wvod_dir = '/mnt/media_a/wv_vod/assets'

# ereader paths
ereader_package_dir = '/mnt/media_a/ereader'
ereader_meta_dir = '/opt/portal'
ereader_vendor_path = '/opt/portal/vendors/ereader'
ebook_meta_path = '/opt/portal/ebook_meta'

def is_memssd_mounted():
    memssd_mnt = '/mnt/memssd_media'

    if os.path.ismount(memssd_mnt):
        check_memssd_asset_version(memssd_mnt)
    else:
        print('Media USB (memssd_media) was not detected or mounted at /mnt/memssd_media') #is_memssd_mounted()

def check_memssd_asset_version(memssd_mnt):
    for dirpath, dirs, files in os.walk(memssd_mnt, followlinks=True):
        for dirname in dirs:
            tar_subdir = os.path.join(dirpath, dirname)
            for filename in os.listdir(dirpath):
                tar_file = os.path.join(dirpath, filename)
                print(tar_file)
                if 'tgz' in tar_file:
                    tgz_file = tarfile.open(tar_file, 'r')
                    for tgzinfo in tgz_file:
                        print(tgzinfo.name)
                        if 'asset_version' in tgzinfo.name:
                            asset_version = tgzinfo.name
                            f = tgz_file.extractfile(asset_version)
                            lines = f.readlines()
                            tgz_asset_version = lines[0].strip()
                            tgz_tid  = lines[1].strip()[3:]
                            tgz_cid = lines[2].strip()
                            print(tgz_asset_version, tgz_tid, tgz_cid)
                            if 'wv' in tar_file:
                                drm_dup = os.path.join(base_wvod_dir, tgz_cid)
                                print(drm_dup)
                                if os.path.exists(drm_dup):
                                    print('DRM asset already installed')
                                    break
                            if 'nondrm' in tar_file:
                                nondrm_dup = os.path.join(base_nvod_dir, tgz_cid)
                                print(nondrm_dup)
                                if os.path.exists(nondrm_dup):
                                    print('NonDRM asset already installed')
                                    break
                        if 'md5' in tgzinfo.name:
                            md5_sig = tgzinfo.name
                            check_memssd_md5_signature(tar_file, md5_sig)


def check_memssd_md5_signature(tar_file, md5_sig):
    print(tar_file, md5_sig)
    tgz_file = tarfile.open(tar_file, 'r')
    f = tgz_file.extractfile(md5_sig)
    lines = f.readlines()
    if lines =
    print(lines)
    print('check md5')
    #check md5 signature
    copy_memssd_content(tar_file)

def copy_memssd_content(tar_file):
    install_dir = '/opt/maint/releases'
    print('copy content')
    shutil.copy(tar_file, install_dir)

is_memssd_mounted()
