# Chương Trình Tạo Ví Ethereum

Đây là một chương trình Python đơn giản để tạo ví Ethereum, bao gồm việc tạo cụm từ mnemonic, khóa bí mật và địa chỉ ví. Chương trình này chỉ dành cho mục đích học tập và không nên sử dụng để tạo ví thật.

## Yêu Cầu

- Python 3.6 trở lên
- Các thư viện: `mnemonic`, `web3`, `eth-account`

## Cài Đặt Thư Viện

Trước khi chạy chương trình, bạn cần cài đặt các thư viện cần thiết bằng lệnh sau:

```bash
pip install mnemonic web3 eth-account
```

## Cách Sử Dụng

1. Chạy chương trình bằng lệnh:

```bash
python ethereum_wallet_generator.py
```

2. Chương trình sẽ tự động:
   - Tạo cụm từ mnemonic (12 từ) theo chuẩn BIP-39
   - Suy ra khóa bí mật (private key) từ cụm từ mnemonic
   - Tạo địa chỉ ví Ethereum từ khóa bí mật
   - Lưu thông tin vào file `wallet_info.txt`
   - Hiển thị địa chỉ ví ra màn hình

## Giải Thích Mã Nguồn

Chương trình sử dụng các thư viện sau:

- `mnemonic`: Để tạo và xử lý cụm từ mnemonic theo chuẩn BIP-39
- `eth_account`: Để tạo tài khoản Ethereum từ cụm từ mnemonic
- `secrets`: Để tạo số ngẫu nhiên an toàn
- `os`: Để làm việc với hệ thống tệp

Quy trình tạo ví bao gồm 4 bước chính:

1. Tạo cụm từ mnemonic (12 từ) theo chuẩn BIP-39
2. Từ cụm từ mnemonic, suy ra khóa bí mật và địa chỉ ví
3. Lưu thông tin vào file `wallet_info.txt`
4. Hiển thị địa chỉ ví ra màn hình

## Lưu Ý An Toàn

- Đây chỉ là chương trình mô phỏng cho mục đích học tập
- Trong thực tế, KHÔNG BAO GIỜ chia sẻ cụm từ mnemonic hoặc khóa bí mật với bất kỳ ai
- Những thông tin này cho phép kiểm soát hoàn toàn ví của bạn