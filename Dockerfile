# Sử dụng image cơ sở
FROM python:3.12

# Đặt thư mục làm việc trong container
WORKDIR D:\Ky1-Nam3-IT-PTIT\Tu_Hoc_Python\Web\backend\Ecommerce_web_selling_book_backend

# Sao chép Pipfile và Pipfile.lock vào container
COPY Pipfile Pipfile.lock /Ecommerce_web_selling_book_backend/
# Sao chép thư mục src vào container
COPY src /Ecommerce_web_selling_book_backend/src
# Cài đặt Pipenv
RUN pip install pipenv

# Cài đặt các phụ thuộc từ Pipfile.lock
RUN pipenv install --deploy --ignore-pipfile

# Sao chép mã nguồn vào container
COPY . /app

# Chạy ứng dụng khi container khởi động
CMD ["pipenv", "run", "python", "src/app.py"]
