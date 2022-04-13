def password_check(password):
    flag_minuscula = False
    flag_maiuscula = False
    flag_numeros = False

    if len(password) < 6 or len(password) > 32 or " " in password:
        return False

    else:
        for letra in password:
            # a to a = 97 a 122
            if 97 <= ord(letra) <= 122:
                flag_minuscula = True

            # A to Z = 65 a 90
            elif 65 <= ord(letra) <= 90:
                flag_maiuscula = True

            # 0 a 9 = 48 a 57
            elif 48 <= ord(letra) <= 57:
                flag_numeros = True

            else:
                return False

        return flag_maiuscula and flag_minuscula and flag_numeros


def main():
    while True:
        try:
            senha = input()
            if password_check(senha):
                print('Senha valida.')
            else:
                print('Senha invalida.')
        except EOFError:
            break


if __name__ == '__main__':
    main()
