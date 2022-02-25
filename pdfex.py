import pdfplumber

print("Extração de informações do documento PDF\n")

arquivo = 'boleto/claro.pdf'

with pdfplumber.open(arquivo) as pdf:
    
    for pagina in pdf.pages:
        
        resultado = pagina.extract_text()
        
        print("\nResultado da Extração: \n")
        
        print(resultado)
    
    