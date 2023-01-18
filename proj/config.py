# База данных
SQLALCHEMY_DATABASE_URI = 'postgresql://administrator:74La_23jlda**3_Tppq@127.0.0.1:5432/kolpakovka'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Скеретный ключ
SECRET_KEY = 'secret_key'

# Файлы
UPLOAD_FOLDER = 'static/imgs/upload'
MAX_CONTENT_LENGHT = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'webp'])