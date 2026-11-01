BẬT NÃO GIẢI MÃ MEKONG! – BẢN SẴN SÀNG ĐƯA LÊN RENDER

Các tệp cần có trong GitHub repository:
- app.py
- requirements.txt

Thiết lập trên Render:
- New + > Web Service
- Connect repository chứa hai tệp trên
- Language: Python 3
- Build Command: pip install -r requirements.txt
- Start Command: gunicorn app:app
- Instance Type: Free

Sau khi deploy thành công, Render cấp một địa chỉ dạng https://ten-website.onrender.com.
Lưu ý: gói miễn phí có thể tự tạm dừng sau 15 phút không có lượt truy cập; lượt mở lại đầu tiên có thể mất khoảng một phút.
