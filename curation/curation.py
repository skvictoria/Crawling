import os
import shutil
import csv
import natsort

DEFAULT_NUM = 9999

def curation(strInlist, strOutlist, start_frame_num=DEFAULT_NUM, end_frame_num=DEFAULT_NUM, frame_rate=20):
  if not os.path.isdir(strInlist):
    print(strInlist, "return cause is not a folder")
    return
  if not os.path.isdir(strOutlist):
    os.makedirs(strOutlist)
  m_start_frame_num = 0
  m_end_frame_num = len(os.listdir(strInlist)) - 1
  
  if(start_frame_num != DEFAULT_NUM):
    m_start_frame_num = start_frame_num
  if(end_frame_num != DEFAULT_NUM):
    m_end_frame_num = end_frame_num
    
  idx = -1
  for files in natsort.natsorted(os.listdir(strInlist)):
    idx += 1
    if(idx < m_start_frame_num):
      continue
    if(idx > m_end_frame_num):
      continue
    if(idx % frame_rate != 0):
      continue
    
    input_path = os.path.join(strInlist, files)
    dest_path = os.path.join(strOutlist, files)
    shutil.copyfile(input_path, dest_path)
    
  print(strInlist, "curated at frame rate", frame_rate, "from", m_start_frame_num, "to", m_end_frame_num, "saved at ", strOutlist)
  
def parse_frame_info(dirs, info):
  pass
  
if __name__ == '__main__':
  pass
