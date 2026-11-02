#include <iostream>
using namespace std;
 
struct Node {
    int data;
    Node *next;
};
 
Node *topNode = NULL;
 
void push(int value) {
    Node *newNode = new Node;
    newNode->data = value;
    newNode->next = topNode;
    topNode = newNode;
    cout << "Inserted\n";
}
 
void pop() {
    if (topNode == NULL) {
        cout << "Stack Underflow\n";
        return;
    }
 
    Node *temp = topNode;
    cout << "Deleted: " << temp->data << "\n";
    topNode = topNode->next;
    delete temp;
}
 
void display() {
    if (topNode == NULL) {
        cout << "Stack is empty\n";
        return;
    }
 
    Node *temp = topNode;
    while (temp != NULL) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << "\n";
}
 
int main() {
    int choice, value;
 
    do {
        cout << "\n1.Push 2.Pop 3.Display 4.Exit\n";
        cin >> choice;
 
        if (choice == 1) {
            cout << "Enter value: ";
            cin >> value;
            push(value);
        } else if (choice == 2) {
            pop();
        } else if (choice == 3) {
            display();
        }
    } while (choice != 4);
 
    return 0;
}
