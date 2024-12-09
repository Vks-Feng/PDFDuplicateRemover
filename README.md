# PDFDuplicateRemover

用于去除离散数学课件中冗余页面，提高可读性

## Notice

第八章群论的ppt存在一些问题，少了以下页数

| 逻辑页码 | 对应的原始ppt实际页码 |
| ---- | ------------ |
| 14   | 63           |
| 20   | 102          |
| 24   | 124          |
| 43   | 243          |
| 44   | 252          |
| 91   | 584          |
| 98   | 627          |
| 117  | 764          |

### 使用说明：PDF 删除重复页面脚本

---

#### **功能简介**

本脚本通过 OCR（光学字符识别）提取 PDF 页面右下角的页码信息，删除具有相同页码的重复页面，仅保留每个页码的最后一个出现的页面，并生成一个新的 PDF 文件。

---

#### **环境要求**

1. Python 3.8 或更高版本。
2. 以下 Python 库：
   - `PyPDF2`
   - `pdf2image`
   - `pytesseract`

---

#### **安装步骤**

1. **安装 Python 库**  
   使用 `pip` 安装所需库：
   ```bash
   pip install PyPDF2 pdf2image pytesseract
   ```

2. **安装 Tesseract-OCR**  
   - **Windows**：
     从 [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) 下载并安装。  
     安装完成后，将路径（例如 `C:\Program Files\Tesseract-OCR\tesseract.exe`）添加到系统的 PATH 环境变量中。
   - **Linux**：
     ```bash
     sudo apt-get install tesseract-ocr
     ```
   - **macOS**：
     ```bash
     brew install tesseract
     ```

3. **安装 Poppler**  
   - **Windows**：
     从 [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/) 下载并安装。  
     将 `bin` 文件夹的路径添加到系统 PATH 环境变量中。
   - **Linux**：
     ```bash
     sudo apt-get install poppler-utils
     ```
   - **macOS**：
     ```bash
     brew install poppler
     ```

---

#### **使用方法**

1. 将脚本文件（`remove_duplicate_pages.py`）放置在项目目录中。
2. 确保输入的 PDF 文件与脚本位于同一目录，或者在脚本中指定 PDF 文件的完整路径。
3. 运行脚本：
   ```bash
   python remove_duplicate_pages.py
   ```

---

#### **参数说明**

1. **输入 PDF 文件**：
   - 修改 `input_pdf` 变量以指定输入 PDF 文件的名称。  
     示例：`input_pdf = "example.pdf"`

2. **输出 PDF 文件**：
   - 脚本会在输入 PDF 文件名的基础上生成一个新的去重 PDF 文件，文件名加上前缀 `"output"`。

3. **OCR 检测区域**：
   - `ocr_area` 变量定义了页码所在的矩形区域。格式为 `(left, top, right, bottom)`。
   - 需要根据实际 PDF 页面内容调整此区域。

---

#### **示例配置**

```python
input_pdf = "示例.pdf"
output_pdf = "output_示例.pdf"
ocr_area = (908, 731, 1008, 756)  # 根据实际 PDF 调整
```

---

#### **工作原理**

![87c368c75b568ccaf35761b1bb96c7d](https://github.com/user-attachments/assets/ca391bb9-a2c0-42dc-ad9a-07e2c105f132)

1. **转换 PDF 页面为图片**：  
   使用 `pdf2image` 将 PDF 的每一页转换为图片。

2. **提取页码信息**：  
   对每页图片的指定区域运行 OCR，识别出页码信息（如 `1/145`）。

3. **去重逻辑**：  
   对具有相同页码的页面，仅保留其最后一次出现。

4. **生成新 PDF 文件**：  
   保存处理后的唯一页面到新 PDF 文件中。

---

#### **输出示例**

输入 PDF 文件为 `example.pdf`，脚本将生成去重后的文件 `output_example.pdf`。

---

#### **开发者说明**

本脚本基于 `PyPDF2`、`pdf2image` 和 `pytesseract` 实现。适用于处理带有重复页码信息的 PDF 文档，简化手动操作流程。
