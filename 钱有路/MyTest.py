import nose
import linecache
from 钱有路 import Post_tools
from nose.tools import *

def my_setup_function():
    global my_post
    my_post = Post_tools.MYPost(config_file_path='config.ini')


# /appfrontservice/app/token/getToke 获取Token
@with_setup(my_setup_function)
def test_token():
