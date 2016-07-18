# -*- coding: utf-8 -*-
#
#  db.py
#  
#  Copyright 2016 wanxu <wanxu_pursue@163.com>
#  
#  
'''
设计db接口

设计底层模块的原则是，根据上层调用者设计简单易用的API接口，然后，实现模块内部代码。

假设transwarp.db模块已经编写完毕，我们希望以这样的方式来调用它：

首先，初始化数据库连接信息，通过create_engine()函数：

from transwarp import db
db.create_engine(user='root', password='password', database='test', host='127.0.0.1', port=3306)
然后，就可以直接操作SQL了。

如果需要做一个查询，可以直接调用select()方法，返回的是list，每一个元素是用dict表示的对应的行：

users = db.select('select * from user')
# users =>
# [
#     { "id": 1, "name": "Michael"},
#     { "id": 2, "name": "Bob"},
#     { "id": 3, "name": "Adam"}
# ]
如果要执行INSERT、UPDATE或DELETE操作，执行update()方法，返回受影响的行数：

n = db.update('insert into user(id, name) values(?, ?)', 4, 'Jack')
update()函数签名为：

update(sql, *args)
统一用?作为占位符，并传入可变参数来绑定，从根本上避免SQL注入攻击。

每个select()或update()调用，都隐含地自动打开并关闭了数据库连接，这样，上层调用者就完全不必关心数据库底层连接。

但是，如果要在一个数据库连接里执行多个SQL语句怎么办？我们用一个with语句实现：

with db.connection():
    db.select('...')
    db.update('...')
    db.update('...')
如果要在一个数据库事务中执行多个SQL语句怎么办？我们还是用一个with语句实现：

with db.transaction():
    db.select('...')
    db.update('...')
    db.update('...')
'''

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
