"""
ให้ width และ height  รับ input จากผู้ใช้งานเข้ามาแล้วนำมาหาผลลัพธ์พร้อมแสดงผลข้อมูล

    print(ผลลัพธ์ของ width 50 ซม และ height 30 ซม คือ sum 80 ซม)
    
โดยตัวเลขต้องเป็นตัวเลขตามที่ผู้ใช้งานกรอกเข้ามา

"""

## input width
width = int(input("Enter your width : "))

## input height
height = int(input("Enter your width : "))

result = width + height


## print
print(
    "ผลลัพธ์ของ width ",
    width,
    "ซม และ ผลลัพธ์ของ height ",
    height,
    "ซม คือ sum",
    result,
    "ซม",
)
