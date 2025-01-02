[root@VM_0_10_centos shellScript]# cat modifyExtension.sh 
#!/bin/bash
# 编写批量修改扩展名脚本,如批量将 txt 文件修改为 doc 文件 
# 执行脚本时,需要给脚本添加位置参数
# 脚本名  txt  doc(可以将 txt 的扩展名修改为 doc)
if [ $# -eq 0 -o $# -eq 1 ];then
    echo "[usage]: ./modifyExtension.sh 需修改的扩展名 修改之后的扩展名"
    exit 0
fi
for i in `ls *.$1`
do
    # ${i%}用法参考：https://blog.csdn.net/lihonghai2392/article/details/77868445
    # ${var%} 删除变量尾部的字符(串)。"%"后可是字符串也可以使用正则匹配。${i%.*}即删除变量i后面的字符串
    mv "$i" "${i%.*}.$2"
done
echo "修改成功！"
