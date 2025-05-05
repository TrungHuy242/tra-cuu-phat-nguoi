import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image, ImageEnhance
import pytesseract
import os

def tra_cuu_phat_nguoi():
    success = False  

    while not success:  
        driver = webdriver.Chrome()
        driver.get('https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html')

        try:
            # Chọn loại phương tiện
            element_loai_phuong_tien = driver.find_element(By.NAME, 'LoaiXe')
            element_loai_phuong_tien.send_keys("Xe máy")

            # Nhập biển số xe
            element_bien_so = driver.find_element(By.NAME, 'BienKiemSoat')
            txt_bien_so = '99D146675'
            element_bien_so.send_keys(txt_bien_so)

            # Tự động đọc mã bảo mật (captcha)
            captcha_img = driver.find_element(By.ID, 'imgCaptcha')
            captcha_img.screenshot('captcha.png')

            captcha_image = Image.open('captcha.png')
            captcha_image = captcha_image.convert('L')
            enhancer = ImageEnhance.Contrast(captcha_image)
            captcha_image = enhancer.enhance(2)

            captcha_code = pytesseract.image_to_string(captcha_image, config='--psm 6').strip()
            print("Mã captcha đọc được:", captcha_code)

            element_captcha = driver.find_element(By.NAME, 'txt_captcha')
            element_captcha.send_keys(captcha_code)

            # Nhấn nút "Tra cứu"
            element_btn = driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/input[1]')
            element_btn.click()

           
            time.sleep(5)

            # Check lỗi Captcha
            try:
                error_div = driver.find_element(By.CLASS_NAME, 'xe_texterror')
                error_text = error_div.text.strip()
                if "Mã xác nhận sai" in error_text:
                    print("Mã xác nhận sai! Restart lại quy trình...")
                    driver.quit()
                    if os.path.exists('captcha.png'):
                        os.remove('captcha.png')
                    continue  
            except:
                print("Không có lỗi captcha, tiếp tục...")

            # Kiểm tra kết quả phạt nguội
            result_table = driver.find_element(By.ID, 'bodyPrint123')
            result_text = result_table.text.strip()

            if "Không tìm thấy kết quả" in result_text:
                print("Không tìm thấy vi phạm phạt nguội!")
                success = True  
            elif result_text == "":
                print("Không có nội dung trả về, cần kiểm tra lại.")
                success = False  
            else:
                print("Tìm thấy vi phạm phạt nguội!")
                print(result_text)
                success = True  

            print("Tiêu đề trang:", driver.title)

        except Exception as e:
            print("Có lỗi xảy ra:", e)

        finally:
            if os.path.exists('captcha.png'):
                os.remove('captcha.png')
            driver.quit()

schedule.every().day.at("06:00").do(tra_cuu_phat_nguoi)
schedule.every().day.at("12:00").do(tra_cuu_phat_nguoi)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
