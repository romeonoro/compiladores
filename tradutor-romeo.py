MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',
    '--..--': ',', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-',
    '-.--.': '(', '-.--.-': ')'
}

def morse_para_ascii(mensagem_morse):

    mensagem_morse = mensagem_morse.strip().replace(' / ', '   ')
    
    palavras_morse = mensagem_morse.split('   ')
    
    mensagem_decodificada = []
    
    for palavra in palavras_morse:
        letras_morse = palavra.split(' ')
        
        palavra_texto = ''.join(MORSE_CODE_DICT.get(letra, '') for letra in letras_morse)
        
        mensagem_decodificada.append(palavra_texto)
        
    return ' '.join(mensagem_decodificada)

if __name__ == "__main__":
    print("=== TRADUTOR DE CÓDIGO MORSE PARA TEXTO ===")
    print("Dica: Use 1 espaço para separar letras e 3 espaços (ou '/') para separar palavras.")
    print("Digite 'sair' a qualquer momento para fechar o programa.\n")
    
    while True:
        codigo = input("Digite o código Morse: ")
        
        if codigo.lower() == 'sair':
            print("Encerrando o tradutor. Até logo!")
            break
            
        if not codigo.strip():
            continue
            
        texto_traduzido = morse_para_ascii(codigo)
        print(f"Texto Traduzido: {texto_traduzido}\n")

# Exemplo de uso:
#  - .... . .-.. .-.. ---   .--. -.-- - .... --- -.
# -.... --...