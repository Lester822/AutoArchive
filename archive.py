from directory import Active_Directory
import os
import datetime
import shutil

active_paths = [Active_Directory("C:\Michael\FilesTest", "E:\TestArchive")]

old_time = 120  # in seconds

def main():
    for active_dir in active_paths:
        for file in active_dir.files():
            edit_time = (os.path.getmtime(f"{active_dir.path()}\\{file}"))
            time_since_edit = datetime.datetime.now().timestamp() - edit_time
            if time_since_edit >= old_time:
                print(f"MOVING {active_dir.path()}\\{file} to ARCHIVE (TIME SINCE EDIT: {time_since_edit} SECONDS)")
                try:
                    shutil.move(f"{active_dir.path()}\\{file}", active_dir.archive_path())
                except:
                    print("FILE ALREADY IN DESTINATION. SKIPPING.")


if __name__ == '__main__':
    main()