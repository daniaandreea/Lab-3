"""
Scrieți un program care determină cea mai lungă subsecvență cu o anumită proprietate a unei liste de numere.
Rezolvați problema folosind:
- Minim două funcții: una pentru calcule, specificată și testată cu assert, și alta care citește, afișează și apelează
funcția pentru calcule. Nu aveți voie să folosiți cod în afara unei funcții.
- O interfață cu utilizatorul care are un meniu de genul:
1. Citire date.
2. Determinare cea mai lungă subsecvență cu proprietatea 1.
3. Determinare cea mai lungă subsecvență cu proprietatea 2.
4. Determinare cea mai lungă subsecvență cu proprietatea 3.
5. Ieșire.

Proprietăți:
2. Toate numerele sunt prime.
12. Toate numerele același număr de divizori.
5. Toate numerele sunt palindroame.
"""


def is_prime(num):
    """
    Verifică dacă un număr este prim.
    :param num: int, numărul de verificat
    :return: True, dacă numărul e prim
             False, altfel
    """
    if num < 2:
        return False
    d = 2
    while d*d <= num:
        if num % d == 0:
            return False
        d += 1
    return True


def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(13) is True
    assert is_prime(18) is False
    assert is_prime(666013) is True


test_is_prime()


def all_prime(lst):
    """
    Determină dacă o listă este formată doar din elemente prime.
    :param lst: lista dată
    :return: True, dacă lst are doar elemente prime
            False, altfel
    """
    for num in lst:
        if is_prime(num) is False:
            return False
    return True


def test_all_prime():
    assert all_prime([3, 11, 14, 5, 7]) is False
    assert all_prime([5, 666013, 19, 23]) is True
    assert all_prime([1, 7, 3, 10]) is False


test_all_prime()


def get_longest_sublist_all_prime(lst):
    """
    Determină cea mai lungă subsecvență cu toate numerele prime.
    :param lst: lista dată
    :return: o listă reprezentând subsecvența cerută
    """
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            considered = lst[i:j + 1]
            if all_prime(considered):
                if len(result) < len(considered):
                    result = considered
    return result


def test_get_longest_sublist_all_prime():
    assert get_longest_sublist_all_prime([1, 2, 10, 7, 5, 666013]) == [7, 5, 666013]
    assert get_longest_sublist_all_prime([]) == []
    assert get_longest_sublist_all_prime([2]) == [2]


test_get_longest_sublist_all_prime()


def nr_of_divisors(num):
    """
        Determină câți divizori are un număr dat.
        :param num: int, numărul de verificat
        :return: int, numărul divizorilor
    """
    count = 0
    for d in range(1, num+1):
        if num % d == 0:
            count = count + 1
    return count


def test_nr_of_divisors():
    assert nr_of_divisors(12) == 6
    assert nr_of_divisors(1) == 1
    assert nr_of_divisors(13) == 2


test_nr_of_divisors()


def all_equal_nr_of_divisors(lst):
    """
    Determină dacă o listă este formată doar din elemente cu același număr de divizori.
    :param lst: lista dată
    :return: True, dacă lst are doar elemente cu proprietatea cerută
            False, altfel
    """
    c = nr_of_divisors(lst[0])
    for num in lst:
        if nr_of_divisors(num) != c:
            return False
    return True


def test_all_equal_nr_of_divisors():
    assert all_equal_nr_of_divisors([3, 17, 12, 5, 7]) is False
    assert all_equal_nr_of_divisors([2, 666013, 19, 23]) is True
    assert all_equal_nr_of_divisors([1, 7, 3, 8]) is False


test_all_equal_nr_of_divisors()


def get_longest_sublist_all_equal_nr_of_divisors(lst):
    """
    Determină cea mai lungă susecvență formată doar din elemente cu același număr de divizori.
    :param lst: lista dată
    :return: o listă reprezentând subsecvența cerută
    """
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            considered = lst[i:j + 1]
            if all_equal_nr_of_divisors(considered):
                if len(result) < len(considered):
                    result = considered
    return result


def test_get_longest_sublist_all_equal_nr_of_divisors():
    assert get_longest_sublist_all_equal_nr_of_divisors([1, 3, 6, 7, 5, 666013]) == [7, 5, 666013]
    assert get_longest_sublist_all_equal_nr_of_divisors([]) == []
    assert get_longest_sublist_all_equal_nr_of_divisors([2]) == [2]


test_get_longest_sublist_all_equal_nr_of_divisors()


def is_palindrome(num):
    """
    Verifică dacă un număr dat este palindrom
    :param num: int, numărul de verificat
    :return: True, dacă numărul e palindrom
             False, altfel
    """
    if num > 9:
        copie = num
        oglindit = 0
        while copie > 0:
            cifra = int(copie % 10)
            oglindit = oglindit * 10 + cifra
            copie = copie // 10
        if num == oglindit:
            return True
        else:
            return False
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(1212) is False
    assert is_palindrome(5555) is True
    assert is_palindrome(4) is False
    assert is_palindrome(9669) is True


test_is_palindrome()


def all_palindrome(lst):
    """
    Determină dacă o listă este formată doar din palindroame.
    :param lst: lista dată
    :return: True, dacă lst are doar palindroame
            False, altfel
    """
    for num in lst:
        if is_palindrome(num) is False:
            return False
    return True


def test_all_palindrome():
    assert all_palindrome([121, 11, 10, 77]) is False
    assert all_palindrome([88888, 44544, 2002]) is True
    assert all_palindrome([101, 121, 33, 88]) is True


test_all_palindrome()


def get_longest_sublist_all_palindrome(lst):
    """
    Determină cea mai lungă susecvență cu palindroame.
    :param lst: lista dată
    :return: o listă reprezentând subsecvența cerută
    """
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            considered = lst[i:j + 1]
            if all_palindrome(considered):
                if len(result) < len(considered):
                    result = considered
    return result


def test_longest_sublist_all_palindrome():
    assert get_longest_sublist_all_palindrome([11, 202, 4, 131, 4554, 888, 17]) == [131, 4554, 888]
    assert get_longest_sublist_all_palindrome([414]) == [414]
    assert get_longest_sublist_all_palindrome([1, 2, 4, 5]) == []


test_longest_sublist_all_palindrome()


def read_list():
    given = input('Dați numerele separate prin virgulă: ')
    str_list = given.split(',')
    int_list = []
    for str_num in str_list:
        int_list.append(int(str_num))
    return int_list


def print_menu():
    print('1. Citire date.')
    print('2. Determinare cea mai lungă subsecvență cu numere prime.')
    print('3. Determinare cea mai lungă subsecvență de numere cu același număr de divizori.')
    print('4. Determinare cea mai lungă subsecvență de palindroame.')
    print('x. Ieșire.')


def main():
    lst = []
    while True:
        print_menu()
        option = input('Alegeți opțiunea: ')
        if option == '1':
            lst = read_list()
        elif option == '2':
            result = get_longest_sublist_all_prime(lst)
            print('Cea mai lungă subsecvență cu toate numerele prime este: ')
            print(result)
        elif option == '3':
            result = get_longest_sublist_all_equal_nr_of_divisors(lst)
            print('Cea mai lungă subsecvență formată doar din elemente cu același număr de divizori este: ')
            print(result)
        elif option == '4':
            result = get_longest_sublist_all_palindrome(lst)
            print('Cea mai lungă subsecvență cu palindroame este: ')
            print(result)
        elif option == 'x':
            break
        else:
            print('Opțiune invalidă, reîncearcă!')


main()
