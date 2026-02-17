from injector import Injector
from internal.router import Router
from internal.server import Http
from config import Config
import dotenv

# 将.env加载环境变量中
dotenv.load_dotenv()

injector = Injector()

conf = Config()


app = Http(__name__, config=conf, router=injector.get(Router))

if __name__ == '__main__':
    app.run(debug=True)


