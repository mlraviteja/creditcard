import logging
import os 

from datetime import datetime 

# creating file name for log file based on current time stamp

log_dir="logs"
log_dir=os.path.join(os.getcwd(),log_dir)

# lets design our logger file 


# creating log_dir if it does not exist 

os.makedirs(log_dir,exist_ok=True)



# creating file name for log file based on 



current_time_stamp=f"{datetime.now().strftime('%y-%m-%d-%H-%M-%S')}"
file_name = f"log _{current_time_stamp}.log"


# creating file path for projects 

log_file_path=os.path.join(log_dir,file_name)


logging.basicConfig(filename=log_file_path,
                    filemode='w',
                    format=['%(asctime)s %(name)s -%(levelname)s -%(message)s'],
                    level=logging.INFO)

