#include <iostream>
#include <stack>
#include <algorithm>
#include <string>
using namespace std;
 
int precedence(char op) {
    if (op == '^') return 3;
    if (op == '*' || op == '/') return 2;
    if (op == '+' || op == '-') return 1;
    return 0;
}
 
int main() {
    string infix, prefix = "";
    stack<char> st;
 
    cout << "Enter infix expression: ";
    cin >> infix;
 
    reverse(infix.begin(), infix.end());
 
    for (int i = 0; i < (int)infix.length(); i++) {
        if (infix[i] == '(')
            infix[i] = ')';
        else if (infix[i] == ')')
            infix[i] = '(';
    }
 
    for (char ch : infix) {
        if (isalnum(ch)) {
            prefix += ch;
        } else if (ch == '(') {
            st.push(ch);
        } else if (ch == ')') {
            while (!st.empty() && st.top() != '(') {
                prefix += st.top();
                st.pop();
            }
            if (!st.empty()) st.pop();
        } else {
            while (!st.empty() && st.top() != '(' &&
                   precedence(st.top()) > precedence(ch)) {
                prefix += st.top();
                st.pop();
            }
            st.push(ch);
        }
    }
 
    while (!st.empty()) {
        prefix += st.top();
        st.pop();
    }
 
    reverse(prefix.begin(), prefix.end());
    cout << "Prefix: " << prefix;
 
    return 0;
}
