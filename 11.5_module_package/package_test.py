import test_package.say_goodbye, test_package.say_hello
from test_package import say_goodbye, say_hello

test_package.say_hello.hello()

test_package.say_goodbye.goodbye()

say_hello.hello()
say_goodbye.goodbye()
