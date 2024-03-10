#script for game
import pyautogui
import cv2
import numpy as np
import time

# تشخیص الگوی بازی
def detect_pattern():
    # کد تشخیص الگو اینجا قرار می‌گیرد
    # برای مثال، می‌توانید با استفاده از OpenCV الگوهای خاص را تشخیص دهید
    pass

# تشخیص بازی به طور عادی یا استفاده از اسکریپت
def detect_script_usage():
    # کد تشخیص بازیکن‌هایی که از اسکریپت استفاده می‌کنند اینجا قرار می‌گیرد
    # برای مثال، می‌توانید با OpenCV الگوهای خاص را تشخیص دهید
    pass

# اجرای اسکریپت
def run_script():
    while True:
        # تشخیص الگوی بازی
        if detect_pattern():
            # تشخیص بازی به طور عادی یا استفاده از اسکریپت
            if not detect_script_usage():
                # اگر بازیکن بازی را به طور عادی انجام دهد، بازی را ادامه دهید
                # در غیر این صورت، بزنید
                pyautogui.click()
                time.sleep(0.5)  
                # انتظار برای جلوگیری از کلیک‌های متوالی
        else:
            print("الگوی بازی یافت نشد!")

if __name__ == "__main__":
    run_script()


