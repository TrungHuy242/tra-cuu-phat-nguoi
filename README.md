# Tra Cứu Phạt Nguội

Đây là script tự động tra cứu phạt nguội trên website https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.htm.

## Yêu cầu
- Máy tính cài đặt Python (phiên bản 3.6 trở lên).
- Trình duyệt Google Chrome.
- ChromeDriver (phiên bản tương thích với Chrome).
- Tesseract-OCR (để đọc mã bảo mật captcha).

## Hướng dẫn cài đặt
1. **Tải ChromeDriver**:
   - Truy cập https://chromedriver.chromium.org/downloads.
   - Tải ChromeDriver phù hợp với phiên bản Chrome trên máy của bạn.
   - Giải nén và copy file `chromedriver.exe` vào thư mục chứa file `tra_cuu_phat_nguoi.py`.

2. **Cài đặt Tesseract-OCR**:
   - Truy cập https://github.com/UB-Mannheim/tesseract/wiki.
   - Tải và cài đặt Tesseract-OCR (VD: `tesseract-ocr-w64-setup-v5.3.0.20221214.exe`).
   - Thêm Tesseract-OCR vào PATH:
     - Nhấn Windows + R, gõ `sysdm.cpl`, nhấn Enter.
     - Vào tab Advanced → Environment Variables.
     - Trong System Variables, tìm Path, nhấn Edit.
     - Thêm `C:\Program Files\Tesseract-OCR`.
     - Nhấn OK để lưu.

3. **Cài đặt Python**:
   - Tải Python từ https://www.python.org/downloads/.
   - Cài đặt và đảm bảo thêm Python vào PATH.

4. **Cài đặt thư viện**:
   - Mở Command Prompt hoặc PowerShell.
   - Di chuyển đến thư mục chứa project:
     ```
     cd D:\TuDongHoaQuyTrinh\Buoi6
     ```
   - Cài đặt các thư viện:
     ```
     pip install -r requirements.txt
     ```

5. **Chỉnh sửa biển số xe**:
   - Mở file `tra_cuu_phat_nguoi.py`.
   - Tìm dòng:
     ```
     txt_bien_so = '74D1-38450'
     ```
   - Thay `74D1-38450` bằng biển số xe của bạn.

## Cách chạy
1. Di chuyển đến thư mục project:
cd D:\TuDongHoaQuyTrinh\DoAn

2. Chạy script:
  python tra_cuu_phat_nguoi.py

3. Script sẽ tự động chạy lúc 6h sáng và 12h trưa mỗi ngày. Kết quả sẽ được in ra terminal:
- Nếu có vi phạm: In thông tin vi phạm (thời gian, địa điểm, hành vi vi phạm, v.v.).
- Nếu không có vi phạm: In "Không tìm thấy vi phạm phạt nguội!".

## Cấu trúc file
- `tra_cuu_phat_nguoi.py`: Script chính để tra cứu phạt nguội.
- `requirements.txt`: Danh sách các thư viện cần thiết.
- `README.md`: File mô tả dự án (file này).

## Lưu ý
- Script sử dụng `pytesseract` để đọc mã captcha, nhưng có thể không đọc chính xác do nhiễu trên hình ảnh captcha.
- Nếu captcha sai, script sẽ tự động thử lại cho đến khi thành công.
- Đảm bảo Chrome và ChromeDriver cùng phiên bản để tránh lỗi.
- Đảm bảo kết nối Internet ổn định khi chạy script.

