"""
pip的常用命令:
安装包
    pip install 包名  # 最新版本
    pip install 包名==1.0.4   # 指定版本
    pip install '包名>=1.0.4' # 最小版本
升级包
    pip install --upgrade 包名
    pip install -U 包名
卸载包
    pip uninstall 包名
搜索包
    pip search 包名
列出已安装的包
    pip list

pip源的修改:
临时镜像:
    指定镜像下载包: pip install 包名 -i 镜像地址, 即在指令中添加-i 网址即可, 例如:
        pip install numpy -i https://mirrors.aliyun.com/pypi/simple/
    常见镜像有：
        镜像名称	        网址
        阿里云	        https://mirrors.aliyun.com/pypi/simple/
        豆瓣	            https://pypi.douban.com/simple/
        清华大学(推荐)	https://pypi.tuna.tsinghua.edu.cn/simple/
        中国科学技术大学	http://pypi.mirrors.ustc.edu.cn/simple/
        华中理工大学	    http://pypi.hustunique.com/
        山东理工大学	    http://pypi.sdutlinux.org/

永久镜像:
    自己添加配置文件
        在'C:\Users\用户名'的目录下解压配置文件，或者在该文件夹下创建一个pip的文件夹，
        在文件内创建一个名为pip.ini的文件，在里面配置镜像内容
    配置文件如下：
        [global]
        index-url = https://pypi.tuna.tsinghua.edu.cn/simple
        [install]
        trusted-host = pypi.tuna.tsinghua.edu.cn
    指令生成:
        在cmd窗口直接输入如下指令生成配置文件:
            pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

"""
