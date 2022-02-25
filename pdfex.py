import pdfplumber

print("Extração de informações do documento PDF\n")

arquivo = 'boleto/claro.pdf'

with pdfplumber.open(arquivo) as pdf:
    
    print("Numero de paginas: ", len(pdf.pages), "\n")
    
    for pagina in pdf.pages:
        
        resultado = pagina.extract_text()
        
        print("\nResultado da Extração: \n")
        
        print(resultado)
    
    