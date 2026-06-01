total_price = int(input("Nhập tổng tiền hóa đơn ban đầu: "))
if total_price >= 500000:
    sale = total_price * 0.1
    total_price -= sale
    print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")
    print(f"Số tiền được giảm giá: {sale} VND")
    print(f"Tổng tiền khách phải trả: {total_price}")
else:
    print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")
    print("Không được giảm giá")
    print(f"Tổng tiền khách phải trả: {total_price}")

