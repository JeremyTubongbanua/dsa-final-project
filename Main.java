import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // compare all permutations of time using System.currentTimeMillis()
    }

    // five different sort algorithms

    // insertion sort
    private static List<Integer> insertionSort(List<Integer> unsorted) {
        List<Integer> sorted = new ArrayList<Integer>();
        for (int i = 0; i < unsorted.size(); i++) {
            int j = 0;
            while (j < sorted.size() && unsorted.get(i) > sorted.get(j)) {
                j++;
            }
            sorted.add(j, unsorted.get(i));
        }
        return sorted;
    }

    // selection sort
    private static List<Integer> selectionSort(List<Integer> unsorted) {
        List<Integer> sorted = new ArrayList<Integer>();
        while (unsorted.size() > 0) {
            int min = unsorted.get(0);
            int minIndex = 0;
            for (int i = 1; i < unsorted.size(); i++) {
                if (unsorted.get(i) < min) {
                    min = unsorted.get(i);
                    minIndex = i;
                }
            }
            sorted.add(min);
            unsorted.remove(minIndex);
        }
        return sorted;
    }

    // quick sort
    private static List<Integer> quickSort(List<Integer> unsorted) {
        if (unsorted.size() <= 1) {
            return unsorted;
        }
        int pivot = unsorted.get(0);
        List<Integer> left = new ArrayList<Integer>();
        List<Integer> right = new ArrayList<Integer>();
        for (int i = 1; i < unsorted.size(); i++) {
            if (unsorted.get(i) < pivot) {
                left.add(unsorted.get(i));
            } else {
                right.add(unsorted.get(i));
            }
        }
        List<Integer> sorted = quickSort(left);
        sorted.add(pivot);
        sorted.addAll(quickSort(right));
        return sorted;
    }

    // bubble sort
    private static List<Integer> bubbleSort(List<Integer> unsorted) {
        List<Integer> sorted = new ArrayList<Integer>(unsorted);
        for (int i = 0; i < sorted.size(); i++) {
            for (int j = 0; j < sorted.size() - 1; j++) {
                if (sorted.get(j) > sorted.get(j + 1)) {
                    int temp = sorted.get(j);
                    sorted.set(j, sorted.get(j + 1));
                    sorted.set(j + 1, temp);
                }
            }
        }
        return sorted;
    }

    // merge sort
    private static List<Integer> merge(List<Integer> left, List<Integer> right) {
        List<Integer> merged = new ArrayList<Integer>();
        int leftIndex = 0;
        int rightIndex = 0;
        while (leftIndex < left.size() && rightIndex < right.size()) {
            if (left.get(leftIndex) < right.get(rightIndex)) {
                merged.add(left.get(leftIndex));
                leftIndex++;
            } else {
                merged.add(right.get(rightIndex));
                rightIndex++;
            }
        }
        while (leftIndex < left.size()) {
            merged.add(left.get(leftIndex));
            leftIndex++;
        }
        while (rightIndex < right.size()) {
            merged.add(right.get(rightIndex));
            rightIndex++;
        }
        return merged;
    }

    private static List<Integer> mergeSort(List<Integer> unsorted) {
        if (unsorted.size() <= 1) {
            return unsorted;
        }
        int mid = unsorted.size() / 2;
        List<Integer> left = new ArrayList<Integer>();
        List<Integer> right = new ArrayList<Integer>();
        for (int i = 0; i < mid; i++) {
            left.add(unsorted.get(i));
        }
        for (int i = mid; i < unsorted.size(); i++) {
            right.add(unsorted.get(i));
        }
        left = mergeSort(left);
        right = mergeSort(right);
        return merge(left, right);
    }
}