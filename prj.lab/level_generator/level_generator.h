#pragma once
#ifndef LEVELGENERATOR_LEVELGENERATOR_H_20230423
#define LEVELGENERATOR_LEVELGENERATOR_H_20230423

#include <iostream>
#include <vector>
#include <random>
#include <cstdlib>
#include <ctime>

static std::mt19937 gen(static_cast<unsigned int>(time(0)));
//! @authors Мельникова М.Ф.
//! @brief Заголовочный файл для библиотеки LevelGenerator

//! \class LevelGenerator level_generator.h level_generator/level_generator.h
class LevelGenerator {
public:
    //! @brief Умолчательный конструктор
    LevelGenerator() = default;
    //! @brief Конструктор копирования
    LevelGenerator(const LevelGenerator&) = default;
    //! @brief Перегрузка оператора присваивания
    LevelGenerator& operator=(const LevelGenerator&) = default;
    //! @brief Деструктор
    ~LevelGenerator() = default;

    //! @brief Конструктор с двумя параметрами
    //! 
    //! Сгенерированный уровень будет размера rows на columns 
    //! @param[in] rows - количество строк карты уровня
    //! @param[in] columns - количество столбцов карты уровня
    LevelGenerator(long long rows, long long columns);

    //! @brief Количество строк карты экземпляра
    long long row_count() const { return n_rows; }
    //! @brief Количество столбцов карты экземпляра
    long long col_count() const { return n_cols; }
    //! @brief Матрица целых чисел, представляет карту уровня и расположение объектов разного типа на ней
    std::vector<std::vector<int>> show_level() const { return level; }

    //! @brief Генерация уровня
    void GenerateLevel();
    //! @brief Сохранение сгенерированного уровня в текстовый файл new_level.txt
    void SaveLevel();
private:
    long long n_rows{ 0 };
    long long n_cols{ 0 };
    std::vector<std::vector<int>> level;

    int RandInt(int a, int b) const;
    void GenerateWalls();
    void GeneratePoints();
};

inline int LevelGenerator::RandInt(int a, int b) const {
    return a + (gen() % (b - a + 1));
}

#endif