#include <iostream>
#include <level_generator\level_generator.h>

int main(int argc, char* argv[]) {
    std::cout << "App started\n";
    long long rows = atoi(argv[1]);
    long long columns = atoi(argv[2]);
    LevelGenerator m = LevelGenerator(rows, columns);
    std::cout << "Generating level...\n";
    m.GenerateLevel();
    std::cout << "Saving level...\n";
    m.SaveLevel();
    std::cout << "Done!\n";
    return 0;
}