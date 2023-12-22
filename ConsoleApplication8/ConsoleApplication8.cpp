#include <iostream>
#include <vector>
#include <random>

int main() {
    // Задані значення імовірностей та відповідних xi
    std::vector<int> xi = { 10, 25, 100, 200 };
    std::vector<double> pi = { 0.1, 0.1, 0.75, 0.05 };

    std::vector<int> sequence_M;

    // Ініціалізуємо генератор випадкових чисел
    std::random_device rd;
    std::default_random_engine generator(rd());

    // Генеруємо послідовність M
    for (int i = 0; i < 100; i++) {
        std::discrete_distribution<int> distribution(pi.begin(), pi.end());
        int random_index = distribution(generator);
        sequence_M.push_back(xi[random_index]);
    }

    // Роздрукуємо послідовність M
    for (int value : sequence_M) {
        std::cout << value << " ";
    }

    return 0;
}