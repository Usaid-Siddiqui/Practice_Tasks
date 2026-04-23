#include <vector>
#include <iostream>

using namespace std;
template<typename T>
vector<vector<T>> matrixMultiply(const vector<vector<T>>& m1, const vector<vector<T>>& m2);

template<typename T>
vector<vector<T>> transpose(const vector<vector<T>>& A);

template<typename T>
vector<vector<T>> linearRegression(const vector<vector<T>>& X, const vector<vector<T>>& y);


int main() {
    vector<vector<double>> X = {
        {1, 1000, 2},
        {1, 1500, 3},
        {1, 1200, 2},
        {1, 2000, 4}
    };

    vector<vector<double>> y = {
        {200},
        {300},
        {240},
        {450}
    };

    auto b = linearRegression(X, y);

    cout << "Intercept:          " << b[0][0] << "\n";
    cout << "Price per sqft:     " << b[1][0] << "\n";
    cout << "Price per bedroom:  " << b[2][0] << "\n";

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
    vector<vector<T>> B(n,vector<T>(m,0));

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
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            aug[i][j] = A[i][j];
        aug[i][i+n] = 1;
    }

    // elimination
    for (int col = 0; col < n; col++) {
        // find pivot, the largest absolute element in the column
        int pivot = col;
        for (int row = col + 1; row < n; row++) {
            if (abs(aug[row][col]) > abs(aug[pivot][col])) {
                pivot = row;
            }
        }

        swap(aug[col], aug[pivot]);
        // if the largest value in the column is 0, matrix is non invertable
        if (aug[col][col] == 0) {
            cout << "Matrix is singular, cannot invert." << endl;
            return {};
        }

        T scale = aug[col][col];
        for (int j = 0; j < 2*n; j++) {
            aug[col][j] /= scale;
        }

        for (int row = 0; row < n; row++) {
            if (row == col) continue;
            T factor = aug[row][col];
            for (int j = 0; j < 2 * n; j++)
                aug[row][j] -= factor * aug[col][j];
        }
    }

    // Right half of matrix is now inverse
    vector<vector<T>> inv(n, vector<T>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            inv[i][j] = aug[i][j + n];

    return inv;
}

template<typename T>
vector<vector<T>> linearRegression(const vector<vector<T>>& X, const vector<vector<T>>& y) {
    auto Xt     = transpose(X);
    auto XtX    = matrixMultiply(Xt, X);
    auto XtXinv = findInverse(XtX);       // use Gauss-Jordan for stability
    auto Xty    = matrixMultiply(Xt, y);
    return matrixMultiply(XtXinv, Xty);
}