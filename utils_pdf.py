import os
from PyPDF2 import PdfReader, PdfWriter


def split_pdf(input_path, output_folder, pages_per_file):
    # Đọc file PDF đầu vào
    pdf_reader = PdfReader(input_path)
    total_pages = len(pdf_reader.pages)

    # Tạo thư mục đầu ra nếu chưa tồn tại
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Chia file PDF thành các file nhỏ
    for start in range(0, total_pages, pages_per_file):
        pdf_writer = PdfWriter()

        # Xác định số trang cho file hiện tại
        end = min(start + pages_per_file, total_pages)

        # Thêm các trang vào file mới
        for page in range(start, end):
            pdf_writer.add_page(pdf_reader.pages[page])

        # Lưu file mới
        output_filename = f'output_{start + 1}-{end}.pdf'
        output_path = os.path.join(output_folder, output_filename)
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

        print(f'Đã tạo file: {output_filename}')


def merge_pdfs(input_folder, output_path):
    # Tạo một đối tượng PdfMerger
    merger = PdfMerger()

    # Lấy danh sách tất cả các file PDF trong thư mục đầu vào
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

    # Sắp xếp các file theo tên (tùy chọn)
    pdf_files.sort()

    # Thêm từng file vào merger
    for pdf_file in pdf_files:
        file_path = os.path.join(input_folder, pdf_file)
        merger.append(file_path)
        print(f"Đã thêm file: {pdf_file}")

    # Ghi file PDF đã gộp
    merger.write(output_path)
    merger.close()

    print(f"Đã gộp thành công các file PDF vào: {output_path}")
# Sử dụng hàm
if __name__ == '__main__':
    input_path = 'input.pdf'  # Đường dẫn đến file PDF đầu vào
    output_folder = 'output'  # Thư mục để lưu các file PDF đầu ra
    pages_per_file = 5  # Số trang cho mỗi file đầu ra

    # split_pdf(input_path, output_folder, pages_per_file)
    # merge_pdfs(input_folder, output_path)
