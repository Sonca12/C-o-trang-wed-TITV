from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Thiết lập trình duyệt
driver = webdriver.Firefox()  # Hoặc webdriver.Chrome() nếu sử dụng Chrome
driver.get('https://titv.vn/')  # Thay thế bằng URL thực tế

# Đợi trang tải
time.sleep(5)

# Click vào thẻ "All"
button_all = driver.find_element(By.CSS_SELECTOR, 'span[data-id="all"]')  # Giả sử đây là thẻ cho "All"
button_all.click()
time.sleep(5)  # Đợi nội dung tải

# Hàm cuộn xuống để tải thêm môn học
def scroll_down():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Thời gian cho trang tải thêm nội dung
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # Kiểm tra nếu đã cuộn hết
            break
        last_height = new_height

# Hàm thu thập bình luận từ tất cả các môn học trong thẻ "All"
def collect_reviews_from_all():
    scroll_down()  # Cuộn xuống để tải hết nội dung

    # Cập nhật danh sách khóa học trong thẻ "All"
    course_elements = driver.find_elements(By.CSS_SELECTOR, 'div.ms_lms_courses_card_item_wrapper')
    if not course_elements:
        print("Không còn môn học nào trong thẻ All để thu thập.")
        return

    for i in range(len(course_elements)):
        try:
            # Click vào khóa học để thu thập bình luận
            course_link = course_elements[i].find_element(By.CSS_SELECTOR, 'a')  # Giả sử có một thẻ <a> để click vào
            course_link.click()
            time.sleep(5)  # Đợi nội dung tải

            # Thu thập bình luận
            reviews = driver.find_elements(By.CSS_SELECTOR, '.masterstudy-single-course-reviews__item-content p')
            for review in reviews:
                print("Bình luận:", review.text)

            # Quay lại danh sách khóa học
            driver.back()
            time.sleep(5)  # Đợi tải lại danh sách khóa học

            # Cuộn xuống để đảm bảo có đầy đủ môn học
            scroll_down()

            # Cập nhật lại danh sách khóa học sau khi quay lại
            course_elements = driver.find_elements(By.CSS_SELECTOR, 'div.ms_lms_courses_card_item_wrapper')

        except Exception as e:
            print(f"Không thể nhấp vào khóa học: {e}")

# Thu thập bình luận từ tất cả các môn trong thẻ "All"
collect_reviews_from_all()

# Kết thúc phiên làm việc
driver.quit()




