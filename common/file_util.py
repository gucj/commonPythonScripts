# coding=utf-8
__author__ = 'gucuijuan'
import os


file_list = []


def find_files_in_dir(search_name, dir_path):
    """
    find files which filename contains search_name in dir_path.
    :param search_name:String
    :param dir_path:String of path
    :return:
    """

    dir_path = os.path.abspath(dir_path)
    if os.path.exists(dir_path)and os.path.isdir(dir_path):
        for line in os.listdir(dir_path):
            if os.path.isdir(line):
                find_files_in_dir(search_name, line)
            else:
                current_file_name = os.path.split(line)[1]
                if current_file_name.__contains__(search_name):
                    file_list.append(os.path.abspath(current_file_name))


def read_file(file_name):
    """
     read file and return list of file content.
     :type file_name: str
     :return:list of file content
     """
    with open(file_name, 'rb') as f:
        file_content = f.readlines()
        return file_content


def write_bytes_to_file(file_name, write_content):
    """
     write bytes to file.if file not exists,new file then  write.
     :type file_name:str
     :type write_content:bytes | bytearray
     :return:
     """
    with open(file_name, "w") as f:
        f.write(write_content)

def write_list_to_file(file_name, write_content):
    """
     write list of str to file.if file not exists,new file then  write.
     :type file_name:str
     :type write_content:list of str
     :return:
     """
    with open(file_name, "w") as f:
        f.writelines(write_content)


def append_bytes_to_file(file_name, write_content):
    """
     append bytes to file.if file not exists,new file then write.
     :type file_name:str
     :type write_content:bytes | bytearray
     :return:
     """
    with open(file_name, "a") as f:
        f.write(write_content)


def append_list_to_file(file_name, write_content):
    """
     append list of str to file.if file not exists,new file then  write.
     :param file_name:str
     :type write_content:list of str
     :return:
     """
    with open(file_name, "a") as f:
        f.writelines(write_content)


def make_dir(dir_name):
    """
    make direction
    :param dir_name:
    :type dir_name:str
    :return:
    """
    os.mkdir(dir_name)


def rm_dir(dir_name):
    """
    remove direction
    :param dir_name:
    :type dir_name:str
    :return:
    """
    os.rmdir(dir_name)


def split_path(path):
    """
    split path to two.
    :param path:
    :type path:str
    :return:tuple of (str,str)
    """
    return os.path.split(path)


def rename_file_or_dir(old_name,new_name):
    """
    rename file or dir.
    :param old_name:
    :type old_name:str
    :param new_name:
    :type new_name:str
    :return:
    """
    os.rename(old_name,new_name)


def remove_file(file_name):
    """
    remove file
    :param file_name:
    :type file_name:str
    :return:
    """
    os.remove(file_name)

# os.path.abspath('.')  #获取当前目录的绝对路径
# os.path.join(path1,path2) #合并2个路径
# os.path.splitext(path) # 获取文件的扩展名
# os.chdir()  #Change the current working directory to the specified path.
# os.listdir(dir)  #列出目录下的子文件和目录