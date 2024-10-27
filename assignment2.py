text=input("შეიყვანეთ სიტყვა:")

if "small" in text:
    print("small")
if "tall" in text:
    print("tall")
if "middle" in text:
    print("middle")

if "small" not in text and "tall" not in text and "middle" not in text:
    print("ამ სიტყვებიდან არცერთი არ მოიძებნა.")
