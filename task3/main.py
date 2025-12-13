import timeit
from rabin_karp_search import rabin_karp_search
from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search

def time_search(func, text, pattern):
    stmt = lambda: func(text, pattern)
    return timeit.timeit(stmt, number=10)

def main():
    with open("article1.txt", "r", encoding="utf-8") as f:
        text1 = f.read()

    with open("article2.txt", "r", encoding="utf-8") as f:
        text2 = f.read()

    # Існуючий підрядок (візьмемо початок тексту)
    pattern_existing1 = text1[10:30]
    pattern_existing2 = text2[50:70]

    # Неіснуючий підрядок
    pattern_fake = "thissubstringdoesnotexist"

    algorithms = {
    "KMP": kmp_search,
    "Rabin-Karp": rabin_karp_search,
    "Boyer-Moore": boyer_moore_search
    }

    for idx, (text, pat_exist) in enumerate([(text1, pattern_existing1), (text2, pattern_existing2)], start=1):
        print(f"\n--- Article {idx} ---")
        times = {}
        for name, func in algorithms.items():
            t_exist = time_search(func, text, pat_exist)
            t_fake = time_search(func, text, pattern_fake)
            print(f"{name}: Existing substring = {t_exist:.6f}s, Fake substring = {t_fake:.6f}s")
            times[name] = t_exist  # або можна зберігати суму t_exist + t_fake

    # Визначаємо найшвидший алгоритм для існуючого підрядка
    fastest = min(times, key=times.get)
    print(f"Fastest algorithm for Article {idx}: {fastest}")

    


if __name__ == "__main__":
    main()