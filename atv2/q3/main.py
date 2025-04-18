# add dynamic event map

def mostrar_mapa_assentos():
    for row in rows:
        print(f'{row} ', end=" ")
        for collum in collumns:
            seat = row + collum
            if seat in seats_taken:
                print(f"[X]", end=" ")
            else:
                print(f"[{seat}]", end=" ")
        print()
    print("   ", end="")
    print(*collumns, sep=f"{' ' * 5}")


def main():
    print("Bem-vindo ao sistema de reservas de assentos\n")
    
    while True:
        print("[1] Reservar assento")
        print("[2] Cancelar reserva")
        print("[3] Sair\n")
        
        comando = input("O que você deseja fazer?\n>> ").strip()
        
        if comando == '1':
            mostrar_mapa_assentos()
            
            while True:
                seat = input("Digite o assento (ex: A1): ").strip().upper()
                if len(seat) == 2 and seat[0] in rows and seat[1] in collumns:
                    if seat not in seats_taken:
                        seats_taken.append(seat)
                        print(f"Assento {seat} reservado com sucesso!\n")
                        break
                    else:
                        print("Assento já reservado. Tente outro.\n")
                        
        elif comando == '2':
            mostrar_mapa_assentos()
            
            while True:
                seat = input("Qual assento você deseja cancelar? (ex: A1): ").strip().upper()
                if len(seat) == 2 and seat[0] in rows and seat[1] in collumns:
                    if seat in seats_taken:
                        seats_taken.remove(seat)
                        break
                    else:
                        print("Assento não reservado. Tente outro.\n")
        
        elif comando == '3':
            print("Saindo do programa...")
            break
                    

rows = ['A', 'B', 'C', 'D', 'E', 'F']
collumns = ['1', '2', '3', '4', '5', '6']
seats_taken = []

if __name__ == '__main__':
    main()