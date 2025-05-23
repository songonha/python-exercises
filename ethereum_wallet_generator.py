# Chương trình tạo ví Ethereum đơn giản
# Chương trình này sẽ tạo cụm từ mnemonic, khóa bí mật và địa chỉ ví Ethereum

# Cài đặt các thư viện cần thiết:
# pip install mnemonic web3 eth-account

# Import các thư viện cần thiết
from mnemonic import Mnemonic  # Thư viện để tạo và xử lý cụm từ mnemonic
from eth_account import Account  # Thư viện để tạo tài khoản Ethereum
import secrets  # Thư viện để tạo số ngẫu nhiên an toàn
import os  # Thư viện để làm việc với hệ thống tệp

# Kích hoạt tính năng tạo tài khoản từ khóa bí mật
Account.enable_unaudited_hdwallet_features()

def main():
    # Hiển thị thông báo giới thiệu
    print("===== CHƯƠNG TRÌNH TẠO VÍ ETHEREUM =====\n")
    print("Lưu ý: Đây chỉ là chương trình mô phỏng. Không sử dụng cho ví thật!\n")
    
    # Bước 1: Tạo cụm từ mnemonic (12 từ) theo chuẩn BIP-39
    print("Bước 1: Tạo cụm từ mnemonic...")
    mnemo = Mnemonic("english")  # Sử dụng từ điển tiếng Anh
    
    # Tạo entropy (nguồn ngẫu nhiên) an toàn bằng thư viện secrets
    # 128 bit cho 12 từ, 256 bit cho 24 từ
    entropy = secrets.token_bytes(16)  # 16 bytes = 128 bits = 12 từ
    
    # Tạo cụm từ mnemonic từ entropy
    mnemonic_phrase = mnemo.to_mnemonic(entropy)
    print(f"Cụm từ mnemonic: {mnemonic_phrase}\n")
    
    # Bước 2: Từ cụm từ mnemonic, suy ra khóa bí mật và địa chỉ ví
    print("Bước 2: Tạo khóa bí mật và địa chỉ ví...")
    
    # Tạo tài khoản từ cụm từ mnemonic
    # Tham số đầu tiên là cụm từ mnemonic
    # Tham số thứ hai là đường dẫn dẫn xuất (derivation path) theo chuẩn BIP-44 cho Ethereum
    account = Account.from_mnemonic(
        mnemonic_phrase,
        account_path="m/44'/60'/0'/0/0"  # Đường dẫn dẫn xuất chuẩn cho Ethereum
    )
    
    # Lấy khóa bí mật (dạng hex)
    private_key = account.key.hex()
    # Thêm tiền tố '0x' nếu chưa có
    if not private_key.startswith('0x'):
        private_key = '0x' + private_key
    
    # Lấy địa chỉ ví (dạng chuỗi)
    wallet_address = account.address
    
    print(f"Khóa bí mật: {private_key}")
    print(f"Địa chỉ ví: {wallet_address}\n")
    
    # Bước 3: Lưu thông tin vào file
    print("Bước 3: Lưu thông tin vào file...")
    
    # Tạo nội dung để lưu vào file
    file_content = f"""===== THÔNG TIN VÍ ETHEREUM =====

LƯU Ý: ĐÂY CHỈ LÀ VÍ MÔ PHỎNG, KHÔNG SỬ DỤNG CHO MỤC ĐÍCH THỰC TẾ!

Cụm từ mnemonic (12 từ):
{mnemonic_phrase}

Khóa bí mật (Private Key):
{private_key}

Địa chỉ ví (Wallet Address):
{wallet_address}

===== CẢNH BÁO AN TOÀN =====
Trong thực tế, KHÔNG BAO GIỜ chia sẻ cụm từ mnemonic hoặc khóa bí mật với bất kỳ ai!
Những thông tin này cho phép kiểm soát hoàn toàn ví của bạn.
"""
    
    # Tên file để lưu thông tin
    file_name = "wallet_info.txt"
    
    # Lưu nội dung vào file
    with open(file_name, "w") as file:
        file.write(file_content)
    
    print(f"Đã lưu thông tin vào file: {os.path.abspath(file_name)}\n")
    
    # Bước 4: Hiển thị địa chỉ ví ra màn hình
    print("Bước 4: Hiển thị địa chỉ ví")
    print(f"Địa chỉ ví EVM của bạn: {wallet_address}\n")
    
    print("===== HOÀN THÀNH =====")
    print("Lưu ý: Trong thực tế, hãy bảo vệ cẩn thận cụm từ mnemonic và khóa bí mật của bạn!")

# Chạy chương trình khi file được thực thi trực tiếp
if __name__ == "__main__":
    main()