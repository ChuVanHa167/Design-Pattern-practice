# vấn đề (Có những class trong hệ thống chỉ nên có 1 instance duy nhất), 
# ý tưởng (Singleton đảm bảo chỉ có một object duy nhất được tạo ra), 
# kết luận (Singleton giúp kiểm soát số lượng instance, đảm bảo toàn hệ thống chỉ dùng chung một object.)

class Logger:

    _instance = None # Biến này dùng để lưu instance duy nhất.

    def __new__(cls): # Phương thức __new__ được gọi trước __init__, nó kiểm tra nếu instance đã tồn tại thì trả về instance đó, nếu chưa thì tạo mới.

        if cls._instance is None: # Nếu chưa có instance nào, tạo mới và lưu vào biến _instance.
            cls._instance = super().__new__(cls) # Gọi __new__ của lớp cha để tạo instance mới.

        return cls._instance

    def log(self, message):
        print(f"[LOG] {message}")