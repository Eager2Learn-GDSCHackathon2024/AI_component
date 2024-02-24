def get_introduce_transcript(prompt):
    try:
        return f"""
        Xin chào em {prompt.user_info.name}. Chào mừng em đến với ứng dụng nhằm giúp em có thể tự học thật hiệu quả và vui vẻ. 
        Phần mềm đã nhận được yêu cầu học tập của em và đang cố gắng xử lý nó, em hãy cố gắng đợi một chút nhé. 
        Chúc em có một ngày học tập tuyệt vời và đầy ý nghĩa!
        """
    except:
        return "An error occured"

