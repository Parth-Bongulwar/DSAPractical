#include <iostream>
#include <algorithm>
using namespace std;
 
int main() {
    int n, key;
    cout << "Enter number of IDs: ";
    cin >> n;
 
    int id[100];
    cout << "Enter student IDs: ";
    for (int i = 0; i < n; i++)
        cin >> id[i];
 
    sort(id, id + n);
 
    cout << "Sorted IDs: ";
    for (int i = 0; i < n; i++)
        cout << id[i] << " ";
 
    cout << "\nEnter ID to search: ";
    cin >> key;
 
    int left = 0, right = n - 1, pos = -1;
 
    while (left <= right) {
        int mid = (left + right) / 2;
 
        if (id[mid] == key) {
            pos = mid;
            break;
        } else if (key < id[mid]) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
 
    if (pos != -1)
        cout << "ID found at index " << pos;
    else
        cout << "ID not found";
 
    return 0;
}
