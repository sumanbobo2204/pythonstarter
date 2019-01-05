import glob, os
parent_dir = r"G:\Wedding_Pics\Taniya and Patla Potty\Wedding"

replace_string='G:\Wedding_Pics\Taniya and Patla Potty\Wedding\\'
rpl = 'DSC_'
rpl2 = '.JPG'
rpl3 = 'WG'

for img_file in glob.glob(os.path.join(parent_dir, '*.JPG')):
    print(img_file.replace(replace_string, '').replace(rpl, '').replace(rpl2, '').replace(rpl3, ''))


