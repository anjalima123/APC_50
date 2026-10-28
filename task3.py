from PyPDF2 import PdfMerger

merger = PdfMerger()

# Add 3 PDF files
merger.append("1.pdf")
merger.append("2.pdf")
merger.append("3.pdf")

# Create one merged PDF
merger.write("merged.pdf")

merger.close()

print("3 PDF files merged successfully!")