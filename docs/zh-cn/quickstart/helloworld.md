
# 简单示例

model.py
```python

from peewee import *
from playhouse.db_url import connect

db = connect("sqlite:///database.db")

class Topic(Model):
    title = CharField(index=True, max_length=255)
    time = BigIntegerField(index=True)
    content = TextField()

    class Meta:
        database = db

db.connect()
db.create_tables([Topic], safe=True)
```

app.py
```python
from slim.support.peewee import PeeweeView
from slim.base.helper import Route

route = Route()

@route('topic')
class TopicView(PeeweeView):
    model = Topic

app = app_init(b'cookies secret', enable_log=True, route=route)
web.run_app(app, host='0.0.0.0', port=9999)
```

```shell
python app.py
======== Running on http://0.0.0.0:9999 ========
(Press CTRL+C to quit)
```

此时有以下接口可用

```
[GET]/api/topic/get
[GET]/api/topic/list/{page}
[GET]/api/topic/list/{page}/{size}
[POST]/api/topic/set
[POST]/api/topic/new
[POST]/api/topic/delete
```