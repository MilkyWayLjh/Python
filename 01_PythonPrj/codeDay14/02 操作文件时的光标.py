"""
模式	        r	    r+	    w	    w+	    a	    a+
读	        +	    +	    	    +	    	    +
写	        	    +	    +	    +	    +	    +
创建			                +	    +	    +	    +
覆盖			                +	    +
指针在开始	+	    +	    +	    +
指针在结尾		    	    	    	    +	    +

注意：当在一个文件中同时操作时，不管读 写 追加，都是在文本的末尾。所以在w+，a+的时候先写后读，总是读不到全部，因为光标在末尾。
"""
# 打开文件-w
f = open('resource/demo.txt', 'w+', encoding='utf8')
# 写入内容
f.write('你好 job1')
f.write('good job2')
f.write('good job3')

# 移动光标：参数是 距离文本开头的字节数，一般写0表示从开头开始
f.seek(0)

# 读取文件
content = f.read()
# 关闭文件
f.close()

print(content)
