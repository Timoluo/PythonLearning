
### 安装第三方模块

## 通过包管理工具pip完成

pip install Pillow  #安装图像处理库 Pillow

# Anaconda，这是一个基于Python的数据处理和科学计算平台，已经内置了许多非常有用的第三方库

## 模块搜索路径

# 默认情况下，Python解释器会搜索当前目录、
# 所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中

## 若要自己添加，有两种方法：
#  1. sys.path.append(‘’)   运行时修改，运行结束后失效
#  2. 设置环境变量PYTHONPATH  与设置Path类似，Python本身搜索路径不被影响



## 引入第三方模块时python解释器的查找机制：

# 1.默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，
# 搜索路径存放在sys模块的path变量中：
import sys
sys.path
#['C:\\Users\\acer1\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip C:\\Users\\acer1\\AppData\\Local\\Programs\\Python\\Python36\\DLLs',
#    'C:\\Users\\acer1\\AppData\\Local\\Programs\\Python\\Python36\\lib',
#    'C:\\Users\\acer1\\AppData\\Local\\Programs\\Python\\Python36']

# 2.添加自己的搜索目录
import sys
sys.path.append( 'C:/Users/acer1/Desktop' )
# 注：
## 1.即使输入无效的 自定义搜索目录，也不会报错
#    相应的只是import模块的时候会找不到
## 2.这种方法是在运行时修改，运行结束后失效。
#    e.g. append操作后重新sys.path命令 发现搜索目录中已加入了自己添加的路径，
#    重启交互界面后失效

