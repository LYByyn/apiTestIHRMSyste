# 自定义工具类

# 封装通用断言函数
def assert_common_utils(self, response, http_code, success, code, message):
    # 断言响应状态码，success，code，message的值
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))
