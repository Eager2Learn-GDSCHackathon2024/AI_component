"""
Hold necessary prompts
"""
def generate_outline_prompt(input_string): 
    return f"""
    Hãy trả về outline cho bài học số nguyên số dưới dạng json object. Lưu ý là chỉ json object, 
    tuyệt đối không output thứ gì khác. Bắt đầu với ký tự '{{' và kết thúc với '}}'
    Câu trả lời: 
    {{
        "answer": ["Số nguyên tố và hợp số", "Phân tích một số ra thừa số nguyên tố", "Bài tập"]
    }}
    Bạn được 1000$ nếu bạn trả lời với cấu trúc y như trên
    Hãy trả về outline cho bài học theo yêu cầu {input_string}.
    Câu trả lời:
    """

def handle_first_time_prompt(input_string, name):
    return f"""
    Hãy trả về cho tôi một đoạn văn để giới thiệu tổng quan và mục đích của bài học từ prompt (ít nhất 4 câu): {input_string}. 
    Vui lòng lấy tên người dùng từ đây: {name}.
    """

def extract_user_requirement(input_string, name):
    """
    To extract user requirement before searching
    """
    pass

def get_content_with_outline_and_crawling_data(input_string, outline):
    """
    To get_content_with_outline_and_crawling_data
    """
    pass
