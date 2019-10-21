# Hướng dẫn sử dụng script

### 1. Clone repo về và cài các gói cần thiết

```
git clone https://github.com/nhanhoadocs/bot_telegram.git
cd bot_telegram/new_post
sudo pip3 install -r requirements.txt
```

### 2. Setup mysql

Tạo 1 database

```
mysql -u root -p
create database new_post;
use new_post;
create table do(id char(10) not null);
create table new(id char(10) not null);
grant all privileges on new_post.* to 'new_post'@'%' identified by 'your_password';
```

### 3. Sửa file setting

Khai báo thông tin cần thiết trong file `setting`

```
vi setting
```

Thay đổi xong thì lưu lại file

### 6. Chạy chương trình

```
python3 main.py
```

Để chương trình chạy thường xuyên thì cho nó vào crontab

```
echo "*/5 * * * * root path_to_file_main.py" >> /etc/crontab
```