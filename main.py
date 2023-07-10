from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    def __get_html_content(self):
        return """
        <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
  integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css">
  <title>Контакты</title>
  <style>
    .sidebar {
      background-color: #040026;
      color: #fff;
      height: 100vh;
      padding: 20px;
      width: 400px;
    }

    .content {
      padding: 70px;
      margin-top: 250px;
      text-align: center;
    }

    .product {
      border: 1px  solid #000000;
      border-radius: 5px;
      padding: 20px;
      margin-bottom: 20px;
    }

    .contacts{
      padding: 70px;
      margin-top: 250px;
      text-align: center;
    }


  </style>
</head>
<body>
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-3 sidebar" height="100px">
        <ul class="nav flex-column">
          <li class="nav-item">
            <a class="nav-link active" href="index.html">Главная</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Категории</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Заказы</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="contact.html">Контакты</a>
          </li>
        </ul>
        
        <div class="btn-group" style="margin-top: 75vh">
          <a class="btn btn-secondary dropdown-toggle " href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Пользователь</a>
        </div>


        <!-- Example single danger button -->
      </div>
      <div class="col-sm-9 contacts">
        <div class="input-group mb-3">
          <input type="text" class="form-control" placeholder="Имя" aria-label="Username" aria-describedby="basic-addon1">
        </div>
        
        <div class="input-group mb-3">
          <span class="input-group-text" id="basic-addon2">@</span>
          <input type="text" class="form-control" placeholder="Почта" aria-label="Recipient's username" aria-describedby="basic-addon2">
        </div>
    
        
        <div class="input-group">
          <span class="input-group-text">Сообщение</span>
          <textarea class="form-control" aria-label="Сообщение"></textarea>
        </div>
        <style type="text/css"> 
          button[name="run_script"] { 
            margin-top: 10px;
            border: none;
            border-radius: 7px;
            padding: 10px 25px;
            background: #00033f;
            cursor: pointer;
            text-transform: uppercase;
            font-weight: bold;
            color: white;
          }
          button[name="run_script"]:hover { 
            background: #c70000;
          } 
        </style>
        <button type="button" name="run_script">Отправить</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  
  

  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.1/umd/popper.min.js"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
        """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        page_content = self.__get_html_content()
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
