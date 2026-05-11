#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <omp.h>

using namespace std;

bool isSorted(vector<int> &arr){
    for(int i = 1; i<arr.size(); i++){
        if(arr[i] < arr[i-1]){
            return false;
        }
    }
    return true;
}

void bubbleSort(vector<int> &arr){
    int n = arr.size();
    for(int i = 0; i<n-1; i++){
        for(int j =0; j<n-i-1; j++){
            if(arr[j] > arr[j+1]){
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

void parallelBubbleSort(vector<int> &arr){
    int n = arr.size();

    for(int i =0; i<n; i++){
        if(i%2 == 0){
            #pragma omp for
            for(int j = 0; j<n-1; j+=2){
                if(arr[j] >arr[j+1]){
                    swap(arr[j], arr[j + 1]);
                }
            }
        } 
        else{
            #pragma omp for
            for(int j = 1; j<n-1; j+=2){
                if(arr[j] >arr[j+1]){
                    swap(arr[j], arr[j + 1]);
                }
            }
        }
    }
}

void merge(vector<int> &arr, int l, int r, int m){
    int n1 = m-l+1;
    int n2 = r-m;

    vector<int> L(n1), R(n2);

    
}