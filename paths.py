from typing import List
from os import listdir


kth_path = r"F:\Session_5\Vision_artificielle_reconnaissance\Support\FiveProject_CBIR\DataSets\kth_tips2/"
kth_dir:List[str] = listdir(kth_path)

data_base_feachures_paht = r"F:\Session_5\Vision_artificielle_reconnaissance\Support\FiveProject_CBIR\Data_Base_Feachures/"
data_base_feachures_dir:List[str] = listdir(data_base_feachures_paht)
print(data_base_feachures_dir)
