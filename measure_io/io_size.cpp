#include <filesystem>
#include <iostream>

int main(){
    std::uintmax_t bytes = 0;
    for (auto& p: std::filesystem::recursive_directory_iterator("io"))
        if (p.is_regular_file()) bytes += p.file_size();
    std::cout << bytes << std::endl;
}
