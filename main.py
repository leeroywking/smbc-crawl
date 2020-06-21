from smbc_crawl.quests import grab_n_comics_from_start
import os
import shutil

if __name__ == "__main__":
    if shutil.which("wget") is not None:
        grab_n_comics_from_start(10)
        from smbc_crawl.parselist import listify_downloads

        listify_downloads()
        os.system("wget -i ./list_of_images.txt -P ./images")

