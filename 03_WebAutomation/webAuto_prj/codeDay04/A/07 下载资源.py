from common.open_web import *
from selenium.webdriver.common.by import By
import os

# 准备配置项
options = webdriver.ChromeOptions()

# 动态生成下载的路径
download_path = os.path.abspath('download')
prefs = {
    'profile.default_content_settings.popups': 0,  # 取消弹窗
    'download.default_directory': download_path,   # 设置下载路径
    "download.prompt_for_download": False,       # 禁用下载提示
    "download.directory_upgrade": True,          # 允许下载到指定目录
    "safebrowsing.enabled": True                 # 启用安全浏览
}
options.add_experimental_option('prefs', prefs)

# 打开浏览器, 请求目标网址
driver = webdriver.Chrome(options=options)
driver.get('https://app.bilibili.com/?spm_id_from=333.1007.0.0')
driver.maximize_window()

driver.implicitly_wait(100)

# 下载的操作
driver.find_element(By.CSS_SELECTOR, '#download-link > a.dt-btn.btn-pc.bg-pc').click()

sleep(30)
# 检查文件下载是否成功
print(os.listdir('./download'))
if 'bili_win-install.exe' in os.listdir('./download'):
    print('下载成功')
else:
    print('下载失败')

sleep(1)
# 退出浏览器
driver.quit()
