#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <queue>
#include <level_generator\level_generator.h>

LevelGenerator::LevelGenerator(long long rows, long long columns) : n_rows(rows), n_cols(columns) {
    if (rows < 1 || columns < 1) {
        throw std::invalid_argument("Rows and columns must be positive integers");
    }
    level.resize(n_rows, std::vector<int>(n_cols, 0));
}

// 0 - пустое поле
// 1 - стена
// 2 - лчки

void LevelGenerator::GenerateWalls() {
    std::ptrdiff_t y = n_rows / 2;
    std::ptrdiff_t x = 1;
    level[y][x] = 9;
    while (x != n_cols - 2) {
        int r = RandInt(1, 3);
        if (r == 1 && y != 1)
            --y;
        else if (r == 2 && y != n_rows - 2)
            ++y;
        else if (r == 3 && x != n_cols - 2)
            ++x;
        level[y][x] = 9;
    }
    for (std::ptrdiff_t i = 0; i < n_cols; ++i) {
        for (std::ptrdiff_t j = 0; j < n_rows; ++j) {
            int r = RandInt(1, 4);
            if (r == 1 && level[j][i] != 9)
                level[j][i] = 1;
            else if (level[j][i] == 9)
                level[j][i] = 0;
        }
    }
}

void LevelGenerator::GeneratePoints() {
    std::ptrdiff_t y = n_rows / 2;
    std::ptrdiff_t x = 1;
    level[y][x] = 9;
    std::queue<std::vector<std::ptrdiff_t>> q;
    std::vector<std::ptrdiff_t> new_cell = {n_rows/2, 1};
    q.push(new_cell);
    while (!q.empty()){
        std::vector<std::ptrdiff_t> current_cell = q.front();
        std::ptrdiff_t y = current_cell[0], x = current_cell[1];
        if (y < n_rows - 1 && level[y+1][x] == 0){
            level[y+1][x] = 9;
            new_cell = {y+1, x};
            q.push(new_cell);
        }
        if (y > 0 && level[y-1][x] == 0){
            level[y-1][x] = 9;
            new_cell = {y-1, x};
            q.push(new_cell);
        }
        if (x < n_cols - 1 && level[y][x+1] == 0){
            level[y][x+1] = 9;
            new_cell = {y, x+1};
            q.push(new_cell);
        }
        if (x > 0 && level[y][x-1] == 0){
            level[y][x-1] = 9;
            new_cell = {y, x-1};
            q.push(new_cell);
        }
        q.pop();
    }
    for (std::ptrdiff_t i = 0; i < n_cols; ++i) {
        for (std::ptrdiff_t j = 0; j < n_rows; ++j) {
            int r = RandInt(1, 10);
            if (r == 1 && level[j][i] == 9)
                level[j][i] = 2;
            else if (level[j][i] == 9)
                level[j][i] = 0;
        }
    }
}

void LevelGenerator::GenerateLevel() {
    GenerateWalls();
    GeneratePoints();
}

// void LevelGenerator::SaveLevel() {
//     auto trash = freopen("..\\out\\new_level.txt", "w", stdout);
//     if (trash == NULL)
//         throw std::logic_error("Can't find the path to the new_level.txt");
//     std::cout << n_rows << ' ' << n_cols << '\n';
//     for (std::ptrdiff_t i = 0; i < level.size(); ++i) {
//         for (std::ptrdiff_t j = 0; j < level[i].size(); ++j) {
//             std::cout << level[i][j] << ' ';
//         }
//         std::cout << '\n';
//     }
//     fclose(stdout);
// }

void LevelGenerator::SaveLevel() {
    std::ofstream fw("..\\out\\new_level.txt", std::ofstream::out);
    if (!fw.is_open())
        throw std::logic_error("Can't find the path to the new_level.txt");
    fw << n_rows << ' ' << n_cols << '\n';
    for (std::ptrdiff_t i = 0; i < level.size(); ++i) {
        for (std::ptrdiff_t j = 0; j < level[i].size(); ++j) {
            fw << level[i][j] << ' ';
        }
        fw << '\n';
    }
    fw.close();
}