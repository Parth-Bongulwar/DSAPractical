#include <iostream>
using namespace std;
 
struct Student {
    int id;
    string name;
    float cgpa;
};
 
int main() {
    int n, key;
    cout << "Enter number of students: ";
    cin >> n;
 
    Student *s = new Student[n];
 
    for (int i = 0; i < n; i++) {
        cout << "Enter ID, name and CGPA: ";
        cin >> s[i].id >> s[i].name >> s[i].cgpa;
    }
 
    cout << "Enter ID to search: ";
    cin >> key;
 
    int pos = -1;
    for (int i = 0; i < n; i++) {
        if (s[i].id == key) {
            pos = i;
            break;
        }
    }
 
    if (pos != -1) {
        cout << "Student Found\n";
        cout << s[pos].id << " " << s[pos].name << " " << s[pos].cgpa;
    } else {
        cout << "Student Not Found";
    }
 
    delete[] s;
    return 0;
}
 
