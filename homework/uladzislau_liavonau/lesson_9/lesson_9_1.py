from datetime import datetime

start_date = "Jan 15, 2023 - 12:05:33"

formatted_date_to_py_view = datetime.strptime(start_date, "%b %d, %Y - %H:%M:%f")
print(formatted_date_to_py_view)

full_month_name = formatted_date_to_py_view.strftime("%B")
print(f"Полное название месяца из заданной даты: {full_month_name}")

formatted_date = formatted_date_to_py_view.strftime("%d.%m.%Y, %H:%M")
print(f"Отформатированная дата имеет следующий вид: {formatted_date}")
