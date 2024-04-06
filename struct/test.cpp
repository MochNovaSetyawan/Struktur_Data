#include <iostream>
#include <string>

using namespace std;

struct Mahasiswa {
    string name;
    int age;
    string address;
};

int main() {
    Mahasiswa mhs;
    mhs.name = "John Lennon";
    mhs.age = 20;
    mhs.address = "Kabupaten Tangerang";

    cout << "Name : " << mhs.name << endl;
    cout << "Name : " << mhs.age << endl;
    cout << "Name : " << mhs.address << endl;

    return 0;
}