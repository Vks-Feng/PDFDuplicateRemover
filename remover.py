import re
from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
from pytesseract import image_to_string

def extract_page_number(text):
    """
    从提取的文本中提取页码信息。
    例如，从 '- 1/145 -' 提取 '1'。
    """
    match = re.search(r'(\d+)/(\d+)', text)  # 匹配形如 "数字/数字" 的部分
    if match:
        current_page = match.group(1)  # 获取当前页码
        print("正在处理第" + current_page + "页")
        return current_page
    return None

def extract_page_number_from_image(image, ocr_area):
    """
    从图片的指定区域提取页码信息。
    """
    cropped_image = image.crop(ocr_area)  # 根据区域裁剪图像
    text = image_to_string(cropped_image, lang="eng")  # OCR 提取文本
    return extract_page_number(text)  # 提取页码信息

def remove_duplicate_pages(input_pdf, output_pdf, ocr_area):
    """
    删除重复的 PDF 页面，保留最后一个出现的。
    """
    # 提取 PDF 页码图片
    images = convert_from_path(input_pdf, dpi=200)

    page_map = {}
    for i, image in enumerate(images):
        page_number = extract_page_number_from_image(image, ocr_area)
        if page_number:
            page_map[page_number] = i  # 保留最后一个出现的页面

    # 获取保留的页面索引
    unique_page_indices = sorted(page_map.values())

    # 读取 PDF 文件并保存保留的页面
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for index in unique_page_indices:
        writer.add_page(reader.pages[index])

    # 保存去重后的 PDF
    with open(output_pdf, "wb") as f:
        writer.write(f)

if __name__ == "__main__":
    input_pdf = "4-关系.pdf"  # 输入 PDF 文件路径
    output_pdf = "output" + input_pdf # 输出 PDF 文件路径

    # 右下角区域（需要根据 PDF 实际内容调整），格式为 (left, top, right, bottom)
    # 实测 PDF 页面为 1008x756 像素，需截取的部分如下ocr_area
    ocr_area = (908, 731, 1008, 756)  

    remove_duplicate_pages(input_pdf, output_pdf, ocr_area)
