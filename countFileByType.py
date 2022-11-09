#count files of every types in the given folder

def count_file_bytype(work_dir):
    result = {}
    import glob
    import os
    for fil in glob.glob(work_dir+'/**',recursive=True):
        file_extension = os.path.splitext(fil)[1]
        if file_extension in result.keys():
            result[file_extension] += 1
        else:
            result[file_extension] = 1

    result = sorted(result.items(),key= lambda x: x[1], reverse=True)
    for item in result:
        if item[1]>5: #only print file types more than 5 files
            print(item)

if __name__ == '__main__':
    count_file_bytype(r'C:\SVN')
