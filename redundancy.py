import shutil
import time
import os
i=0
threshold_time=1800
while True:
    i=i+1
    print("Starting Backup copy #",i)
    if os.name == 'nt':
        path_original_brb=r"RESULTS\RESULTS_COL.csv"
        path_backup_brb=r"BACKUP\RESULTS_COL_"+(str(i))+"_.csv"
        path_original_usa=r"RESULTS\RESULTS_NL.csv"
        path_backup_usa=r"BACKUP\RESULTS_NL_"+(str(i))+"_.csv"
    else:
        path_original_brb=r"RESULTS/RESULTS_COL.csv"
        path_backup_brb=r"BACKUP/RESULTS_COL_"+(str(i))+"_.csv"
        path_original_usa=r"RESULTS/RESULTS_NL.csv"
        path_backup_usa=r"BACKUP/RESULTS_NL_"+(str(i))+"_.csv"
    shutil.copyfile(path_original_brb,path_backup_brb)
    shutil.copyfile(path_original_usa,path_backup_usa)
    print("Backup copy #",i)
    print("Done")
    time.sleep(threshold_time)
