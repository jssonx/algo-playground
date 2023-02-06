import shutil
import os

# src_folder = os.path.expanduser("~/.lc/leetcode/cache/")
# dst_folder = './lc_cache/'

dst_folder = os.path.expanduser("~/.lc/leetcode/cache/")
src_folder = '../lc_cache/'

if os.path.exists(dst_folder):
    shutil.rmtree(dst_folder)
shutil.copytree(src_folder, dst_folder)