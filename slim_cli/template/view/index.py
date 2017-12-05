from slim.base.view import BaseView
from slim.retcode import RETCODE
from view import route


@route('/misc')
class TestBaseView(BaseView):
    @classmethod
    def interface(cls):
        cls.use('info', 'GET')

    async def info(self):
        self.finish(RETCODE.SUCCESS, {
            'retcode': list(RETCODE.items()),
            #'retinfo': RETCODE.txt,
        })