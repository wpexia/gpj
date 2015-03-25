# Scrapy settings for gpj_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'gpj'

SPIDER_MODULES = ['gpj.spiders']
NEWSPIDER_MODULE = 'gpj.spiders'
def setup_django_environment(path):
    import imp, os, sys
    from django.core.management import setup_environ
    m = imp.load_module('settings', *imp.find_module('settings', [path]))
    setup_environ(m)
    sys.path.append(os.path.abspath(os.path.join(path, os.path.pardir)))

setup_django_environment("C:/work/work/gpj/gpj/gpjweb/gpjweb")

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gpj (+http://www.yourdomain.com)'
