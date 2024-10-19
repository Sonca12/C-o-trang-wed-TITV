from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Đường dẫn tới geckodriver
gecko_path = r"C:\Users\HP\Downloads\geckodriver-v0.35.0-win64\geckodriver.exe"

# Thiết lập service cho geckodriver
service = Service(gecko_path)

# Tạo một instance của Firefox
driver = webdriver.Firefox(service=service)

# Mở trang web
driver.get("https://titv.vn/")

# Đợi trang tải hoàn toàn
time.sleep(5)

# Lặp qua từng data-id từ 75 đến 81
for data_id in range(75, 82):
    # Tìm phần tử với data-id cụ thể
    li_element = driver.find_element(By.CSS_SELECTOR, f'span[data-id="{data_id}"]')

    # Cuộn đến phần tử
    driver.execute_script("arguments[0].scrollIntoView();", li_element)

    # Chờ cho phần tử có thể click được
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(li_element))

    # Click vào phần tử
    li_element.click()

    # Đợi nội dung tải
    time.sleep(5)

    # Thu thập các môn học
    course_elements = driver.find_elements(By.CSS_SELECTOR, 'div.ms_lms_courses_card_item')

    for course in course_elements:
        # Lấy tên môn học
        try:
            course_name = course.find_element(By.CSS_SELECTOR, 'div.ms_lms_courses_card_item_wrapper > div:nth-child(2) > a:nth-child(1) > h3').text
        except Exception:
            course_name = "Tên không có sẵn"

        # Lấy giá môn học
        try:
            price_element = course.find_element(By.CSS_SELECTOR, 'div.ms_lms_courses_card_item_info_price > div.ms_lms_courses_card_item_info_price_single > span')
            course_price = price_element.text
        except Exception:
            course_price = "Giá không có sẵn"

        # Lấy số sao
        try:
            rating_element = course.find_element(By.CSS_SELECTOR, 'div.ms_lms_courses_card_item_info_rating_quantity > span')
            course_rating = rating_element.text
        except Exception:
            course_rating = "Chưa có đánh giá"

        # Lấy số thành viên tham gia
        try:
            members_element = course.find_element(By.CSS_SELECTOR, 'div.ms_lms_courses_card_item_meta_block > i.stmlms-members + span')
            members_count = members_element.text
        except Exception:
            members_count = "Không có thông tin"

        # Lấy số người xem
        try:
            views_element = course.find_element(By.CSS_SELECTOR, 'div.ms_lms_courses_card_item_meta_block > i.stmlms-views + span')
            views_count = views_element.text
        except Exception:
            views_count = "Không có thông tin"

        # In ra thông tin
        print(f"Tên môn: {course_name}, Giá: {course_price}, Số sao: {course_rating}, Thành viên tham gia: {members_count}, Người xem: {views_count}")

    # Quay lại trang trước
    driver.back()
    time.sleep(5)

# Đóng trình duyệt
driver.quit()


















































































