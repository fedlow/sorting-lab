import random
import time
import matplotlib.pyplot as plt

from sorts import bubble_sort, selection_sort, insertion_sort


def measure(func, arr, repeats=3):
    total = 0.0
    for _ in range(repeats):
        data = arr.copy()
        start = time.perf_counter()
        func(data)
        total += time.perf_counter() - start
    return total / repeats


def main():
    random.seed(42)

    sizes = [100, 200, 300, 500, 700, 1000, 1500, 2000]
    bubble_times = []
    selection_times = []
    insertion_times = []

    for n in sizes:
        arr = [random.randint(1, 10_000) for _ in range(n)]

        bt = measure(bubble_sort, arr)
        st = measure(selection_sort, arr)
        it = measure(insertion_sort, arr)

        bubble_times.append(bt)
        selection_times.append(st)
        insertion_times.append(it)

        print(f"n={n:5d} | bubble={bt:.5f} c | selection={st:.5f} c | insertion={it:.5f} c")

    # График
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bubble_times, marker="o", label="Пузырьком")
    plt.plot(sizes, selection_times, marker="s", label="Выбором")
    plt.plot(sizes, insertion_times, marker="^", label="Вставками")
    plt.xlabel("Размер списка n")
    plt.ylabel("Среднее время сортировки, сек")
    plt.title("Сравнение простых сортировок")
    plt.legend()
    plt.grid(True)
    plt.savefig("sorting_comparison.png", dpi=150)
    plt.show()

    # Markdown-таблица в файл (UTF-8)
    lines = ["| n | Пузырьком, с | Выбором, с | Вставками, с |",
             "|---|---|---|---|"]
    for n, bt, st, it in zip(sizes, bubble_times, selection_times, insertion_times):
        lines.append(f"| {n} | {bt:.5f} | {st:.5f} | {it:.5f} |")

    with open("results.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("\nТаблица сохранена в results.md")

if __name__ == "__main__":
    main()