
## Django Admin 模块

**使用Django模块的事项：**  
1.*setting.py* 的INSTALLED_APPS中添加`django.contrib.admin`,依赖的还有`django.contrib.auth`,`django.contrib.contenttypes`,`django.contrib.messages`和`django.contrib.sessions`  
2.在TEMPLATE_CONTEXT_PROCESSORS添加：`django.contrib.messages.context_processors.messsags`  
3.MIDDLEWARE_CLASS中添加：`django.contrib.auth.middleware.AuthenticateionMiddleware`和`django.contrib.messages.middleware.MessageMiddleware`
