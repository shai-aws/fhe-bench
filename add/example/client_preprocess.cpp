#include <fstream>
#include <iostream>

using namespace std;

int main(){
    double q, d;

    std::ifstream db("../datasets/DB.txt");
    if (!db.is_open())
        throw std::runtime_error("Cannot open ../datasets/DB.txt");
    if (!(db >> d))
        throw std::runtime_error("Failed to read double from ../datasets/DB.txt");

    std::ifstream qry("../datasets/query.txt");
    if (!qry.is_open())
        throw std::runtime_error("Cannot open ../datasets/query.txt");
    if (!(qry >> q))
        throw std::runtime_error("Failed to read double from ../datasets/query.txt");

    std::ofstream("../io/plain_db.bin", std::ios::binary).write((char*)&d, sizeof(double));
    std::ofstream("../io/plain_q.bin", std::ios::binary).write((char*)&q, sizeof(double));
}