#include <iostream>
using namespace std;
 
int q[5];
int front = -1, rear = -1;
 
void enqueue(int value) {
    if ((rear + 1) % 5 == front) {
        cout << "Queue is full\n";
        return;
    }
 
    if (front == -1)
        front = 0;
 
    rear = (rear + 1) % 5;
    q[rear] = value;
    cout << "Inserted\n";
}
 
void dequeue() {
    if (front == -1) {
        cout << "Queue is empty\n";
        return;
    }
 
    cout << "Deleted: " << q[front] << "\n";
 
    if (front == rear) {
        front = rear = -1;
    } else {
        front = (front + 1) % 5;
    }
}
 
void display() {
    if (front == -1) {
        cout << "Queue is empty\n";
        return;
    }
 
    int i = front;
    while (true) {
        cout << q[i] << " ";
        if (i == rear) break;
        i = (i + 1) % 5;
    }
    cout << "\n";
}
 
int main() {
    int choice, value;
 
    do {
        cout << "\n1.Enqueue 2.Dequeue 3.Display 4.Exit\n";
        cin >> choice;
 
        if (choice == 1) {
            cout << "Enter value: ";
            cin >> value;
            enqueue(value);
        } else if (choice == 2) {
            dequeue();
        } else if (choice == 3) {
            display();
        }
    } while (choice != 4);
 
    return 0;
}
