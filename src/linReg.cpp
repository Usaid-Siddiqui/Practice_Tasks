#include <vector>
#include <iostream>

using namespace std;
template<typename T>
vector<vector<T>> matrixMultiply(const vector<vector<T>>& m1, const vector<vector<T>>& m2);

template<typename T>
vector<vector<T>> transpose(const vector<vector<T>>& A);


int main() {


    return 0;
}

template<typename T>
vector<vector<T>> matrixMultiply(const vector<vector<T>>& m1, const vector<vector<T>>& m2) {
    int m = m1.size(), n = m1[0].size(), p = m2.size(), q = m2[0].size();
    vector<vector<T>> output(m, vector<T>(q,0));
    if (n != p) {
        cout << "Error. Matrix size doesn't match." << endl;
        return output;
    }

    for (int i = 0; i < m; i++) 
        for (int j = 0; j < q; j++) 
            for (int k = 0; k < n; k++) 
                output[i][j] += m1[i][k] * m2[k][j];

    return output;
}

template<typename T>
vector<vector<T>> transpose(const vector<vector<T>>& A) {
    int m = A.size(), n = A[0].size();
    vector<vector<T> B(n,vector<T>(m,0));

    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            B[j][i] = A[i][j];

    return B;
}

template<typename T>
vector<vector<T>> findInverse(const vector<vector<T>>& A) {
    int n = A.size();

    // build augmented matrix
    vector<vector<T>> aug(n, vector<T>(2*n,0));
    for int (i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            aug[i][j] = A[i][j];
        aug[i][i+n] = 1;
    }

    // elimination
    for (int col = 0; col < n; col++) {
        
    }
}