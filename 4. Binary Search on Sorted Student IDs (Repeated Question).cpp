#include <iostream>
#include <algorithm>
using namespace std;
 
int main() {
    int n, key, id[100];
    cout << "Enter number of IDs: ";
    cin >> n;
 
    for (int i = 0; i < n; i++)
        cin >> id[i];
 
    sort(id, id + n);
 
    int left = 0, right = n - 1, pos = -1;
    cout << "Enter ID to search: ";
    cin >> key;
 
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
 
    if (pos == -1)
        cout << "ID not found";
    else
        cout << "ID found at index " << pos;
 
    return 0;
}
