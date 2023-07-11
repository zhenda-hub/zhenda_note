import django
from django.conf import settings as st
from zd_note import settings


if __name__ == '__main__':
    st.configure(default_settings=settings, DEBUG=True)
    django.setup()

# 现在可以访问Django项目内部的模块了
# from myapp import models