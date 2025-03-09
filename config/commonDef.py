class CommonDef:
    @staticmethod
    def format_number(amount):
        # Chuyển đổi amount thành float nếu nó là chuỗi
        try:
            number = float(amount)
        except (ValueError, TypeError):
            return "Invalid amount"  # Trả về thông báo lỗi nếu không thể chuyển đổi

        # Định dạng số với dấu phẩy ngăn cách hàng nghìn và thêm "VND"
        formatted_amount = "{:,.0f}".format(number)
        return f"{formatted_amount} VND"

    @staticmethod
    def unformat_number(amount):
        try:
            remove_vnd = amount.replace("VND", "").strip().replace(",", "")
            return float(remove_vnd)
        except (ValueError, TypeError, AttributeError):
            return None