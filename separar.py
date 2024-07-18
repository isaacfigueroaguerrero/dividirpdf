from PyPDF2 import PdfReader, PdfWriter
import os


def contains_hoja_1(text):
    return "HOJA 1" in text


def split_pdf(input_path, output_dir):
    print(f"Procesando archivo: {input_path}")

    try:
        with open(input_path, 'rb') as file:
            reader = PdfReader(file)
            total_pages = len(reader.pages)
            print(f"Total de páginas: {total_pages}")

            current_writer = PdfWriter()
            current_start = 1
            documents_created = 0

            for i, page in enumerate(reader.pages, start=1):
                print(f"Procesando página {i}/{total_pages}")

                text = page.extract_text()

                if contains_hoja_1(text):
                    print(f"Encontrado 'HOJA 1' en la página {i}")

                    # Si no es la primera página, guardar el documento anterior
                    if i > 1:
                        output_path = os.path.join(
                            output_dir, f"documento_separado_{current_start}-{i-1}.pdf")
                        with open(output_path, "wb") as output_file:
                            current_writer.write(output_file)
                        print(f"Documento creado: {output_path}")
                        documents_created += 1

                    # Iniciar un nuevo documento
                    current_writer = PdfWriter()
                    current_start = i

                    print(f"Nueva sección iniciada en página {i}")

                current_writer.add_page(page)

            # Guardar el último documento
            output_path = os.path.join(
                output_dir, f"documento_separado_{current_start}-{total_pages}.pdf")
            with open(output_path, "wb") as output_file:
                current_writer.write(output_file)
            print(f"Documento final creado: {output_path}")
            documents_created += 1

            print(f"\nProceso completado.")
            print(f"Total de documentos creados: {documents_created}")

    except Exception as e:
        print(f"Error durante la ejecución: {str(e)}")


# Uso del script
input_pdf = r"C:\Users\anton\OneDrive\Escritorio\pruebas\test.pdf"
output_dir = r"C:\Users\anton\OneDrive\Escritorio\pruebas"
split_pdf(input_pdf, output_dir)
