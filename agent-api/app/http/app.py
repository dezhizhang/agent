from injector import Injector
from internal.router import Router
from internal.server import Http

import dotenv

# 将.env加载环境变量中
dotenv.load_dotenv()

injector = Injector()


app = Http(__name__,router=injector.get(Router))


if __name__ == '__main__':
    app.run(debug=True)


